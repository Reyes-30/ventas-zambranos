"""
Módulo de Procesamiento de Datos y Análisis
==========================================

Este módulo contiene todas las funciones de lógica de negocio para el análisis
de datos de ventas, incluyendo:

- Cálculo de métricas ejecutivas y KPIs
- Análisis de series temporales por mes
- Agregaciones por categoría de producto
- Algoritmos de Machine Learning (PCA, K-Means)
- Estructuras de datos optimizadas para resultados

El módulo está diseñado para ser independiente de la interfaz, permitiendo
uso tanto en aplicaciones web como en scripts de análisis batch.

Características principales:
- Funciones puras sin efectos secundarios
- Manejo robusto de datos faltantes
- Optimización para pandas DataFrames
- Resultados estructurados con dataclasses

Author: Equipo de Desarrollo Zambranos
Version: 2.0
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

from .exceptions import ProcessingError

# Configuración de Ordenamiento Temporal
# ======================================
# Define el orden cronológico correcto de los meses para análisis temporal
# Crucial para gráficas y análisis de tendencias estacionales

MESES_ORDEN = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre",
]

# Variables Numéricas para Análisis Estadístico
# =============================================
# Lista de columnas numéricas que pueden ser usadas en análisis estadísticos,
# correlaciones y algoritmos de machine learning

VARIABLES_NUM = [
    'Cantidad Vendida',   # Unidades vendidas
    'Precio Unitario',    # Precio por unidad
    'Ingreso Total',      # Ingresos totales
    'Costo Unitario',     # Costo por unidad
    'Costo Total',        # Costos totales
    'Utilidad Bruta',     # Ganancia bruta
    'ISV',                # Impuesto sobre ventas
    'Ingreso Neto'        # Ingreso después de costos
]


def resumen_metricas(df: pd.DataFrame) -> Dict[str, float]:
    """
    Calcula métricas ejecutivas principales del negocio.

    Esta función genera los KPIs más importantes para dashboards ejecutivos
    y reportes de rendimiento. Todas las métricas son calculadas de forma
    robusta con manejo de valores faltantes.

    Args:
        df (pd.DataFrame): DataFrame con datos de ventas validados

    Returns:
        Dict[str, float]: Diccionario con métricas principales:
            - total_ingresos: Suma de todos los ingresos
            - total_isv: Suma de impuestos sobre ventas
            - utilidad_promedio: Media de utilidad bruta
            - total_ventas: Suma de unidades vendidas
            - categorias_unicas: Número de categorías diferentes
            - meses_activos: Número de meses con datos

    Examples:
        >>> metricas = resumen_metricas(df)
        >>> print(f"Ingresos: ${metricas['total_ingresos']:,.2f}")

    Note:
        Todas las sumas ignoran valores NaN automáticamente (pandas default).
        Los tipos se convierten explícitamente para compatibilidad JSON.
    """
    return {
        "total_ingresos": float(df['Ingreso Total'].sum()),
        "total_isv": float(df['ISV'].sum()),
        "utilidad_promedio": float(df['Utilidad Bruta'].mean()),
        "total_ventas": float(df['Cantidad Vendida'].sum()),
        "categorias_unicas": int(df['Categoría'].nunique()),
        "meses_activos": int(df['Mes'].nunique()),
    }


def series_temporales(df: pd.DataFrame) -> Dict[str, pd.Series]:
    """
    Calcula series temporales agregadas por mes para análisis de tendencias.

    Agrupa los datos por mes y calcula totales de ingresos e ISV, manteniendo
    el orden cronológico correcto usando MESES_ORDEN. Útil para gráficas
    de líneas temporales y análisis estacional.

    Args:
        df (pd.DataFrame): DataFrame con columna 'Mes' en español

    Returns:
        Dict[str, pd.Series]: Diccionario con series temporales:
            - "ingresos": Series con ingresos totales por mes
            - "isv": Series con ISV total por mes
            Ambas series están indexadas por mes en orden cronológico.

    Examples:
        >>> series = series_temporales(df)
        >>> mejor_mes = series["ingresos"].idxmax()
        >>> print(f"Mejor mes: {mejor_mes}")

    Note:
        Usa reindex() para garantizar orden cronológico, rellenando con NaN
        los meses sin datos. Esto es crítico para gráficas temporales correctas.
    """
    # Agrupar por mes y sumar, luego reordenar cronológicamente
    ingresos = df.groupby('Mes')['Ingreso Total'].sum().reindex(MESES_ORDEN)
    isv = df.groupby('Mes')['ISV'].sum().reindex(MESES_ORDEN)
    return {"ingresos": ingresos, "isv": isv}


def categoria_agg(df: pd.DataFrame) -> Dict[str, pd.Series | pd.DataFrame]:
    """
    Calcula agregaciones por categoría de producto para análisis de segmentos.

    Genera estadísticas resumidas por categoría que son fundamentales para
    entender qué productos/servicios impulsan el negocio.

    Args:
        df (pd.DataFrame): DataFrame con columnas 'Categoría', 'Cantidad Vendida', 'Utilidad Bruta'

    Returns:
        Dict[str, pd.Series | pd.DataFrame]: Resultados por categoría:
            - "ventas": Series con total de unidades vendidas por categoría
            - "utilidad": DataFrame con media y suma de utilidad por categoría

    Examples:
        >>> agg = categoria_agg(df)
        >>> top_categoria = agg["ventas"].idxmax()
        >>> print(f"Categoría top en ventas: {top_categoria}")

    Note:
        La utilidad se calcula tanto como promedio (para comparar márgenes)
        como suma total (para comparar contribución absoluta al negocio).
    """
    # Total de unidades vendidas por categoría
    ventas = df.groupby('Categoría')['Cantidad Vendida'].sum()
    
    # Utilidad promedio y total por categoría (redondeado para legibilidad)
    utilidad = df.groupby('Categoría')['Utilidad Bruta'].agg(['mean', 'sum']).round(2)
    
    return {"ventas": ventas, "utilidad": utilidad}


# Estructuras de Datos para Resultados de Machine Learning
# =======================================================

@dataclass
class PCAResult:
    """
    Resultado estructurado del análisis de Componentes Principales (PCA).

    Attributes:
        components (np.ndarray): Datos transformados en espacio de componentes principales
                                Shape: (n_samples, n_components)
        explained (np.ndarray): Proporción de varianza explicada por cada componente
                               Shape: (n_components,), suma <= 1.0

    Examples:
        >>> result = run_pca(df, variables, n_components=2)
        >>> total_variance = result.explained.sum()
        >>> print(f"Varianza explicada total: {total_variance:.2%}")

    Note:
        Los componentes están ordenados por varianza explicada (descendente).
        El primer componente siempre explica la mayor varianza.
    """
    components: np.ndarray
    explained: np.ndarray


@dataclass
class ClusterResult:
    """
    Resultado estructurado del análisis de clustering K-Means.

    Attributes:
        labels (np.ndarray): Etiquetas de cluster para cada observación
                            Shape: (n_samples,), valores: 0 a k-1
        centers (np.ndarray): Centroides de cada cluster en espacio escalado
                             Shape: (k, n_features)
    perfil (pd.DataFrame): Perfil agregado por clúster (media por variables numéricas)
                  Index: 0..k-1, Columnas: variables numéricas

    Examples:
        >>> result = run_kmeans(df, variables, k=3)
        >>> cluster_sizes = pd.Series(result.labels).value_counts()
        >>> print(f"Tamaños de clusters: {cluster_sizes.to_dict()}")

    Note:
        Los centroides están en espacio escalado (StandardScaler).
        Use el perfil para interpretar características en unidades originales.
    """
    labels: np.ndarray
    centers: np.ndarray
    perfil: pd.DataFrame


def run_pca(df: pd.DataFrame, variables: List[str], n_components: int = 2) -> PCAResult:
    """
    Ejecuta Análisis de Componentes Principales (PCA) para reducción dimensional.

    PCA es útil para:
    - Visualizar datos multidimensionales en 2D/3D
    - Identificar las direcciones de mayor varianza
    - Reducir la dimensionalidad preservando información
    - Detectar patrones ocultos en los datos

    Args:
        df (pd.DataFrame): DataFrame con datos numéricos
        variables (List[str]): Lista de columnas numéricas a incluir en el análisis
        n_components (int): Número de componentes principales a calcular (default: 2)

    Returns:
        PCAResult: Objeto con componentes transformados y varianza explicada

    Raises:
        ProcessingError: Si hay problemas con los datos o el cálculo

    Examples:
        >>> variables = ['Ingreso Total', 'Utilidad Bruta', 'Cantidad Vendida']
        >>> result = run_pca(df, variables, n_components=2)
        >>> print(f"Varianza explicada: {result.explained}")

    Note:
        - Los datos se escalan automáticamente (StandardScaler)
        - Las filas con NaN se excluyen del análisis
        - Los componentes están ordenados por varianza explicada
    """
    try:
        # Seleccionar variables y remover filas con valores faltantes
        X = df[variables].dropna()
        
        if len(X) == 0:
            raise ProcessingError("No hay datos válidos después de remover NaN")
        
        # Escalar datos para que todas las variables tengan igual peso
        X_scaled = StandardScaler().fit_transform(X)
        
        # Aplicar PCA con número de componentes especificado
        pca = PCA(n_components=n_components)
        components_transformed = pca.fit_transform(X_scaled)
        
        return PCAResult(
            components=components_transformed,
            explained=pca.explained_variance_ratio_
        )
        
    except Exception as e:
        raise ProcessingError("Error ejecutando PCA", detail=str(e))


def run_kmeans(df: pd.DataFrame, variables: List[str], k: int) -> ClusterResult:
    """
    Ejecuta clustering K-Means para segmentación de datos.

    K-Means es útil para:
    - Segmentar clientes/productos en grupos similares
    - Identificar patrones naturales en los datos
    - Crear perfiles de comportamiento
    - Optimizar estrategias por segmento

    Args:
        df (pd.DataFrame): DataFrame con datos numéricos
        variables (List[str]): Lista de columnas numéricas para clustering
        k (int): Número de clusters a crear

    Returns:
        ClusterResult: Objeto con etiquetas, centroides y perfil completo

    Raises:
        ProcessingError: Si hay problemas con los datos o el cálculo

    Examples:
        >>> variables = ['Ingreso Total', 'Utilidad Bruta', 'Cantidad Vendida']
        >>> result = run_kmeans(df, variables, k=3)
        >>> perfil_por_cluster = result.perfil.groupby('Cluster').mean()

    Note:
        - Los datos se escalan automáticamente (StandardScaler)
        - Se usa random_state=42 para resultados reproducibles
        - Los centroides están en espacio escalado
        - El perfil contiene datos originales + columna 'Cluster'
    """
    try:
        # Seleccionar variables y remover filas con valores faltantes
        X = df[variables].dropna()
        
        if len(X) < k:
            raise ProcessingError(f"No hay suficientes datos ({len(X)}) para {k} clusters")
        
        # Escalar datos para que todas las variables tengan igual peso
        X_scaled = StandardScaler().fit_transform(X)
        
        # Aplicar K-Means con configuración reproducible
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = kmeans.fit_predict(X_scaled)
        
        # Crear perfil agregado (media por clúster) para análisis rápido
        df_tmp = df.loc[X.index].copy()
        df_tmp['Cluster'] = labels
        perfil = df_tmp.groupby('Cluster')[variables].mean().round(4)

        return ClusterResult(
            labels=labels,
            centers=kmeans.cluster_centers_,
            perfil=perfil
        )
    except Exception as e:
        raise ProcessingError("Error ejecutando K-Means", detail=str(e))
