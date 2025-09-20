import io
import pandas as pd
import pytest

from src.app.io_utils import read_dataframe, list_sheets, validate_schema, REQUIRED_COLUMNS


def make_min_df():
    return pd.DataFrame({
        'Mes': ['Enero', 'Febrero'],
        'Categoría': ['A', 'B'],
        'Cantidad Vendida': [1, 2],
        'Ingreso Total': [10.0, 20.0],
        'ISV': [1.5, 3.0],
        'Utilidad Bruta': [3.0, 6.0],
    })


def test_read_csv_semicolon_auto_delimiter():
    # CSV con ; como separador
    content = (
        "Mes;Categoría;Cantidad Vendida;Ingreso Total;ISV;Utilidad Bruta\n"
        "Enero;A;1;10;2;3\n"
        "Febrero;B;2;20;3;6\n"
    ).encode("utf-8")
    df = read_dataframe(content)
    validate_schema(df)
    assert len(df) == 2


def test_read_csv_tab():
    content = (
        "Mes\tCategoría\tCantidad Vendida\tIngreso Total\tISV\tUtilidad Bruta\n"
        "Enero\tA\t1\t10\t2\t3\n"
    ).encode("utf-8")
    # Forzamos separador tab para evitar falsos negativos de Sniffer
    df = read_dataframe(content, delimiter="\t")
    validate_schema(df)
    assert df.iloc[0]['Mes'] == 'Enero'


def test_read_excel_xlsx_bytes():
    df_in = make_min_df()
    bio = io.BytesIO()
    with pd.ExcelWriter(bio, engine='openpyxl') as writer:
        df_in.to_excel(writer, index=False, sheet_name='Data')
    content = bio.getvalue()

    df = read_dataframe(content, sheet_name='Data', file_name='sample.xlsx')
    validate_schema(df)
    assert set(REQUIRED_COLUMNS).issuperset(df.columns)


def test_read_excel_xlsm_bytes():
    # Usamos el mismo contenido; openpyxl puede leerlo aunque la extensión sea xlsm
    df_in = make_min_df()
    bio = io.BytesIO()
    with pd.ExcelWriter(bio, engine='openpyxl') as writer:
        df_in.to_excel(writer, index=False, sheet_name='Hoja1')
    content = bio.getvalue()

    df = read_dataframe(content, sheet_name='Hoja1', file_name='macro.xlsm')
    validate_schema(df)
    assert len(df) == 2


def test_read_excel_multi_sheet_selection_and_list_sheets():
    df1 = make_min_df()
    df2 = df1.copy()
    df2['Mes'] = ['Marzo', 'Abril']
    bio = io.BytesIO()
    with pd.ExcelWriter(bio, engine='openpyxl') as writer:
        df1.to_excel(writer, index=False, sheet_name='Datos')
        df2.to_excel(writer, index=False, sheet_name='Otra')
    content = bio.getvalue()

    # Ver hojas
    sheets = list_sheets(content, file_name='multi.xlsx')
    assert set(['Datos', 'Otra']).issubset(set(sheets))

    # Leer una hoja específica
    df = read_dataframe(content, sheet_name='Otra', file_name='multi.xlsx')
    validate_schema(df)
    assert list(df['Mes']) == ['Marzo', 'Abril']


@pytest.mark.skip(reason="Se requiere un PDF con tablas para prueba integral; validar manualmente con archivos reales.")
def test_read_pdf_tables_manual():
    # Este test se deja como recordatorio: proveer un PDF con tablas simples
    # y verificar que read_dataframe lo convierta a DataFrame.
    pass
