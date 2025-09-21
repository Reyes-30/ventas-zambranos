"""
Genera un PDF tabular (ventas_demo_tabla.pdf) a partir de datos de ejemplo
para validar la carga de PDFs con tablas en la aplicación (pdfplumber).

Requisitos: reportlab
"""
from __future__ import annotations

import os
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer


ROOT = os.path.dirname(os.path.dirname(__file__))
SRC_CSV = os.path.join(ROOT, "datosExcel.csv")
OUT_PDF = os.path.join(os.path.dirname(__file__), "ventas_demo_tabla.pdf")


def cargar_datos(path: str, n=20) -> pd.DataFrame:
    df = pd.read_csv(path)
    df.columns = [c.strip().strip('"') for c in df.columns]
    # Limitar filas para que quepa bien
    return df.head(n)


def build_pdf(df: pd.DataFrame, path_pdf: str):
    doc = SimpleDocTemplate(path_pdf, pagesize=landscape(A4), leftMargin=24, rightMargin=24, topMargin=24, bottomMargin=24)
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph("Reporte de Ventas - Tabla de Ejemplo", styles['Title']))
    elements.append(Spacer(1, 12))

    # Preparar datos para tabla (encabezados + filas)
    data = [df.columns.tolist()] + df.values.tolist()

    table = Table(data, repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0d6efd')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 10),
        ('BOTTOMPADDING', (0,0), (-1,0), 8),
        ('GRID', (0,0), (-1,-1), 0.25, colors.grey),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.whitesmoke, colors.HexColor('#f8f9fa')]),
    ]))

    elements.append(table)
    doc.build(elements)


def main():
    os.makedirs(os.path.dirname(OUT_PDF), exist_ok=True)
    df = cargar_datos(SRC_CSV, n=25)
    build_pdf(df, OUT_PDF)
    print("PDF creado en:", OUT_PDF)


if __name__ == "__main__":
    main()
