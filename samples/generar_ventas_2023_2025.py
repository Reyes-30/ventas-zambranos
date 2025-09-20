"""
Genera un archivo Excel con tres hojas (2023, 2024 y 2025 hasta el mes actual)
a partir de `datosExcel.csv`, agregando nuevas categorías y >100 registros.

Salida: samples/ventas_2023_2025.xlsx
"""
from __future__ import annotations

import os
from datetime import datetime
import numpy as np
import pandas as pd


SRC_CSV = os.path.join(os.path.dirname(os.path.dirname(__file__)), "datosExcel.csv")
OUT_XLSX = os.path.join(os.path.dirname(__file__), "ventas_2023_2025.xlsx")

MESES = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
]


def _coerce_numeric(s: pd.Series) -> pd.Series:
    """Convierte una serie con números en texto a float (quita comas, etc.)."""
    return (
        s.astype(str)
        .str.replace(" ", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.replace("$", "", regex=False)
        .str.replace("\"", "", regex=False)
        .str.strip()
        .replace({"": np.nan})
        .astype(float)
    )


def cargar_base(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    # Normalizar nombres de columnas
    df.columns = [c.strip().strip("\"") for c in df.columns]
    # Limpiar comillas en string Mes/Categoría
    for col in ["Mes", "Categoría"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip('" ')

    # Convertir numéricas
    for col in [
        "Cantidad Vendida",
        "Precio Unitario",
        "Ingreso Total",
        "Costo Unitario",
        "Costo Total",
        "Utilidad Bruta",
        "ISV",
        "Ingreso Neto",
    ]:
        if col in df.columns:
            df[col] = _coerce_numeric(df[col])
    return df


def sintetizar_datos(base: pd.DataFrame) -> tuple[list[str], dict[str, tuple[float, float]], np.ndarray]:
    """
    Produce listas/rangos para generar datos: categorías extendidas, medias de
    precio y costo por categoría y distribución de cantidades.
    """
    rng = np.random.default_rng(42)

    categorias_base = sorted(base["Categoría"].unique().tolist())
    categorias_extra = ["Chaquetas", "Zapatos", "Accesorios", "Faldas", "Suéteres"]
    categorias = categorias_base + categorias_extra

    # Rangos realistas de precios en Lempiras (HNL) por categoría
    # Valores de referencia típicos para ropa de marca importada en Honduras
    PRECIOS_HNL_RANGOS: dict[str, tuple[float, float]] = {
        "Pantalones": (1200, 3200),
        "Camisas": (800, 2200),
        "Vestidos": (1600, 4200),
        "Blusas": (700, 1800),
        "Shorts": (600, 1500),
        "Chaquetas": (2000, 5200),
        "Zapatos": (1400, 4200),
        "Accesorios": (200, 900),
        "Faldas": (800, 2200),
        "Suéteres": (900, 2600),
    }

    # Para categorías no listadas explícitamente usar un rango general
    rango_default = (700, 2500)
    precios_rangos: dict[str, tuple[float, float]] = {}
    for cat in categorias:
        precios_rangos[cat] = PRECIOS_HNL_RANGOS.get(cat, rango_default)

    # Distribución de cantidades a partir de los datos originales
    cantidades = base["Cantidad Vendida"].dropna().to_numpy()
    if len(cantidades) == 0:
        cantidades = rng.integers(20, 160, size=200)

    return categorias, precios_rangos, cantidades


def generar_tabla_anual(
    year: int,
    categorias: list[str],
    precios_rangos: dict[str, tuple[float, float]],
    cantidades_pool: np.ndarray,
) -> pd.DataFrame:
    rng = np.random.default_rng(100 + year)
    # Hasta mes actual si year es el vigente
    hoy = datetime.today()
    meses = MESES if year < hoy.year else MESES[: hoy.month]

    registros = []
    tasa_isv = 0.15
    for mes in meses:
        for cat in categorias:
            cant = int(rng.choice(cantidades_pool))
            # Precio en Lempiras dentro del rango de la categoría con una leve variación mensual
            low, high = precios_rangos.get(cat, (700, 2500))
            base_price = rng.uniform(low, high)
            p_unit = float(base_price * rng.uniform(0.95, 1.05))

            # Costo como porcentaje del precio (55% a 75%), asegurando < precio
            c_unit = float(min(p_unit * rng.uniform(0.55, 0.75), p_unit - 5.0))

            ingreso_total = round(cant * p_unit, 2)
            costo_total = round(cant * c_unit, 2)
            utilidad_bruta = round(ingreso_total - costo_total, 2)
            isv = round(ingreso_total * tasa_isv, 2)
            ingreso_neto = round(ingreso_total - isv, 2)

            registros.append(
                {
                    "Mes": mes,
                    "Categoría": cat,
                    "Cantidad Vendida": cant,
                    "Precio Unitario": round(p_unit, 2),
                    "Ingreso Total": ingreso_total,
                    "Costo Unitario": round(c_unit, 2),
                    "Costo Total": costo_total,
                    "Utilidad Bruta": utilidad_bruta,
                    "ISV": isv,
                    "Ingreso Neto": ingreso_neto,
                }
            )

    df = pd.DataFrame(registros)
    # Ordenar columnas como en la base
    cols = [
        "Mes",
        "Categoría",
        "Cantidad Vendida",
        "Precio Unitario",
        "Ingreso Total",
        "Costo Unitario",
        "Costo Total",
        "Utilidad Bruta",
        "ISV",
        "Ingreso Neto",
    ]
    return df[cols]


def main():
    os.makedirs(os.path.dirname(OUT_XLSX), exist_ok=True)

    base = cargar_base(SRC_CSV)
    categorias, precios_rangos, cantidades_pool = sintetizar_datos(base)

    df_2023 = generar_tabla_anual(2023, categorias, precios_rangos, cantidades_pool)
    df_2024 = generar_tabla_anual(2024, categorias, precios_rangos, cantidades_pool)
    df_2025 = generar_tabla_anual(2025, categorias, precios_rangos, cantidades_pool)

    # Guardar a Excel con 3 hojas
    with pd.ExcelWriter(OUT_XLSX, engine="openpyxl") as writer:
        df_2023.to_excel(writer, index=False, sheet_name="2023")
        df_2024.to_excel(writer, index=False, sheet_name="2024")
        df_2025.to_excel(writer, index=False, sheet_name="2025")

    # Pequeña verificación
    print("Archivo creado:", OUT_XLSX)
    print("Filas por hoja:")
    print("2023:", len(df_2023))
    print("2024:", len(df_2024))
    print("2025:", len(df_2025))


if __name__ == "__main__":
    main()
