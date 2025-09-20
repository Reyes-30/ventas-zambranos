import io
import pandas as pd
from pathlib import Path

base = Path(__file__).resolve().parent
out = base / 'ventas_multi_hoja.xlsx'

# Hoja Datos con columnas requeridas
hoja1 = pd.DataFrame({
    'Mes': ['Julio', 'Agosto', 'Septiembre'],
    'Categoría': ['Higiene', 'Bebidas', 'Snacks'],
    'Cantidad Vendida': [55, 200, 180],
    'Ingreso Total': [4950, 25000, 21600],
    'ISV': [742.5, 3750, 3240],
    'Utilidad Bruta': [1500, 8200, 6500],
})

# Hoja Otra con nombres "sucios" para probar mapeo
hoja2 = pd.DataFrame({
    'periodo': ['Octubre', 'Noviembre'],
    'categoria producto': ['Limpieza', 'Higiene'],
    'unidades vendidas': [100, 120],
    'ventas': [12000, 14400],
    'iva': [1800, 2160],
    'ganancia': [4000, 4800],
})

# Hoja Extra con columnas adicionales
hoja3 = pd.DataFrame({
    'Mes': ['Diciembre'],
    'Categoría': ['Bebidas'],
    'Cantidad Vendida': [300],
    'Ingreso Total': [36000],
    'ISV': [5400],
    'Utilidad Bruta': [12000],
    'Costo Unitario': [80],
    'Ingreso Neto': [30600],
})

with pd.ExcelWriter(out, engine='openpyxl') as writer:
    hoja1.to_excel(writer, index=False, sheet_name='Datos')
    hoja2.to_excel(writer, index=False, sheet_name='Otra')
    hoja3.to_excel(writer, index=False, sheet_name='Extra')

print(f"Archivo generado: {out}")
