"""
Sistema de Tour Interactivo para la aplicación de análisis de ventas.
Proporciona guía paso a paso para nuevos usuarios.
"""
import streamlit as st
from typing import List, Dict, Any


def crear_pasos_tour() -> List[Dict[str, Any]]:
    """
    Define todos los pasos del tour interactivo.
    
    Returns:
        List[Dict]: Lista de pasos con identificadores, títulos, descripciones y acciones.
    """
    return [
        {
            "id": "bienvenida",
            "titulo": "🎉 ¡Bienvenido al Sistema de Análisis de Ventas!",
            "descripcion": """
            Este sistema te permite analizar datos de ventas de manera profesional e interactiva.
            
            **Características principales:**
            - 📊 Análisis estadístico completo
            - 📈 Gráficas interactivas y exportables  
            - 🔍 Machine Learning (PCA y Clustering)
            - 📝 Exportación de reportes y datos
            
            Te guiaremos paso a paso para que aproveches todas las funcionalidades.
            """,
            "target": None,
            "accion": "continuar"
        },
        {
            "id": "sidebar",
            "titulo": "🔧 Panel de Control Lateral",
            "descripcion": """
            El panel lateral es tu centro de comando:
            
            **📁 Cargar Datos:**
            - Sube archivos CSV, Excel (.xlsx/.xls)
            - Autodetección de delimitadores
            - Selector de archivos recientes
            
            **⚙️ Configuración:**
            - Número de clústeres para ML
            - Tema de gráficas (moderno/clásico/oscuro)
            - Gráficas interactivas on/off
            
            **❓ Ayuda:** Siempre disponible para consultas
            """,
            "target": "sidebar",
            "accion": "highlight"
        },
        {
            "id": "carga_datos",
            "titulo": "📁 Cómo Cargar tus Datos",
            "descripcion": """
            **Paso 1:** Haz clic en "Selecciona tu archivo de datos"
            
            **Formatos soportados:**
            - CSV (con cualquier delimitador)
            - Excel (.xlsx, .xls)
            
            **Columnas requeridas:**
            - Mes, Categoría, Cantidad Vendida
            - Ingreso Total, ISV, Utilidad Bruta
            
            **💡 Tip:** Si no tienes archivo, el sistema usará datos de ejemplo automáticamente.
            
            **Archivos Recientes:** Una vez subidos, aparecen en el selector para reutilizar.
            """,
            "target": "file_uploader",
            "accion": "pulse"
        },
        {
            "id": "tab_resumen",
            "titulo": "📊 Resumen Ejecutivo - Tu Dashboard Principal",
            "descripcion": """
            La primera pestaña te muestra los KPIs más importantes:
            
            **📈 Métricas Clave:**
            - Ingresos totales y promedio mensual
            - ISV generado
            - Utilidad bruta promedio
            - Unidades vendidas y categorías activas
            
            **🔍 Vista de Datos:**
            - Filtros por mes y categoría
            - Exploración interactiva del dataset
            
            **📥 Exportaciones:**
            - Datos en CSV
            - Reporte ejecutivo en Word
            - Paquete completo en ZIP
            """,
            "target": "tab1",
            "accion": "navigate"
        },
        {
            "id": "tab_temporal",
            "titulo": "📈 Análisis Temporal - Tendencias en el Tiempo",
            "descripcion": """
            Analiza cómo evoluciona tu negocio mes a mes:
            
            **📊 Tipos de análisis:**
            - **Ingresos por mes:** Barras interactivas con valores
            - **ISV por mes:** Línea de tiempo del impuesto
            - **Comparativo:** Ingresos vs ISV en una sola vista
            
            **✨ Características:**
            - Orden cronológico de meses respetado
            - Detección automática de meses pico y valle
            - Gráficas descargables individualmente
            - **ZIP masivo** de todas las gráficas temporales
            """,
            "target": "tab2",
            "accion": "navigate"
        },
        {
            "id": "tab_categoria",
            "titulo": "🎯 Análisis por Categoría - Segmentación de Productos",
            "descripcion": """
            Descubre qué categorías impulsan tu negocio:
            
            **🥧 Distribución de Ventas:**
            - Gráfico de pastel con porcentajes
            - Estadísticas detalladas por categoría
            
            **💰 Utilidad por Categoría:**
            - Promedio vs Total (configurable)
            - Ranking visual horizontal
            
            **🏆 Ranking Completo:**
            - Top 3 destacado con medallas
            - Tabla completa ordenable
            - Múltiples métricas de comparación
            
            **📥 Exporta** cada análisis en CSV
            """,
            "target": "tab3",
            "accion": "navigate"
        },
        {
            "id": "tab_estadistico",
            "titulo": "🔍 Análisis Estadístico - Patrones Profundos",
            "descripcion": """
            Herramientas avanzadas para analistas:
            
            **📊 Histogramas:**
            - Distribución de variables seleccionables
            - Detección de normalidad y sesgo
            
            **📦 Boxplots:**
            - Identificación automática de outliers
            - Análisis de dispersión
            
            **🔗 Correlaciones:**
            - Matriz de calor interactiva
            - Top correlaciones fuertes automáticas
            
            **📈 Estadísticas Descriptivas:**
            - Resumen completo: media, mediana, desv. std.
            - Detección de datos faltantes
            - Rangos y percentiles
            """,
            "target": "tab4",
            "accion": "navigate"
        },
        {
            "id": "tab_ml",
            "titulo": "🧮 Machine Learning - Inteligencia Artificial",
            "descripcion": """
            Análisis avanzado con algoritmos de ML:
            
            **🔍 PCA (Análisis de Componentes Principales):**
            - Reducción dimensional a 2D/3D
            - Varianza explicada por componente
            - Visualización de patrones ocultos
            
            **🎯 Clustering (K-Means):**
            - Segmentación automática de datos
            - Configurable de 2-8 grupos
            - Perfil promedio por clúster (heatmap)
            - Score de calidad (silueta)
            
            **📊 Análisis Combinado:**
            - PCA + Clustering integrado
            - Recomendaciones automáticas
            - Interpretación de resultados
            """,
            "target": "tab5",
            "accion": "navigate"
        },
        {
            "id": "exportaciones",
            "titulo": "📥 Sistema de Exportaciones",
            "descripcion": """
            Múltiples formas de llevar tus análisis:
            
            **📊 Gráficas:**
            - Descarga individual (PNG de alta calidad)
            - ZIP masivo por sección
            - Compatible con presentaciones
            
            **📋 Datos:**
            - CSV de tablas procesadas
            - Datos filtrados y agregados
            - Formatos listos para Excel
            
            **📝 Reportes:**
            - Word con métricas ejecutivas
            - Formato profesional
            - Personalizable con notas
            
            **📦 Paquetes Completos:**
            - ZIP con todo incluido
            - Ideal para compartir o archivar
            """,
            "target": None,
            "accion": "info"
        },
        {
            "id": "configuracion",
            "titulo": "⚙️ Configuración Avanzada",
            "descripcion": """
            Personaliza tu experiencia:
            
            **🎨 Temas Visuales:**
            - **Moderno:** Colores vibrantes, gradientes
            - **Clásico:** Estilo tradicional de análisis
            - **Oscuro:** Ideal para presentaciones
            
            **📱 Interactividad:**
            - **ON:** Gráficas Plotly (zoom, hover, filtros)
            - **OFF:** Gráficas Matplotlib (estáticas, más rápidas)
            
            **🔢 Parámetros ML:**
            - Número de clústeres para segmentación
            - Componentes PCA (2-5 dimensiones)
            
            **💾 Persistencia:**
            - Archivos recientes automáticos
            - Configuración recordada por sesión
            """,
            "target": "sidebar",
            "accion": "highlight"
        },
        {
            "id": "consejos",
            "titulo": "💡 Consejos y Mejores Prácticas",
            "descripcion": """
            **🚀 Para mejores resultados:**
            
            **📁 Preparación de datos:**
            - Usa nombres de meses en español
            - Evita celdas vacías en columnas clave
            - Formato numérico consistente
            
            **📊 Análisis efectivo:**
            - Comienza con Resumen Ejecutivo
            - Analiza tendencias temporales
            - Segmenta por categorías
            - Usa ML para patrones ocultos
            
            **📥 Exportaciones profesionales:**
            - Descarga gráficas en alta resolución
            - Usa reportes Word para ejecutivos
            - ZIP completo para archivar análisis
            
            **🔧 Rendimiento:**
            - Archivos <10MB para fluidez
            - Gráficas estáticas si hay lag
            - Usa filtros para datasets grandes
            """,
            "target": None,
            "accion": "info"
        },
        {
            "id": "finalizacion",
            "titulo": "🎯 ¡Listo para Analizar!",
            "descripcion": """
            **🎉 ¡Felicitaciones!** Ya conoces todas las funcionalidades.
            
            **🔄 Flujo recomendado:**
            1. **Carga** tus datos (CSV/Excel)
            2. **Revisa** métricas en Resumen Ejecutivo
            3. **Explora** tendencias temporales
            4. **Analiza** categorías de productos
            5. **Profundiza** con estadísticas
            6. **Descubre** patrones con Machine Learning
            7. **Exporta** resultados profesionales
            
            **❓ ¿Necesitas ayuda?**
            - Botón "❓ Tour" siempre disponible
            - Tooltips en cada control
            - Mensajes de error explicativos
            
            **🚀 ¡Comienza tu análisis ahora!**
            """,
            "target": None,
            "accion": "finish"
        }
    ]


def mostrar_tour_interactivo():
    """
    Implementa el tour interactivo paso a paso usando session state.
    """
    # Inicializar estado del tour
    if "tour_activo" not in st.session_state:
        st.session_state["tour_activo"] = False
    if "tour_paso" not in st.session_state:
        st.session_state["tour_paso"] = 0
    
    pasos = crear_pasos_tour()
    
    # Botón para iniciar/reiniciar tour
    if st.sidebar.button("❓ **Tour Interactivo**", help="Guía paso a paso por todas las funcionalidades"):
        st.session_state["tour_activo"] = True
        st.session_state["tour_paso"] = 0
    
    # Estilos específicos del tour (evitar saltos de línea y mejorar botones)
    st.markdown(
        """
        <style>
        /* Contenedor del tour para aplicar estilos locales */
        .tour-nav .stButton > button {
            width: 100%;
            min-height: 40px;
            white-space: nowrap; /* evita que el texto se corte en vertical */
            font-weight: 600;
            border-radius: 8px;
        }
        /* Botón central (Salir) en rojo para diferenciarlo */
        .tour-nav [data-testid="column"]:nth-child(2) .stButton > button {
            background: linear-gradient(90deg, #dc3545 0%, #c82333 100%) !important;
            color: #fff !important;
            border: none !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Mostrar tour si está activo
    if st.session_state["tour_activo"] and st.session_state["tour_paso"] < len(pasos):
        paso_actual = pasos[st.session_state["tour_paso"]]
        
        # Modal/contenedor para el paso actual
        with st.container():
            st.markdown("---")
            st.markdown(f"### {paso_actual['titulo']}")
            st.markdown(f"**Paso {st.session_state['tour_paso'] + 1} de {len(pasos)}**")
            
            # Barra de progreso
            progreso = (st.session_state["tour_paso"] + 1) / len(pasos)
            st.progress(progreso)
            
            # Contenido del paso
            st.markdown(paso_actual["descripcion"])
            
            # Controles de navegación (dentro de contenedor para estilos)
            st.markdown('<div class="tour-nav">', unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 1, 1])

            with col1:
                if st.button("⬅️ Anterior", disabled=(st.session_state["tour_paso"] == 0), use_container_width=True):
                    st.session_state["tour_paso"] -= 1
                    st.rerun()

            with col2:
                if st.button("✖ Salir", use_container_width=True):
                    st.session_state["tour_activo"] = False
                    st.rerun()

            with col3:
                if st.session_state["tour_paso"] < len(pasos) - 1:
                    if st.button("Siguiente ➡️", use_container_width=True):
                        st.session_state["tour_paso"] += 1
                        st.rerun()
                else:
                    if st.button("✅ Finalizar", use_container_width=True):
                        st.session_state["tour_activo"] = False
                        st.success("🎉 ¡Tour completado! Ya puedes usar todas las funcionalidades.")
                        st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown("---")


def mostrar_ayuda_contextual(seccion: str) -> None:
    """
    Muestra ayuda específica según la sección actual.
    
    Args:
        seccion: Identificador de la sección actual ('resumen', 'temporal', etc.)
    """
    ayuda_seccion = {
        "resumen": """
        ### 📊 Ayuda - Resumen Ejecutivo
        - **Métricas:** KPIs calculados automáticamente de tus datos
        - **Filtros:** Usa los selectores para explorar subconjuntos
        - **Exportar:** Botones de descarga para datos y reportes
        """,
        "temporal": """
        ### 📈 Ayuda - Análisis Temporal
        - **Radio buttons:** Selecciona el tipo de análisis
        - **Interactivo:** Hover sobre gráficas para detalles
        - **Orden:** Meses siempre en secuencia cronológica
        - **ZIP:** Descarga todas las gráficas de una vez
        """,
        "categoria": """
        ### 🎯 Ayuda - Análisis por Categoría
        - **Pie chart:** Distribución porcentual de ventas
        - **Métricas:** Cambia entre promedio y total
        - **Ranking:** Top 3 visual + tabla completa
        - **CSV:** Exporta cada tabla individualmente
        """,
        "estadistico": """
        ### 🔍 Ayuda - Análisis Estadístico
        - **Multiselect:** Elige variables para histogramas/boxplots
        - **Correlaciones:** Rojo=negativa, Azul=positiva
        - **Outliers:** Puntos fuera de Q1-1.5*IQR, Q3+1.5*IQR
        - **Missing:** Datos faltantes mostrados por variable
        """,
        "ml": """
        ### 🧮 Ayuda - Machine Learning
        - **PCA:** Reduce dimensiones para visualizar patrones
        - **Clustering:** Agrupa datos similares automáticamente
        - **K:** Número de grupos (slider en sidebar)
        - **Silueta >0.5:** Clusters bien definidos
        """
    }
    
    if seccion in ayuda_seccion:
        with st.expander("❓ **Ayuda de esta sección**"):
            st.markdown(ayuda_seccion[seccion])


def tooltip_personalizado(texto: str, ayuda: str) -> str:
    """
    Crea tooltips personalizados para elementos de la UI.
    
    Args:
        texto: Texto principal a mostrar
        ayuda: Texto del tooltip
        
    Returns:
        str: HTML con tooltip personalizado
    """
    return f"""
    <div title="{ayuda}" style="cursor: help; border-bottom: 1px dotted #999;">
        {texto}
    </div>
    """
