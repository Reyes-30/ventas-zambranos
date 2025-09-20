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


def sintetizar_datos(base: pd.DataFrame) -> tuple[list[str], dict[str, float], dict[str, float], np.ndarray]:
    """
    Produce listas/rangos para generar datos: categorías extendidas, medias de
    precio y costo por categoría y distribución de cantidades.
    """
    rng = np.random.default_rng(42)

    categorias_base = sorted(base["Categoría"].unique().tolist())
    categorias_extra = ["Chaquetas", "Zapatos", "Accesorios", "Faldas", "Suéteres"]
    categorias = categorias_base + categorias_extra

    # Medias por categoría conocidas
    precio_medias: dict[str, float] = {}
    costo_medias: dict[str, float] = {}
    for cat in categorias_base:
        sub = base[base["Categoría"] == cat]
        precio_medias[cat] = float(sub["Precio Unitario"].mean())
        costo_medias[cat] = float(sub["Costo Unitario"].mean())

    # Para nuevas categorías, derivar valores basados en distribución global
    precio_global = float(base["Precio Unitario"].mean())
    costo_global = float(base["Costo Unitario"].mean())
    for cat in categorias_extra:
        # Variar ±25% alrededor de la media global
        precio_medias[cat] = float(precio_global * rng.uniform(0.75, 1.25))
        # Asegurar costo < precio
        costo_medias[cat] = float(
            min(precio_medias[cat] * rng.uniform(0.55, 0.8), precio_medias[cat] - 1.5)
        )

    # Distribución de cantidades a partir de los datos originales
    cantidades = base["Cantidad Vendida"].dropna().to_numpy()
    if len(cantidades) == 0:
        cantidades = rng.integers(20, 160, size=200)

    return categorias, precio_medias, costo_medias, cantidades


def generar_tabla_anual(
    year: int,
    categorias: list[str],
    precio_medias: dict[str, float],
    costo_medias: dict[str, float],
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
            # Precios con variación del ±20%
            p_unit = float(precio_medias[cat] * rng.uniform(0.8, 1.2))
            c_unit = float(min(costo_medias[cat] * rng.uniform(0.8, 1.15), p_unit * 0.9))

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
    categorias, precio_medias, costo_medias, cantidades_pool = sintetizar_datos(base)

    df_2023 = generar_tabla_anual(2023, categorias, precio_medias, costo_medias, cantidades_pool)
    df_2024 = generar_tabla_anual(2024, categorias, precio_medias, costo_medias, cantidades_pool)
    df_2025 = generar_tabla_anual(2025, categorias, precio_medias, costo_medias, cantidades_pool)

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
