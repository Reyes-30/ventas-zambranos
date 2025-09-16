"""
Módulo de Utilidades de Entrada/Salida (I/O Utils)
================================================

Este módulo proporciona funciones seguras y robustas para el manejo de archivos
en el Sistema de Análisis de Ventas Zambranos. Incluye:

- Lectura segura de archivos CSV y Excel con detección automática de formato
- Validación exhaustiva de esquemas de datos
- Escritura atómica de archivos con locks para evitar corrupción
- Sistema de hashing para identificación única de archivos
- Coerción inteligente de tipos de datos

Características de Seguridad:
- Atomic writes para prevenir corrupción de archivos
- File locking para acceso concurrente seguro
- Validación de esquemas antes del procesamiento
- Hashing SHA-256 para integridad de datos

Author: Equipo de Desarrollo Zambranos
Version: 2.0
"""

import csv
import hashlib
import io
import os
from pathlib import Path
from typing import Optional, Tuple

import pandas as pd
from filelock import FileLock

from .exceptions import FileIOError, ValidationError

# Configuración de Directorios del Sistema
# ========================================
# Estructura de almacenamiento organizada para separar
# datos de entrada (uploads) y salida (outputs)

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
UPLOADS_DIR = DATA_DIR / "uploads"  # Archivos subidos por usuarios
OUTPUTS_DIR = DATA_DIR / "outputs"  # Resultados y exportaciones

# Crear directorios si no existen
UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

# Esquema de Datos Requerido
# ==========================
# Columnas obligatorias que debe contener cualquier archivo de datos
# para ser procesado por el sistema de análisis

REQUIRED_COLUMNS = [
    "Mes",              # Nombre del mes en español (ej: "Enero", "Febrero")
    "Categoría",        # Categoría del producto/servicio
    "Cantidad Vendida", # Número de unidades vendidas (entero/float)
    "Ingreso Total",    # Ingresos totales en moneda local (float)
    "ISV",              # Impuesto sobre ventas (float)
    "Utilidad Bruta"    # Ganancia bruta calculada (float)
]


def _sniff_delimiter(sample: bytes) -> Optional[str]:
    """
    Detecta automáticamente el delimitador de un archivo CSV.

    Utiliza el módulo csv.Sniffer de Python para analizar una muestra
    del archivo y determinar el delimitador más probable.

    Args:
        sample (bytes): Muestra de bytes del inicio del archivo CSV

    Returns:
        Optional[str]: Delimitador detectado (',', ';', '\t', etc.) o None si falla

    Examples:
        >>> delimiter = _sniff_delimiter(b"col1,col2,col3\n1,2,3")
        >>> print(delimiter)  # ','
    """
    try:
        # Decodificar muestra con manejo de errores para caracteres especiales
        text_sample = sample.decode("utf-8", errors="ignore")
        dialect = csv.Sniffer().sniff(text_sample)
        return dialect.delimiter
    except Exception:
        # Si falla la detección, retornar None para usar delimitador por defecto
        return None


def file_sha256(content: bytes) -> str:
    """
    Calcula hash SHA-256 de contenido de archivo para identificación única.

    El hash se usa para:
    - Evitar duplicación de archivos
    - Verificar integridad de datos
    - Generar nombres únicos de archivo

    Args:
        content (bytes): Contenido completo del archivo

    Returns:
        str: Hash SHA-256 en formato hexadecimal

    Examples:
        >>> hash_val = file_sha256(b"contenido del archivo")
        >>> print(len(hash_val))  # 64 caracteres
    """
    return hashlib.sha256(content).hexdigest()


def save_upload_safely(filename: str, content: bytes) -> Path:
    """
    Guarda archivo subido de forma atómica y segura con hash único.

    Implementa las siguientes medidas de seguridad:
    - Escritura atómica usando archivo temporal
    - File locking para prevenir acceso concurrente
    - Nombres únicos basados en hash para evitar colisiones
    - Sincronización forzada al disco (fsync)

    Args:
        filename (str): Nombre original del archivo
        content (bytes): Contenido binario del archivo

    Returns:
        Path: Ruta al archivo guardado con nombre hash-único

    Raises:
        FileIOError: Si falla la escritura o el lock del archivo

    Examples:
        >>> saved_path = save_upload_safely("ventas.csv", csv_content)
        >>> print(saved_path.name)  # "ventas-a1b2c3d4.csv"

    Note:
        El archivo se guarda como "{nombre}-{hash_12_chars}.{extension}"
        donde hash_12_chars son los primeros 12 caracteres del SHA-256.
    """
    # Generar hash truncado para nombre único
    digest = file_sha256(content)[:12]
    safe_name = f"{Path(filename).stem}-{digest}{Path(filename).suffix}"
    target = UPLOADS_DIR / safe_name

    # Usar lock de archivo para operación atómica
    lock = FileLock(str(target) + ".lock")
    with lock:
        # Escribir a archivo temporal primero
        tmp_path = target.with_suffix(target.suffix + ".tmp")
        with open(tmp_path, "wb") as f:
            f.write(content)
            f.flush()  # Forzar flush del buffer
            os.fsync(f.fileno())  # Forzar sincronización al disco
        
        # Mover atómicamente de temporal a final
        os.replace(tmp_path, target)
    
    return target


def read_dataframe(path_or_bytes: bytes | str | Path, delimiter: str | None = None) -> pd.DataFrame:
    """
    Lee archivo de datos de múltiples formatos con detección automática.

    Esta función es el núcleo del sistema de lectura de archivos, capaz de manejar:
    - Archivos CSV con detección automática de delimitador
    - Archivos Excel (.xlsx, .xls)
    - Archivos Parquet (para futuras extensiones)
    - Contenido en memoria (bytes) desde uploads web

    Args:
        path_or_bytes (bytes | str | Path): Ruta al archivo o contenido en bytes
        delimiter (str | None): Delimitador específico para CSV, None para auto-detección

    Returns:
        pd.DataFrame: DataFrame cargado y listo para procesamiento

    Raises:
        FileIOError: Si no se puede leer el archivo o el formato no es soportado

    Examples:
        >>> # Leer desde archivo local
        >>> df = read_dataframe("datos/ventas.csv")
        
        >>> # Leer desde bytes con delimitador específico
        >>> df = read_dataframe(file_content, delimiter=";")
        
        >>> # Leer Excel
        >>> df = read_dataframe("reporte.xlsx")

    Note:
        Para archivos CSV en bytes, primero intenta leer como CSV con el delimitador
        detectado/especificado. Si falla, intenta leer como Excel automáticamente.
    """
    try:
        if isinstance(path_or_bytes, (str, Path)):
            # Lectura desde archivo local
            path = Path(path_or_bytes)
            suf = path.suffix.lower()
            
            if suf in [".xlsx", ".xls"]:
                # Archivos Excel usando engine por defecto
                return pd.read_excel(path)
            elif suf == ".parquet":
                # Soporte futuro para Parquet (datos grandes)
                return pd.read_parquet(path)
            else:
                # CSV con delimitador específico o detección automática
                return pd.read_csv(path, sep=delimiter or ",")
        else:
            # Lectura desde bytes (upload web)
            sample = path_or_bytes[:4096]  # Muestra para detección de delimitador
            sep = delimiter
            
            if sep is None:
                # Auto-detección de delimitador usando muestra
                sniff = _sniff_delimiter(sample)
                sep = sniff or ","  # Fallback a coma si falla detección
            
            # Crear buffer de bytes y intentar lectura
            bio = io.BytesIO(path_or_bytes)
            bio.seek(0)
            
            try:
                # Primer intento: CSV con delimitador detectado/especificado
                return pd.read_csv(bio, sep=sep)
            except Exception:
                # Segundo intento: Excel (algunos CSV problemáticos se abren como Excel)
                bio.seek(0)
                return pd.read_excel(bio)
                
    except Exception as e:
        # Convertir cualquier error a nuestra excepción personalizada
        raise FileIOError("No se pudo leer el archivo", detail=str(e))


def validate_schema(df: pd.DataFrame) -> None:
    """
    Valida que el DataFrame contenga todas las columnas requeridas para el análisis.

    Esta función es crítica para garantizar que los datos cargados puedan ser
    procesados correctamente por todos los módulos de análisis del sistema.

    Args:
        df (pd.DataFrame): DataFrame a validar

    Raises:
        ValidationError: Si faltan una o más columnas requeridas, incluye:
                        - Lista de columnas faltantes en el mensaje
                        - Lista completa de columnas requeridas en detail

    Examples:
        >>> validate_schema(df)  # Pasa silenciosamente si es válido
        >>> validate_schema(df_incompleto)  # Raises ValidationError

    Note:
        Esta función no modifica el DataFrame, solo valida su estructura.
        Las columnas adicionales no listadas en REQUIRED_COLUMNS son permitidas.
    """
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValidationError(
            message=f"Faltan columnas requeridas: {', '.join(missing)}",
            detail=f"Requeridas: {REQUIRED_COLUMNS}"
        )


def coerce_numeric(df: pd.DataFrame, numeric_cols: list[str]) -> pd.DataFrame:
    """
    Convierte columnas especificadas a tipos numéricos con manejo de errores.

    Utiliza pandas.to_numeric con errors='coerce' para convertir valores no
    numéricos a NaN en lugar de fallar. Esto permite procesar datos con
    inconsistencias de formato.

    Args:
        df (pd.DataFrame): DataFrame original
        numeric_cols (list[str]): Lista de nombres de columnas a convertir

    Returns:
        pd.DataFrame: Copia del DataFrame con columnas convertidas a numéricas

    Examples:
        >>> df_clean = coerce_numeric(df, ['Cantidad Vendida', 'Ingreso Total'])
        >>> print(df_clean['Cantidad Vendida'].dtype)  # float64

    Note:
        - Solo procesa columnas que existen en el DataFrame
        - Valores no convertibles se vuelven NaN (no genera errores)
        - Retorna una copia, no modifica el DataFrame original
    """
    dfn = df.copy()
    for c in numeric_cols:
        if c in dfn.columns:
            # Conversión segura: valores inválidos → NaN
            dfn[c] = pd.to_numeric(dfn[c], errors="coerce")
    return dfn
