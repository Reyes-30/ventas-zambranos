"""
Sistema de Análisis de Ventas Zambranos - Versión Simplificada
==============================================================

Aplicación web esencial para análisis de datos de ventas.
Incluye solo las funcionalidades críticas:
- Carga de datos CSV/Excel
- Métricas principales
- Gráficas básicas
- Análisis temporal y por categoría
- Machine Learning básico (PCA, K-Means)

Author: Equipo de Desarrollo Zambranos
Version: 2.0 Simple
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from pathlib import Path
import io

# Configuración de página
st.set_page_config(
    page_title="📊 Análisis de Ventas Zambranos",
    page_icon="📊",
    layout="wide"
)

# CSS básico
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 1rem;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #1e3c72;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Constantes
REQUIRED_COLUMNS = [
    "Mes", "Categoría", "Cantidad Vendida", "Ingreso Total", "ISV", "Utilidad Bruta"
]

MESES_ORDEN = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

# Funciones principales
@st.cache_data
def load_data(uploaded_file):
    """Carga datos desde archivo CSV o Excel"""
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        # Validar columnas requeridas
        missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
        if missing_cols:
            st.error(f"Faltan columnas: {missing_cols}")
            return None
            
        # Convertir a numérico
        numeric_cols = ['Cantidad Vendida', 'Ingreso Total', 'ISV', 'Utilidad Bruta']
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        return df
    except Exception as e:
        st.error(f"Error cargando archivo: {e}")
        return None

def calculate_metrics(df):
    """Calcula métricas principales"""
    return {
        "total_ingresos": df['Ingreso Total'].sum(),
        "total_isv": df['ISV'].sum(),
        "utilidad_promedio": df['Utilidad Bruta'].mean(),
        "total_ventas": df['Cantidad Vendida'].sum(),
        "categorias_unicas": df['Categoría'].nunique(),
        "meses_activos": df['Mes'].nunique()
    }

def plot_ingresos_por_mes(df):
    """Gráfica de ingresos por mes"""
    monthly_data = df.groupby('Mes')['Ingreso Total'].sum().reindex(MESES_ORDEN).fillna(0)
    
    fig = px.bar(
        x=monthly_data.index,
        y=monthly_data.values,
        title="💰 Ingresos por Mes",
        labels={'x': 'Mes', 'y': 'Ingresos Totales'}
    )
    fig.update_layout(showlegend=False)
    return fig

def plot_categoria_pie(df):
    """Gráfica de pastel por categoría"""
    cat_data = df.groupby('Categoría')['Cantidad Vendida'].sum()
    
    fig = px.pie(
        values=cat_data.values,
        names=cat_data.index,
        title="🥧 Distribución de Ventas por Categoría"
    )
    return fig

def run_pca_simple(df):
    """PCA simplificado"""
    numeric_cols = ['Cantidad Vendida', 'Ingreso Total', 'ISV', 'Utilidad Bruta']
    data = df[numeric_cols].dropna()
    
    if len(data) < 2:
        return None, None
    
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    
    pca = PCA(n_components=2)
    components = pca.fit_transform(data_scaled)
    
    return components, pca.explained_variance_ratio_

def run_kmeans_simple(df, k=3):
    """K-Means simplificado"""
    numeric_cols = ['Cantidad Vendida', 'Ingreso Total', 'ISV', 'Utilidad Bruta']
    data = df[numeric_cols].dropna()
    
    if len(data) < k:
        return None
    
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(data_scaled)
    
    return labels

# Interfaz principal
def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>📊 Sistema de Análisis de Ventas Zambranos</h1>
        <p>Versión Simplificada - Solo Funciones Esenciales</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar para carga de datos
    with st.sidebar:
        st.header("📁 Cargar Datos")
        uploaded_file = st.file_uploader(
            "Sube tu archivo CSV o Excel",
            type=['csv', 'xlsx', 'xls']
        )
        
        if uploaded_file:
            df = load_data(uploaded_file)
            if df is not None:
                st.success("✅ Datos cargados correctamente")
                st.info(f"📊 {len(df)} filas, {len(df.columns)} columnas")
        else:
            # Buscar archivos locales como fallback
            local_files = list(Path(".").glob("*.csv")) + list(Path(".").glob("*.xlsx"))
            if local_files:
                selected_file = st.selectbox("O usa archivo local:", [""] + [f.name for f in local_files])
                if selected_file:
                    df = load_data(open(selected_file, 'rb'))
                    if df is not None:
                        st.success(f"✅ Usando {selected_file}")
            df = None
    
    # Contenido principal
    if 'df' not in locals() or df is None:
        st.info("👆 Sube un archivo de datos para comenzar el análisis")
        st.markdown("""
        ### 📋 Formato requerido:
        Tu archivo debe contener estas columnas:
        - **Mes**: Enero, Febrero, etc.
        - **Categoría**: Categoría del producto
        - **Cantidad Vendida**: Unidades vendidas
        - **Ingreso Total**: Ingresos totales
        - **ISV**: Impuesto sobre ventas
        - **Utilidad Bruta**: Ganancia bruta
        """)
        return
    
    # Tabs principales
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Resumen", "📈 Temporal", "🎯 Categorías", "🤖 ML"])
    
    with tab1:
        st.header("📊 Resumen Ejecutivo")
        
        # Métricas
        metrics = calculate_metrics(df)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("💰 Ingresos Totales", f"${metrics['total_ingresos']:,.0f}")
            st.metric("🏛️ ISV Total", f"${metrics['total_isv']:,.0f}")
        with col2:
            st.metric("📈 Utilidad Promedio", f"${metrics['utilidad_promedio']:,.0f}")
            st.metric("🛒 Ventas Totales", f"{metrics['total_ventas']:,.0f}")
        with col3:
            st.metric("🏪 Categorías", metrics['categorias_unicas'])
            st.metric("📅 Meses Activos", metrics['meses_activos'])
        
        # Tabla de datos
        st.subheader("📋 Vista de Datos")
        st.dataframe(df.head(10), use_container_width=True)
    
    with tab2:
        st.header("📈 Análisis Temporal")
        
        # Gráfica de ingresos por mes
        fig_monthly = plot_ingresos_por_mes(df)
        st.plotly_chart(fig_monthly, use_container_width=True)
        
        # Estadísticas por mes
        monthly_stats = df.groupby('Mes').agg({
            'Ingreso Total': 'sum',
            'Cantidad Vendida': 'sum',
            'Utilidad Bruta': 'mean'
        }).round(2)
        
        st.subheader("📊 Estadísticas Mensuales")
        st.dataframe(monthly_stats, use_container_width=True)
    
    with tab3:
        st.header("🎯 Análisis por Categorías")
        
        # Gráfica de pastel
        fig_pie = plot_categoria_pie(df)
        st.plotly_chart(fig_pie, use_container_width=True)
        
        # Ranking de categorías
        cat_ranking = df.groupby('Categoría').agg({
            'Ingreso Total': 'sum',
            'Cantidad Vendida': 'sum',
            'Utilidad Bruta': 'sum'
        }).sort_values('Ingreso Total', ascending=False)
        
        st.subheader("🏆 Ranking de Categorías")
        st.dataframe(cat_ranking, use_container_width=True)
    
    with tab4:
        st.header("🤖 Machine Learning")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🔍 Análisis PCA")
            components, explained_var = run_pca_simple(df)
            
            if components is not None:
                fig_pca = px.scatter(
                    x=components[:, 0],
                    y=components[:, 1],
                    title=f"PCA - Varianza explicada: {explained_var.sum():.1%}"
                )
                st.plotly_chart(fig_pca, use_container_width=True)
                
                st.write(f"**Componente 1**: {explained_var[0]:.1%}")
                st.write(f"**Componente 2**: {explained_var[1]:.1%}")
            else:
                st.warning("No hay suficientes datos para PCA")
        
        with col2:
            st.subheader("🎯 Clustering K-Means")
            k_clusters = st.slider("Número de clusters", 2, 6, 3)
            
            labels = run_kmeans_simple(df, k_clusters)
            
            if labels is not None:
                # Agregar labels al dataframe para visualización
                df_viz = df.copy()
                df_viz['Cluster'] = labels[:len(df_viz)]
                
                fig_cluster = px.scatter(
                    df_viz,
                    x='Ingreso Total',
                    y='Utilidad Bruta',
                    color='Cluster',
                    title=f"Clustering K-Means (k={k_clusters})"
                )
                st.plotly_chart(fig_cluster, use_container_width=True)
                
                # Perfil por cluster
                cluster_profile = df_viz.groupby('Cluster')[['Ingreso Total', 'Utilidad Bruta', 'Cantidad Vendida']].mean().round(2)
                st.write("**Perfil por Cluster:**")
                st.dataframe(cluster_profile)
            else:
                st.warning("No hay suficientes datos para clustering")

if __name__ == "__main__":
    main()
