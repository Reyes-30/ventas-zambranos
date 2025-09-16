# 🚀 Guía para Desarrolladores - Sistema Zambranos

## 🎯 Bienvenido al Equipo

Esta guía te ayudará a configurar tu entorno de desarrollo y contribuir efectivamente al Sistema de Análisis de Ventas Zambranos. Nuestro objetivo es mantener un código de alta calidad, bien documentado y fácil de mantener.

---

## 📋 Requisitos Previos

### Software Necesario
- **Python 3.9+** (recomendado 3.11)
- **Git** para control de versiones
- **VS Code** (recomendado) con extensiones:
  - Python Extension Pack
  - Pylance (incluido en Python Extension Pack)
  - pytest (para testing)
  - Black Formatter
  - Flake8 (linting)

### Conocimientos Recomendados
- **Python**: Pandas, NumPy, Matplotlib/Plotly
- **Streamlit**: Framework web para aplicaciones de datos
- **Machine Learning**: Scikit-learn básico (PCA, K-Means)
- **Testing**: pytest y conceptos de testing unitario
- **Git**: Flujo de trabajo con branches y pull requests

---

## 🛠️ Configuración del Entorno

### 1. Clonar el Repositorio

```bash
git clone <repository-url>
cd Proyecto
```

### 2. Crear Entorno Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias

```bash
# Dependencias principales
pip install -r requirements.txt

# Dependencias de desarrollo (si existe)
pip install -r requirements-dev.txt

# O instalar dependencias individuales para desarrollo
pip install pytest pytest-benchmark black flake8 mypy
```

### 4. Verificar Instalación

```bash
# Ejecutar tests
pytest tests/ -v

# Ejecutar aplicación
streamlit run app.py
```

### 5. Configurar Pre-commit Hooks (Opcional pero Recomendado)

```bash
pip install pre-commit
pre-commit install
```

---

## 🏗️ Arquitectura del Proyecto

### Estructura de Directorios

```
Proyecto/
├── app.py                      # Aplicación principal Streamlit
├── requirements.txt            # Dependencias Python
├── README.md                   # Documentación básica
├── 
├── src/app/                    # Módulos de lógica de negocio
│   ├── __init__.py
│   ├── io_utils.py            # Manejo de archivos y validación
│   ├── processing.py          # Análisis y ML
│   ├── exceptions.py          # Jerarquía de excepciones
│   └── tour_interactivo.py    # Tour guiado de usuario
│
├── data/                      # Datos del sistema
│   ├── uploads/              # Archivos subidos por usuarios
│   └── outputs/              # Exportaciones generadas
│
├── tests/                     # Suite de pruebas
│   ├── test_io_utils.py
│   ├── test_processing.py
│   ├── test_ml_algorithms.py
│   ├── fixtures/             # Datos de prueba
│   └── conftest.py           # Configuración pytest
│
├── logs/                      # Archivos de log
│   └── app.log
│
└── docs/                      # Documentación
    ├── manual_usuario.md
    ├── documentacion_tecnica.md
    └── guia_desarrolladores.md
```

### Separación de Responsabilidades

#### `app.py` - Capa de Presentación
- Interfaz de usuario Streamlit
- Manejo de estado de sesión
- Coordinación entre módulos
- **NO contiene lógica de negocio**

#### `src/app/io_utils.py` - Capa de Datos
- Lectura y escritura segura de archivos
- Validación de esquemas
- Operaciones atómicas con locks

#### `src/app/processing.py` - Capa de Negocio
- Cálculos y análisis de datos
- Algoritmos de Machine Learning
- **Funciones puras sin efectos secundarios**

#### `src/app/exceptions.py` - Manejo de Errores
- Jerarquía de excepciones personalizada
- Contexto detallado para debugging

#### `src/app/tour_interactivo.py` - Experiencia de Usuario
- Tour guiado paso a paso
- Ayuda contextual por secciones

---

## 🎨 Estándares de Código

### Formateo y Style

Usamos **Black** para formateo automático con configuración estándar:

```bash
# Formatear todo el código
black src/ tests/ app.py

# Verificar formato sin cambiar
black --check src/ tests/ app.py
```

### Linting

Usamos **Flake8** para análisis de código:

```bash
# Verificar todo el código
flake8 src/ tests/ app.py

# Configuración en setup.cfg (crear si no existe)
[flake8]
max-line-length = 88
extend-ignore = E203, W503
```

### Type Hints

Usamos **type hints** en todas las funciones públicas:

```python
from typing import Optional, Dict, List, Tuple
import pandas as pd

def procesar_datos(df: pd.DataFrame, columnas: List[str]) -> Dict[str, float]:
    """Función con type hints apropiados."""
    pass
```

### Documentación

Seguimos el estilo **Google docstrings**:

```python
def ejemplo_funcion(parametro1: str, parametro2: int = 10) -> bool:
    """
    Descripción breve de la función.

    Descripción más detallada si es necesaria, explicando el contexto
    y uso de la función.

    Args:
        parametro1 (str): Descripción del primer parámetro
        parametro2 (int, optional): Descripción del segundo parámetro. Defaults to 10.

    Returns:
        bool: Descripción del valor de retorno

    Raises:
        ValueError: Cuándo y por qué se lanza esta excepción
        ProcessingError: Otra excepción posible

    Examples:
        >>> resultado = ejemplo_funcion("test", 20)
        >>> print(resultado)
        True

    Note:
        Notas adicionales importantes sobre la función.
    """
    pass
```

---

## 🧪 Testing

### Estructura de Tests

Organizamos tests por módulo:
- `test_io_utils.py` - Tests de lectura/escritura de archivos
- `test_processing.py` - Tests de lógica de negocio
- `test_ml_algorithms.py` - Tests específicos de ML
- `fixtures/` - Datos de prueba reutilizables

### Escribir Tests

#### Test Básico
```python
import pytest
import pandas as pd
from src.app.processing import resumen_metricas

def test_resumen_metricas_datos_validos():
    """Test con datos válidos completos."""
    df = pd.DataFrame({
        'Ingreso Total': [1000, 2000, 1500],
        'ISV': [150, 300, 225],
        'Utilidad Bruta': [500, 1000, 750],
        'Cantidad Vendida': [10, 20, 15],
        'Categoría': ['A', 'B', 'A'],
        'Mes': ['Enero', 'Febrero', 'Enero']
    })
    
    resultado = resumen_metricas(df)
    
    assert resultado['total_ingresos'] == 4500
    assert resultado['total_isv'] == 675
    assert resultado['categorias_unicas'] == 2
    assert resultado['meses_activos'] == 2
```

#### Test con Excepciones
```python
def test_validacion_columnas_faltantes():
    """Test que verifica manejo de columnas faltantes."""
    df_incompleto = pd.DataFrame({'Mes': ['Enero']})
    
    with pytest.raises(ValidationError) as exc_info:
        validate_schema(df_incompleto)
    
    assert "Faltan columnas requeridas" in str(exc_info.value)
```

#### Fixtures para Datos de Prueba
```python
@pytest.fixture
def sample_dataframe():
    """Fixture con DataFrame de ejemplo para tests."""
    return pd.DataFrame({
        'Mes': ['Enero', 'Febrero', 'Marzo'],
        'Categoría': ['A', 'B', 'A'],
        'Cantidad Vendida': [100, 200, 150],
        'Ingreso Total': [1000, 2000, 1500],
        'ISV': [150, 300, 225],
        'Utilidad Bruta': [500, 1000, 750]
    })

def test_con_fixture(sample_dataframe):
    """Test usando fixture de datos."""
    resultado = resumen_metricas(sample_dataframe)
    assert isinstance(resultado, dict)
```

### Ejecutar Tests

```bash
# Todos los tests
pytest

# Tests con verbose output
pytest -v

# Tests específicos
pytest tests/test_processing.py

# Tests con coverage
pytest --cov=src/app --cov-report=html

# Solo tests rápidos (excluir benchmarks)
pytest --benchmark-skip

# Solo benchmarks de performance
pytest --benchmark-only
```

---

## 🔄 Flujo de Desarrollo

### Workflow de Git

1. **Crear rama feature**
```bash
git checkout -b feature/nueva-funcionalidad
```

2. **Desarrollar y hacer commits**
```bash
git add .
git commit -m "feat: agregar nueva funcionalidad de análisis"
```

3. **Ejecutar tests localmente**
```bash
pytest tests/ -v
black --check src/ tests/ app.py
flake8 src/ tests/ app.py
```

4. **Push y crear Pull Request**
```bash
git push origin feature/nueva-funcionalidad
# Crear PR en GitHub/GitLab
```

### Convenciones de Commits

Usamos **Conventional Commits**:

```bash
feat: nueva funcionalidad
fix: corrección de bug
docs: actualización de documentación
style: cambios de formato (no afectan lógica)
refactor: refactoring de código
test: agregar o modificar tests
chore: tareas de mantenimiento
```

Ejemplos:
```bash
git commit -m "feat: agregar algoritmo de clustering jerárquico"
git commit -m "fix: corregir validación de archivos Excel"
git commit -m "docs: actualizar documentación de API"
git commit -m "test: agregar tests para funciones de ML"
```

---

## 🆕 Agregar Nuevas Funcionalidades

### 1. Nuevo Análisis de Datos

#### Paso 1: Definir Resultado
```python
# En src/app/processing.py
@dataclass
class NuevoAnalisisResult:
    """Resultado del nuevo análisis."""
    metric_principal: float
    detalles: Dict[str, any]
    interpretacion: str
```

#### Paso 2: Implementar Función
```python
def nuevo_analisis(df: pd.DataFrame, parametros: Dict) -> NuevoAnalisisResult:
    """
    Implementa nuevo tipo de análisis.

    Args:
        df: DataFrame con datos validados
        parametros: Configuración del análisis

    Returns:
        NuevoAnalisisResult: Resultado estructurado

    Raises:
        ProcessingError: Si hay problemas en el cálculo
    """
    try:
        # Lógica del análisis aquí
        resultado = calcular_nueva_metrica(df, parametros)
        
        return NuevoAnalisisResult(
            metric_principal=resultado,
            detalles=crear_detalles(df),
            interpretacion=generar_interpretacion(resultado)
        )
    except Exception as e:
        raise ProcessingError("Error en nuevo análisis", detail=str(e))
```

#### Paso 3: Escribir Tests
```python
# En tests/test_processing.py
def test_nuevo_analisis_datos_validos():
    """Test del nuevo análisis con datos válidos."""
    df = crear_dataframe_ejemplo()
    parametros = {'param1': 'valor1'}
    
    resultado = nuevo_analisis(df, parametros)
    
    assert isinstance(resultado, NuevoAnalisisResult)
    assert resultado.metric_principal > 0
    assert 'interpretacion' in resultado.interpretacion
```

#### Paso 4: Integrar en UI
```python
# En app.py, agregar nueva tab o sección
with tab_nuevo_analisis:
    st.header("🔍 Nuevo Análisis")
    
    # Controles de configuración
    param1 = st.selectbox("Parámetro 1", opciones)
    
    if st.button("Ejecutar Análisis"):
        try:
            resultado = nuevo_analisis(st.session_state.df, {'param1': param1})
            
            # Mostrar resultados
            st.metric("Métrica Principal", f"{resultado.metric_principal:.2f}")
            st.write(resultado.interpretacion)
            
        except ProcessingError as e:
            st.error(f"Error en análisis: {e}")
```

### 2. Nueva Visualización

#### Crear Función de Plot
```python
def crear_nueva_visualizacion(df: pd.DataFrame, **kwargs) -> Figure:
    """
    Crea nueva visualización personalizada.

    Args:
        df: DataFrame con datos
        **kwargs: Parámetros de configuración

    Returns:
        Figure: Figura de Plotly o Matplotlib
    """
    if kwargs.get('interactivo', True):
        # Versión Plotly
        fig = px.scatter(df, x='x_col', y='y_col', **kwargs)
        fig.update_layout(template="plotly_white")
        return fig
    else:
        # Versión Matplotlib
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(df['x_col'], df['y_col'])
        return fig
```

#### Integrar con Sistema de Exportación
```python
# En app.py
fig = crear_nueva_visualizacion(df, interactivo=mostrar_interactivas)

if isinstance(fig, go.Figure):
    st.plotly_chart(fig, use_container_width=True)
    _record_plotly(fig, "nueva_visualizacion")
else:
    st.pyplot(fig)
    _record_matplotlib(fig, "nueva_visualizacion")
```

---

## 🔧 Debugging y Troubleshooting

### Logging para Development

```python
import logging

# Configurar logging más detallado para desarrollo
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
)

logger = logging.getLogger(__name__)

def mi_funcion(datos):
    logger.debug(f"Procesando {len(datos)} registros")
    
    try:
        resultado = procesar(datos)
        logger.info(f"Procesamiento exitoso: {resultado}")
        return resultado
    except Exception as e:
        logger.error(f"Error procesando datos: {e}", exc_info=True)
        raise
```

### Debugging en Streamlit

```python
# Usar st.write para debugging rápido
st.write("DEBUG: Valor de variable", variable)

# Mostrar estructura de DataFrame
st.write("DEBUG: DataFrame info")
st.dataframe(df.head())
st.write(f"Shape: {df.shape}, Columns: {df.columns.tolist()}")

# Mostrar estado de sesión
if st.checkbox("Mostrar session_state"):
    st.write(st.session_state)
```

### Problemas Comunes

#### Error: "ModuleNotFoundError"
```bash
# Verificar que estás en el entorno virtual correcto
which python
pip list

# Reinstalar dependencias
pip install -r requirements.txt
```

#### Error: "Streamlit command not found"
```bash
# Instalar Streamlit en el entorno virtual
pip install streamlit

# Verificar instalación
streamlit --version
```

#### Error: Tests Fallan
```bash
# Ejecutar test específico con más detalle
pytest tests/test_especifico.py::test_funcion -v -s

# Verificar que todos los módulos se pueden importar
python -c "from src.app import io_utils, processing, exceptions"
```

---

## 📚 Recursos y Referencias

### Documentación Oficial
- [Streamlit Docs](https://docs.streamlit.io/)
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/)
- [Plotly Python](https://plotly.com/python/)
- [Scikit-learn](https://scikit-learn.org/stable/user_guide.html)
- [pytest Documentation](https://docs.pytest.org/)

### Herramientas de Desarrollo
- [Black Code Formatter](https://black.readthedocs.io/)
- [Flake8 Linter](https://flake8.pycqa.org/)
- [MyPy Type Checker](https://mypy.readthedocs.io/)
- [Pre-commit Hooks](https://pre-commit.com/)

### Estilo y Convenciones
- [PEP 8 - Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Conventional Commits](https://www.conventionalcommits.org/)

---

## 🤝 Proceso de Contribución

### Checklist antes de Pull Request

- [ ] **Código formateado** con Black
- [ ] **Linting limpio** con Flake8
- [ ] **Tests escritos** para nueva funcionalidad
- [ ] **Tests pasando** localmente
- [ ] **Documentación actualizada** (docstrings, README, etc.)
- [ ] **Commits descriptivos** siguiendo convenciones
- [ ] **Sin archivos sensibles** (logs, datos privados, etc.)

### Code Review

Cuando hagas review de código, considera:

#### Funcionalidad
- ¿El código hace lo que se supone?
- ¿Maneja casos edge apropiadamente?
- ¿Tiene validación de entrada adecuada?

#### Mantenibilidad
- ¿Es fácil de entender?
- ¿Está bien documentado?
- ¿Sigue los patrones establecidos?

#### Performance
- ¿Es eficiente para datasets grandes?
- ¿Podría causar memory leaks?
- ¿Usa las mejores prácticas de pandas/numpy?

#### Testing
- ¿Tiene cobertura de tests adecuada?
- ¿Los tests son claros y completos?
- ¿Incluye tests de casos edge?

---

## 🚀 Deployment

### Para Desarrollo Local
```bash
streamlit run app.py --server.headless false
```

### Para Producción con Docker
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN mkdir -p data/uploads logs

EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
```

### Variables de Entorno
```bash
# .env file para configuración
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_ENABLE_CORS=false
STREAMLIT_THEME_PRIMARY_COLOR="#1e3c72"
LOG_LEVEL=INFO
```

---

## 📞 Soporte y Contacto

### Para Problemas Técnicos
1. Revisar logs en `logs/app.log`
2. Verificar issues conocidos en documentación
3. Ejecutar suite de tests para verificar integridad
4. Contactar al equipo senior si persiste el problema

### Para Nuevas Ideas
1. Crear issue en el repositorio
2. Discutir en reuniones de equipo
3. Crear documento de diseño para features grandes
4. Implementar MVP para validar concepto

---

*¡Bienvenido al equipo! Esta guía es un documento vivo que mejora con la experiencia del equipo.*

*Última actualización: Septiembre 2025*  
*Versión: 2.0*
