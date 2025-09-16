import io
import pandas as pd
from src.app.io_utils import read_dataframe, validate_schema, coerce_numeric, REQUIRED_COLUMNS
import pytest


def test_read_csv_bytes():
    data = b"Mes,Categor\xc3\xada,Cantidad Vendida,Ingreso Total,ISV,Utilidad Bruta\nEnero,A,1,10,2,3\n"
    df = read_dataframe(data)
    assert not df.empty


def test_validate_schema_ok():
    df = pd.DataFrame({
        'Mes': ['Enero'], 'Categoría': ['A'], 'Cantidad Vendida': [1],
        'Ingreso Total': [10], 'ISV': [2], 'Utilidad Bruta': [3]
    })
    validate_schema(df)  # no exception


def test_coerce_numeric():
    df = pd.DataFrame({'x': ['1', 'a', '3']})
    out = coerce_numeric(df, ['x'])
    assert out['x'].isna().sum() == 1
