import time
import numpy as np
import pandas as pd
from src.app.processing import run_pca, run_kmeans, VARIABLES_NUM


def test_perf_pca_kmeans_smoke(benchmark):
    # dataset sintético ~50k filas
    n = 50000
    n1 = n // 2
    n2 = n - n1
    rng = np.random.default_rng(42)
    # Dos clústeres con medias diferentes en variables numéricas
    df1 = pd.DataFrame({
        'Mes': ['Enero']*n1,
        'Categoría': ['A']*n1,
        'Cantidad Vendida': rng.normal(10, 1, n1),
        'Ingreso Total': rng.normal(100, 5, n1),
        'ISV': rng.normal(15, 1, n1),
        'Utilidad Bruta': rng.normal(30, 2, n1),
        'Precio Unitario': rng.normal(10, 0.5, n1),
        'Costo Unitario': rng.normal(5, 0.3, n1),
        'Costo Total': rng.normal(50, 3, n1),
        'Ingreso Neto': rng.normal(85, 4, n1),
    })
    df2 = pd.DataFrame({
        'Mes': ['Febrero']*n2,
        'Categoría': ['B']*n2,
        'Cantidad Vendida': rng.normal(25, 1, n2),
        'Ingreso Total': rng.normal(220, 5, n2),
        'ISV': rng.normal(33, 1, n2),
        'Utilidad Bruta': rng.normal(70, 2, n2),
        'Precio Unitario': rng.normal(12, 0.5, n2),
        'Costo Unitario': rng.normal(6, 0.3, n2),
        'Costo Total': rng.normal(110, 3, n2),
        'Ingreso Neto': rng.normal(187, 4, n2),
    })
    df = pd.concat([df1, df2], ignore_index=True)

    def _run():
        res_pca = run_pca(df, VARIABLES_NUM, 2)
        res_km = run_kmeans(df, VARIABLES_NUM, 2)
        return res_pca.components.shape, res_km.perfil.shape

    shape_pca, shape_km = benchmark(_run)
    assert shape_pca[1] == 2  # 2 componentes PCA
    assert shape_km[0] == n   # Mismo número de filas que el dataset original
    assert shape_km[1] > 8    # Al menos las columnas originales + cluster
