# 📊 Sistema de Análisis de Ventas Zambranos

**Aplicación web moderna para análisis avanzado de datos de ventas con Machine Learning integrado**

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.37+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/Tests-Passing-green.svg)](tests/)

## 🎯 ¿Qué es este sistema?

El Sistema de Análisis de Ventas Zambranos es una aplicación web completa que transforma datos de ventas en insights accionables. Desarrollado originalmente como un proyecto de Jupyter Notebook, ha evolucionado a una aplicación web profesional con:

### ✨ Características Principales

- **📊 Dashboard Ejecutivo**: Métricas clave y KPIs en tiempo real
- **📈 Análisis Temporal**: Tendencias mensuales y estacionalidad
- **🎯 Segmentación por Categorías**: Análisis detallado por productos
- **🔍 Estadísticas Avanzadas**: Correlaciones, outliers, distribuciones
- **🤖 Machine Learning**: PCA y Clustering para descubrir patrones ocultos
- **📥 Exportación Profesional**: CSV, Word, PNG, ZIP
- **🎨 UI Moderna**: Interfaz responsive con múltiples temas
- **🛡️ Seguridad**: Manejo seguro de archivos con validación
- **🎓 Tour Interactivo**: Guía paso a paso para nuevos usuarios

### 🚀 Demo en Vivo

```bash
# Ejecutar localmente
pip install -r requirements.txt
streamlit run app.py
```

La aplicación se abrirá en `http://localhost:8501`

---

## 📋 Requisitos del Sistema

### Software Requerido
- **Python 3.9+** (recomendado 3.11)
- **pip** para gestión de paquetes

### Formatos de Datos Soportados
- **CSV** (con detección automática de delimitador)
- **Excel** (.xlsx, .xls)

### Esquema de Datos Mínimo
Tu archivo debe contener estas columnas:
- `Mes` - Nombre del mes en español
- `Categoría` - Categoría del producto/servicio
- `Cantidad Vendida` - Unidades vendidas (numérico)
- `Ingreso Total` - Ingresos totales (numérico)
- `ISV` - Impuesto sobre ventas (numérico)
- `Utilidad Bruta` - Ganancia bruta (numérico)

---

## 🛠️ Instalación

### Instalación Rápida

```bash
# 1. Clonar repositorio
git clone <repository-url>
cd Proyecto

# 2. Crear entorno virtual
python -m venv venv

# 3. Activar entorno virtual
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar aplicación
streamlit run app.py
```

### Verificar Instalación

```bash
# Ejecutar tests
pytest tests/ -v

# Verificar dependencias
pip check
```

---

## 🚀 Uso Rápido

### Primera Vez - Tour Guiado
1. Abre la aplicación
2. Haz clic en **"❓ Tour Interactivo"** en el panel lateral
3. Sigue la guía paso a paso (12 pasos, ~10 minutos)

### Flujo Típico de Análisis
1. **Cargar Datos**: Sube tu archivo CSV/Excel
2. **Resumen Ejecutivo**: Revisa métricas principales
3. **Análisis Temporal**: Identifica tendencias mensuales
4. **Análisis por Categoría**: Descubre productos top
5. **Estadísticas**: Explora correlaciones y distribuciones
6. **Machine Learning**: Encuentra patrones ocultos con PCA/Clustering
7. **Exportar**: Descarga reportes y gráficas

---

## 📊 Capacidades de Análisis

### Análisis Estadístico
- Métricas descriptivas completas
- Correlaciones con heatmap
- Detección automática de outliers
- Histogramas y boxplots interactivos

### Machine Learning
- **PCA (Análisis de Componentes Principales)**
  - Reducción dimensional
  - Visualización de patrones multidimensionales
  - Análisis de varianza explicada

- **K-Means Clustering**
  - Segmentación automática de datos
  - Perfiles detallados por cluster
  - Score de silueta para calidad

### Visualizaciones
- **Gráficas Interactivas** (Plotly): Zoom, hover, filtros
- **Gráficas Estáticas** (Matplotlib): Alta resolución para reportes
- **Múltiples Temas**: Moderno, Clásico, Oscuro

---

## 📁 Estructura del Proyecto

```
Proyecto/
├── app.py                      # 🎯 Aplicación principal Streamlit
├── requirements.txt            # 📦 Dependencias Python
├── 
├── src/app/                    # 🏗️ Módulos de lógica de negocio
│   ├── io_utils.py            # 📂 Manejo seguro de archivos
│   ├── processing.py          # 🧮 Análisis y Machine Learning  
│   ├── exceptions.py          # ⚠️ Jerarquía de excepciones
│   └── tour_interactivo.py    # 🎓 Tour guiado de usuario
│
├── data/                      # 💾 Almacenamiento de datos
│   ├── uploads/              # 📤 Archivos subidos
│   └── outputs/              # 📥 Exportaciones
│
├── tests/                     # 🧪 Suite de pruebas
│   ├── test_*.py             # Tests unitarios
│   └── fixtures/             # Datos de prueba
│
├── logs/                      # 📋 Sistema de logging
│   └── app.log               # Logs de aplicación
│
└── docs/                      # 📚 Documentación completa
    ├── manual_usuario.md      # 👤 Manual para usuarios
    ├── documentacion_tecnica.md # 🔧 Docs técnicas
    └── guia_desarrolladores.md # 👨‍💻 Guía para devs
```

---

## 🧪 Testing

### Ejecutar Tests

```bash
# Todos los tests
pytest

# Tests con cobertura
pytest --cov=src/app --cov-report=html

# Tests de performance
pytest --benchmark-only

# Tests específicos
pytest tests/test_processing.py -v
```

### Tipos de Tests
- **Unitarios**: Funciones individuales
- **Integración**: Flujo completo de datos
- **Performance**: Benchmarks de velocidad
- **Validación**: Esquemas y tipos de datos

---

## 📚 Documentación Completa

| Documento | Audiencia | Contenido |
|-----------|-----------|-----------|
| [**Manual de Usuario**](docs/manual_usuario.md) | 👤 Usuarios finales | Guías paso a paso, FAQ, troubleshooting |
| [**Documentación Técnica**](docs/documentacion_tecnica.md) | 🔧 Arquitectos/DevOps | Arquitectura, APIs, algoritmos, deployment |
| [**Guía para Desarrolladores**](docs/guia_desarrolladores.md) | 👨‍💻 Programadores | Setup, estándares, contribución, testing |

### Ayuda Contextual en la App
- **🎓 Tour Interactivo**: 12 pasos guiados dentro de la aplicación
- **❓ Ayuda por Sección**: Tooltips y explicaciones contextuales
- **📋 Logs Detallados**: `logs/app.log` para debugging

---

## 🎨 Ejemplos de Uso

### Ejemplo 1: Análisis Rápido de Ventas
```python
# Los datos se cargan automáticamente via UI
# Métricas calculadas en tiempo real:
# - Ingresos totales: $1,234,567
# - Categorías top: Electrónicos (45%), Ropa (30%)
# - Mejor mes: Diciembre (+25% vs promedio)
```

### Ejemplo 2: Segmentación con ML
```python
# Clustering automático identifica 3 segmentos:
# - Segment 1: Alto volumen, baja utilidad (35% datos)
# - Segment 2: Bajo volumen, alta utilidad (25% datos)  
# - Segment 3: Volumen medio, utilidad media (40% datos)
```

### Ejemplo 3: Exportación Profesional
```python
# Un clic genera:
# - reporte_ejecutivo.docx (Word con métricas)
# - graficas_temporales.zip (PNG alta resolución)
# - datos_procesados.csv (para análisis adicional)
```

---

## 🤝 Contribución

### Proceso de Contribución
1. **Fork** el repositorio
2. **Crea rama** feature: `git checkout -b feature/nueva-funcionalidad`
3. **Desarrolla** siguiendo estándares del proyecto
4. **Escribe tests** para nueva funcionalidad
5. **Ejecuta tests**: `pytest tests/ -v`
6. **Formatea código**: `black src/ tests/ app.py`
7. **Commit** con mensaje descriptivo
8. **Push** y crea **Pull Request**

### Estándares de Código
- **Formateo**: Black (line length 88)
- **Linting**: Flake8
- **Docstrings**: Google style
- **Type Hints**: Requeridos en funciones públicas
- **Tests**: pytest con >80% coverage

---

## 🛣️ Roadmap

### Versión Actual: 2.0
- ✅ Aplicación web completa
- ✅ Machine Learning integrado
- ✅ Tour interactivo
- ✅ Documentación completa
- ✅ Suite de testing

### Próximas Versiones
- 📊 Análisis predictivo con series temporales
- 🗄️ Conexión a bases de datos
- 🌐 API REST para integraciones
- 👥 Sistema de usuarios y autenticación

---

## 📞 Soporte

### Recursos de Ayuda
- **📚 Documentación**: Revisa las guías en `/docs/`
- **🎓 Tour Interactivo**: Dentro de la aplicación
- **🐛 Issues**: Reporta bugs en GitHub Issues

### Tecnologías Principales
- **[Streamlit](https://streamlit.io/)** - Framework web para aplicaciones de datos
- **[Pandas](https://pandas.pydata.org/)** - Manipulación y análisis de datos
- **[Plotly](https://plotly.com/)** - Visualizaciones interactivas
- **[Scikit-learn](https://scikit-learn.org/)** - Machine Learning

---

<div align="center">

**🚀 ¿Listo para transformar tus datos de ventas en insights accionables?**

*Desarrollado con ❤️ para el análisis de datos moderno*

*Última actualización: Septiembre 2025 • Versión 2.0*

</div>
