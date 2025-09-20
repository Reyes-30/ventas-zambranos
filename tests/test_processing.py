import pandas as pd
from src.app.processing import resumen_metricas, series_temporales, categoria_agg, run_pca, run_kmeans, VARIABLES_NUM


def sample_df():
    return pd.DataFrame({
        'Mes': ['Enero', 'Febrero', 'Enero', 'Febrero'],
        'Categoría': ['A', 'B', 'A', 'B'],
        'Cantidad Vendida': [10, 20, 5, 15],
        'Ingreso Total': [100, 200, 50, 150],
        'ISV': [15, 30, 7.5, 22.5],
        'Utilidad Bruta': [30, 60, 15, 45],
        'Precio Unitario': [10, 10, 10, 10],
        'Costo Unitario': [5, 5, 5, 5],
        'Costo Total': [50, 100, 25, 75],
        'Ingreso Neto': [85, 170, 42.5, 127.5]
    })


def test_resumen_metricas():
    df = sample_df()
    m = resumen_metricas(df)
    assert m['total_ingresos'] == 500


def test_series_temporales():
    df = sample_df()
    s = series_temporales(df)
    assert list(s['ingresos'].index)[:2] == ['Enero', 'Febrero']


def test_pca_kmeans():
    df = sample_df()
    res_pca = run_pca(df, VARIABLES_NUM, n_components=2)
    assert res_pca.components.shape[1] == 2
    res_km = run_kmeans(df, VARIABLES_NUM, k=2)
    assert set(res_km.perfil.index) == {0, 1}
