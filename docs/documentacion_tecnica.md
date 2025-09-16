# 📋 Documentación Técnica - Sistema de Análisis de Ventas Zambranos

## 🏗️ Arquitectura del Sistema

### Visión General

El Sistema de Análisis de Ventas Zambranos es una aplicación web moderna construida con **Streamlit** que proporciona capacidades avanzadas de análisis de datos, machine learning y visualización. La arquitectura sigue un patrón modular que separa responsabilidades y facilita el mantenimiento.

```
Sistema de Análisis Zambranos/
├── app.py                    # Aplicación principal Streamlit
├── src/app/                  # Módulos de negocio
│   ├── __init__.py
│   ├── io_utils.py          # Manejo de archivos y validación
│   ├── processing.py        # Lógica de análisis y ML
│   ├── exceptions.py        # Jerarquía de excepciones
│   └── tour_interactivo.py  # Sistema de tour guiado
├── data/uploads/            # Almacenamiento seguro de archivos
├── logs/                    # Sistema de logging
├── tests/                   # Suite de pruebas
└── docs/                   # Documentación
```

### Principios de Diseño

1. **Separación de Responsabilidades**: Cada módulo tiene una función específica
2. **Seguridad Primero**: Validación exhaustiva y manejo seguro de archivos
3. **Experiencia de Usuario**: Tour interactivo y ayuda contextual
4. **Escalabilidad**: Arquitectura modular para futuras extensiones
5. **Mantenibilidad**: Código bien documentado y probado

---

## 🔧 Stack Tecnológico

### Core Framework
- **Streamlit 1.37+**: Framework web para aplicaciones de datos
- **Python 3.8+**: Lenguaje base del sistema

### Procesamiento de Datos
- **pandas 2.0+**: Manipulación y análisis de datos
- **numpy 1.24+**: Operaciones numéricas y arrays
- **scikit-learn 1.3+**: Algoritmos de machine learning

### Visualización
- **plotly 5.15+**: Gráficas interactivas y dinámicas
- **matplotlib 3.7+**: Gráficas estáticas de alta calidad
- **seaborn 0.12+**: Visualizaciones estadísticas avanzadas
- **kaleido 0.2+**: Exportación de gráficas Plotly a PNG

### Documentación y Reportes
- **python-docx 0.8+**: Generación de documentos Word
- **streamlit-guided-tour**: Tour interactivo de usuario

### Desarrollo y Testing
- **pytest 7.4+**: Framework de pruebas unitarias
- **pytest-benchmark**: Pruebas de rendimiento
- **filelock 3.12+**: Sincronización de archivos

### Logging y Monitoreo
- **logging (built-in)**: Sistema de logs estructurado
- **hashlib (built-in)**: Hashing SHA-256 para archivos

---

## 📊 Modelo de Datos

### Esquema de Entrada

El sistema espera datos tabulares con el siguiente esquema mínimo:

```python
REQUIRED_COLUMNS = [
    'Mes',              # str: Nombre del mes en español
    'Categoría',        # str: Categoría del producto
    'Cantidad Vendida', # int/float: Unidades vendidas
    'Ingreso Total',    # float: Ingresos totales
    'ISV',              # float: Impuesto sobre ventas
    'Utilidad Bruta'    # float: Ganancia bruta
]

OPTIONAL_COLUMNS = [
    'Precio Unitario',  # float: Precio por unidad
    'Costo Unitario',   # float: Costo por unidad
    'Costo Total',      # float: Costo total
    'Ingreso Neto'      # float: Ingreso después de costos
]
```

### Transformaciones de Datos

#### 1. Validación y Coerción
```python
def validate_schema(df: pd.DataFrame) -> tuple[bool, list]:
    """Valida esquema mínimo de datos"""
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    return len(missing) == 0, missing

def coerce_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Convierte columnas a tipos numéricos"""
    numeric_cols = ['Cantidad Vendida', 'Ingreso Total', 'ISV', 'Utilidad Bruta']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df
```

#### 2. Normalización Temporal
```python
MONTH_ORDER = [
    'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
    'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
]

def normalize_months(df: pd.DataFrame) -> pd.DataFrame:
    """Ordena meses cronológicamente"""
    df['Mes'] = pd.Categorical(df['Mes'], categories=MONTH_ORDER, ordered=True)
    return df.sort_values('Mes')
```

---

## 🏗️ Componentes del Sistema

### 1. `app.py` - Aplicación Principal

#### Responsabilidades
- Interfaz de usuario Streamlit
- Coordinación entre módulos
- Gestión de estado de sesión
- Control de flujo de la aplicación

#### Estructura Principal
```python
def main():
    """Función principal de la aplicación"""
    configure_page()           # Configuración de página
    load_custom_css()         # Estilos personalizados
    create_sidebar()          # Panel de control lateral
    
    if 'df' in st.session_state:
        show_main_tabs()      # Tabs de análisis
    else:
        show_upload_interface()  # Interfaz de carga
```

#### Gestión de Estado
```python
# Variables de sesión críticas
st.session_state = {
    'df': pd.DataFrame,           # Datos principales
    'theme': str,                 # Tema visual
    'interactive_plots': bool,    # Modo de gráficas
    'saved_plots': dict,         # Cache de gráficas
    'tour_progress': dict,       # Progreso del tour
    'file_hash': str            # Hash del archivo actual
}
```

### 2. `src/app/io_utils.py` - Gestión de Archivos

#### Funciones Principales

```python
def read_dataframe(file_obj, filename: str, delimiter: str = 'auto') -> pd.DataFrame:
    """Lee archivo CSV/Excel con detección automática de formato"""
    
def save_upload_safely(uploaded_file) -> tuple[str, str]:
    """Guarda archivo de forma segura con hash único"""
    
def list_recent_files() -> list[tuple[str, str, datetime]]:
    """Lista archivos recientes con metadatos"""
    
def generate_file_hash(content: bytes) -> str:
    """Genera hash SHA-256 para identificación única"""
```

#### Seguridad de Archivos
- **Atomic Writes**: Escritura atómica para evitar corrupción
- **File Locking**: `filelock` para acceso concurrente seguro
- **Hash-based Naming**: Evita colisiones y sobreescritura accidental
- **Validation**: Verificación de formato y tamaño

### 3. `src/app/processing.py` - Lógica de Análisis

#### Métricas Estadísticas
```python
@dataclass
class MetricasResumen:
    """Estructura de métricas principales"""
    ingresos_totales: float
    isv_total: float
    utilidad_promedio: float
    unidades_vendidas: int
    num_categorias: int
    meses_activos: int

def resumen_metricas(df: pd.DataFrame) -> MetricasResumen:
    """Calcula métricas ejecutivas principales"""
```

#### Machine Learning
```python
@dataclass
class PCAResult:
    """Resultado del análisis PCA"""
    components: np.ndarray
    explained_variance_ratio: np.ndarray
    transformed_data: np.ndarray

@dataclass
class ClusterResult:
    """Resultado del clustering K-Means"""
    labels: np.ndarray
    centers: np.ndarray
    silhouette_score: float
    cluster_profiles: pd.DataFrame

def run_pca(df: pd.DataFrame, n_components: int = 2) -> PCAResult:
    """Ejecuta análisis de componentes principales"""
    
def run_kmeans(df: pd.DataFrame, n_clusters: int = 3) -> ClusterResult:
    """Ejecuta clustering K-Means"""
```

### 4. `src/app/exceptions.py` - Manejo de Errores

#### Jerarquía de Excepciones
```python
class ZambranosAnalysisError(Exception):
    """Excepción base del sistema"""

class DataValidationError(ZambranosAnalysisError):
    """Errores de validación de datos"""

class FileProcessingError(ZambranosAnalysisError):
    """Errores de procesamiento de archivos"""

class AnalysisError(ZambranosAnalysisError):
    """Errores durante análisis estadístico"""

class MLError(ZambranosAnalysisError):
    """Errores en algoritmos de ML"""
```

### 5. `src/app/tour_interactivo.py` - Sistema de Tour

#### Arquitectura del Tour
```python
@dataclass
class PasoTour:
    """Definición de un paso del tour"""
    titulo: str
    contenido: str
    posicion: str  # sidebar, main, tab
    tab_objetivo: str = None
    accion_requerida: str = None

def crear_pasos_tour() -> list[PasoTour]:
    """Define secuencia completa del tour (12 pasos)"""
    
def mostrar_tour_interactivo():
    """Ejecuta tour guiado con navegación"""
```

---

## 🎨 Sistema de UI/UX

### Themes y Estilos

#### CSS Personalizado
```css
/* Tema Moderno */
.metric-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 15px;
    padding: 20px;
    color: white;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
}

/* Tema Clásico */
.classic-theme {
    --primary-color: #2E86AB;
    --secondary-color: #A23B72;
    --background-color: #F18F01;
}

/* Tema Oscuro */
.dark-theme {
    --bg-color: #1E1E1E;
    --text-color: #FFFFFF;
    --accent-color: #FF6B6B;
}
```

#### Sistema de Componentes
```python
def create_metric_card(title: str, value: str, delta: str = None):
    """Crea tarjeta de métrica estilizada"""
    
def create_styled_dataframe(df: pd.DataFrame, height: int = 400):
    """DataFrame con estilos personalizados"""
    
def show_success_message(message: str):
    """Mensaje de éxito con íconos"""
```

### Responsive Design

El sistema adapta automáticamente el layout según el dispositivo:
- **Desktop**: Layout completo con sidebar
- **Tablet**: Sidebar colapsable
- **Mobile**: Stack vertical de componentes

---

## 🔍 Algoritmos de Análisis

### Análisis Estadístico

#### Correlaciones
```python
def calcular_correlaciones(df: pd.DataFrame) -> tuple[pd.DataFrame, list]:
    """
    Calcula matriz de correlación y identifica correlaciones fuertes
    
    Returns:
        tuple: (correlation_matrix, strong_correlations)
    """
    numeric_df = df.select_dtypes(include=[np.number])
    correlation_matrix = numeric_df.corr()
    
    # Identificar correlaciones fuertes
    strong_corr = []
    for i in range(len(correlation_matrix.columns)):
        for j in range(i+1, len(correlation_matrix.columns)):
            corr_value = correlation_matrix.iloc[i, j]
            if abs(corr_value) > 0.7:  # Umbral de correlación fuerte
                strong_corr.append({
                    'var1': correlation_matrix.columns[i],
                    'var2': correlation_matrix.columns[j],
                    'correlation': corr_value
                })
    
    return correlation_matrix, strong_corr
```

#### Detección de Outliers
```python
def detectar_outliers(df: pd.DataFrame, column: str) -> dict:
    """
    Detecta outliers usando método IQR
    
    Returns:
        dict: Información detallada de outliers
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    
    return {
        'count': len(outliers),
        'percentage': (len(outliers) / len(df)) * 100,
        'bounds': (lower_bound, upper_bound),
        'outlier_values': outliers[column].tolist()
    }
```

### Machine Learning

#### PCA - Análisis de Componentes Principales
```python
def run_pca(df: pd.DataFrame, n_components: int = 2) -> PCAResult:
    """
    Ejecuta PCA para reducción dimensional
    
    Algorithm:
    1. Standardize data (Z-score normalization)
    2. Compute covariance matrix
    3. Find eigenvalues and eigenvectors
    4. Project data onto principal components
    """
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    
    # Preparación de datos
    numeric_df = df.select_dtypes(include=[np.number])
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numeric_df)
    
    # PCA
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(scaled_data)
    
    return PCAResult(
        components=pca.components_,
        explained_variance_ratio=pca.explained_variance_ratio_,
        transformed_data=transformed_data
    )
```

#### K-Means Clustering
```python
def run_kmeans(df: pd.DataFrame, n_clusters: int = 3) -> ClusterResult:
    """
    Ejecuta clustering K-Means
    
    Algorithm:
    1. Initialize k centroids randomly
    2. Assign points to nearest centroid
    3. Update centroids to cluster means
    4. Repeat until convergence
    """
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score
    from sklearn.preprocessing import StandardScaler
    
    # Preparación
    numeric_df = df.select_dtypes(include=[np.number])
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numeric_df)
    
    # K-Means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(scaled_data)
    
    # Métricas de calidad
    silhouette_avg = silhouette_score(scaled_data, labels)
    
    # Perfil de clusters
    cluster_profiles = calculate_cluster_profiles(df, labels)
    
    return ClusterResult(
        labels=labels,
        centers=kmeans.cluster_centers_,
        silhouette_score=silhouette_avg,
        cluster_profiles=cluster_profiles
    )
```

---

## 📊 Visualización y Gráficas

### Sistema Dual de Visualización

#### Plotly (Interactivo)
```python
def create_interactive_plot(df: pd.DataFrame, plot_type: str, **kwargs):
    """Crea gráficas interactivas con Plotly"""
    
    if plot_type == 'bar':
        fig = px.bar(df, **kwargs)
        fig.update_layout(
            template="plotly_white",
            hovermode="x unified",
            showlegend=True
        )
    elif plot_type == 'line':
        fig = px.line(df, **kwargs)
        fig.update_traces(mode='lines+markers')
    
    return fig
```

#### Matplotlib (Estático)
```python
def create_static_plot(df: pd.DataFrame, plot_type: str, **kwargs):
    """Crea gráficas estáticas con Matplotlib"""
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    if plot_type == 'bar':
        bars = ax.bar(df.index, df.values, **kwargs)
        # Añadir valores en barras
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:,.0f}', ha='center', va='bottom')
    
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    return fig
```

### Sistema de Exportación

#### PNG de Alta Resolución
```python
def export_plot_png(fig, filename: str, dpi: int = 300):
    """Exporta gráfica como PNG de alta calidad"""
    
    if hasattr(fig, 'write_image'):  # Plotly
        fig.write_image(filename, width=1200, height=800, scale=2)
    else:  # Matplotlib
        fig.savefig(filename, dpi=dpi, bbox_inches='tight', 
                   facecolor='white', edgecolor='none')
```

---

## 🔐 Seguridad y Validación

### Validación de Archivos

#### Validación de Formato
```python
def validate_file_format(filename: str) -> bool:
    """Valida formatos de archivo permitidos"""
    allowed_extensions = {'.csv', '.xlsx', '.xls'}
    return Path(filename).suffix.lower() in allowed_extensions

def validate_file_size(file_obj, max_size_mb: int = 50) -> bool:
    """Valida tamaño máximo de archivo"""
    file_obj.seek(0, 2)  # Ir al final
    size = file_obj.tell()
    file_obj.seek(0)     # Volver al inicio
    return size <= max_size_mb * 1024 * 1024
```

#### Sanitización de Datos
```python
def sanitize_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia y sanitiza DataFrame"""
    
    # Remover filas completamente vacías
    df = df.dropna(how='all')
    
    # Limpiar espacios en strings
    string_cols = df.select_dtypes(include=['object']).columns
    df[string_cols] = df[string_cols].apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    
    # Validar rangos numéricos
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        # Remover valores infinitos
        df[col] = df[col].replace([np.inf, -np.inf], np.nan)
        # Validar rangos razonables para datos de ventas
        if 'Precio' in col or 'Costo' in col:
            df[col] = df[col].where(df[col] >= 0)  # No negativos
    
    return df
```

### Logging y Monitoreo

#### Sistema de Logs Estructurado
```python
import logging
from datetime import datetime

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def log_user_action(action: str, details: dict = None):
    """Registra acciones del usuario"""
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'action': action,
        'details': details or {},
        'session_id': st.session_state.get('session_id', 'unknown')
    }
    logger.info(f"USER_ACTION: {log_entry}")

def log_error(error: Exception, context: str = ""):
    """Registra errores con contexto"""
    logger.error(f"ERROR in {context}: {type(error).__name__}: {str(error)}")
```

---

## 🧪 Testing y Quality Assurance

### Estructura de Tests

```
tests/
├── test_io_utils.py          # Tests de manejo de archivos
├── test_processing.py        # Tests de análisis
├── test_ml_algorithms.py     # Tests de ML
├── test_visualizations.py    # Tests de gráficas
├── fixtures/                 # Datos de prueba
│   ├── sample_data.csv
│   └── invalid_data.csv
└── conftest.py              # Configuración pytest
```

### Tests Unitarios

#### Test de Validación de Datos
```python
import pytest
import pandas as pd
from src.app.io_utils import validate_schema, coerce_numeric_columns

def test_validate_schema_valid_data():
    """Test validación con datos válidos"""
    df = pd.DataFrame({
        'Mes': ['Enero', 'Febrero'],
        'Categoría': ['A', 'B'],
        'Cantidad Vendida': [100, 200],
        'Ingreso Total': [1000.0, 2000.0],
        'ISV': [150.0, 300.0],
        'Utilidad Bruta': [500.0, 1000.0]
    })
    
    is_valid, missing = validate_schema(df)
    assert is_valid == True
    assert missing == []

def test_validate_schema_missing_columns():
    """Test validación con columnas faltantes"""
    df = pd.DataFrame({
        'Mes': ['Enero'],
        'Categoría': ['A']
        # Faltan columnas requeridas
    })
    
    is_valid, missing = validate_schema(df)
    assert is_valid == False
    assert 'Cantidad Vendida' in missing
```

#### Test de Machine Learning
```python
def test_pca_basic_functionality():
    """Test básico del algoritmo PCA"""
    df = create_sample_numeric_data()
    
    result = run_pca(df, n_components=2)
    
    assert result.transformed_data.shape[1] == 2
    assert len(result.explained_variance_ratio) == 2
    assert 0 <= result.explained_variance_ratio.sum() <= 1

def test_kmeans_clustering():
    """Test básico del clustering K-Means"""
    df = create_sample_numeric_data()
    
    result = run_kmeans(df, n_clusters=3)
    
    assert len(set(result.labels)) <= 3  # Máximo 3 clusters
    assert -1 <= result.silhouette_score <= 1  # Rango válido
    assert result.cluster_profiles.shape[0] == 3  # Un perfil por cluster
```

### Tests de Performance

```python
import pytest_benchmark

def test_processing_performance(benchmark):
    """Test de rendimiento para procesamiento de datos"""
    df = create_large_dataset(10000)  # 10k filas
    
    result = benchmark(resumen_metricas, df)
    
    assert result.ingresos_totales > 0
    # Benchmark se registra automáticamente

def test_pca_performance(benchmark):
    """Test de rendimiento para PCA"""
    df = create_large_numeric_dataset(5000)
    
    result = benchmark(run_pca, df, n_components=3)
    
    assert result.transformed_data.shape[0] == 5000
```

### Continuous Integration

#### GitHub Actions (Ejemplo)
```yaml
name: CI/CD Pipeline

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest pytest-benchmark
    
    - name: Run tests
      run: |
        pytest tests/ -v --benchmark-skip
    
    - name: Run performance tests
      run: |
        pytest tests/ --benchmark-only --benchmark-json=benchmark.json
```

---

## 🚀 Deployment y DevOps

### Configuración de Producción

#### Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copiar requerimientos e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Crear directorios necesarios
RUN mkdir -p data/uploads logs

# Exponer puerto
EXPOSE 8501

# Comando de inicio
CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
```

#### docker-compose.yml
```yaml
version: '3.8'

services:
  zambranos-app:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
    environment:
      - STREAMLIT_SERVER_HEADLESS=true
      - STREAMLIT_SERVER_ENABLE_CORS=false
    restart: unless-stopped

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - zambranos-app
```

### Monitoreo en Producción

#### Health Checks
```python
def health_check():
    """Endpoint de health check"""
    checks = {
        'database': check_data_directory(),
        'logging': check_log_system(),
        'memory': check_memory_usage(),
        'disk': check_disk_space()
    }
    
    all_healthy = all(checks.values())
    
    return {
        'status': 'healthy' if all_healthy else 'unhealthy',
        'checks': checks,
        'timestamp': datetime.now().isoformat()
    }
```

#### Metrics Collection
```python
def collect_usage_metrics():
    """Recolecta métricas de uso"""
    return {
        'active_sessions': count_active_sessions(),
        'files_processed_today': count_daily_uploads(),
        'avg_processing_time': get_avg_processing_time(),
        'memory_usage': get_memory_usage(),
        'error_rate': calculate_error_rate()
    }
```

---

## 🔧 Mantenimiento y Extensibilidad

### Patrones de Extensión

#### Añadir Nuevos Análisis
```python
# 1. Definir dataclass para resultado
@dataclass
class NuevoAnalisisResult:
    resultado_principal: float
    datos_adicionales: dict

# 2. Implementar función de análisis
def nuevo_analisis(df: pd.DataFrame, parametros: dict) -> NuevoAnalisisResult:
    """Nueva funcionalidad de análisis"""
    # Lógica de análisis aquí
    pass

# 3. Añadir al pipeline principal
def run_all_analyses(df: pd.DataFrame):
    """Pipeline completo de análisis"""
    return {
        'metricas': resumen_metricas(df),
        'pca': run_pca(df),
        'clustering': run_kmeans(df),
        'nuevo_analisis': nuevo_analisis(df, {})  # ← Nuevo análisis
    }
```

#### Nuevos Tipos de Visualización
```python
def register_new_plot_type(plot_type: str, render_function):
    """Registra nuevo tipo de gráfica"""
    PLOT_RENDERERS[plot_type] = render_function

def create_custom_visualization(df: pd.DataFrame, viz_type: str, **kwargs):
    """Factory para visualizaciones personalizadas"""
    if viz_type in PLOT_RENDERERS:
        return PLOT_RENDERERS[viz_type](df, **kwargs)
    else:
        raise ValueError(f"Tipo de visualización no soportado: {viz_type}")
```

### Database Integration (Futuro)

#### Estructura para Base de Datos
```python
# models.py
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AnalysisSession(Base):
    __tablename__ = 'analysis_sessions'
    
    id = Column(Integer, primary_key=True)
    session_id = Column(String(64), unique=True)
    file_hash = Column(String(64))
    created_at = Column(DateTime)
    last_accessed = Column(DateTime)

class ProcessedData(Base):
    __tablename__ = 'processed_data'
    
    id = Column(Integer, primary_key=True)
    session_id = Column(String(64))
    analysis_type = Column(String(32))
    result_data = Column(String)  # JSON serialized
    created_at = Column(DateTime)
```

### API Integration (Futuro)

#### REST API Endpoints
```python
from fastapi import FastAPI, UploadFile
from pydantic import BaseModel

app = FastAPI()

class AnalysisRequest(BaseModel):
    analysis_type: str
    parameters: dict

@app.post("/api/upload")
async def upload_data(file: UploadFile):
    """Endpoint para subir datos"""
    pass

@app.post("/api/analyze")
async def run_analysis(request: AnalysisRequest):
    """Endpoint para ejecutar análisis"""
    pass

@app.get("/api/results/{session_id}")
async def get_results(session_id: str):
    """Endpoint para obtener resultados"""
    pass
```

---

## 📚 Referencias y Recursos

### Documentación Externa
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/user_guide.html)
- [Plotly Python Documentation](https://plotly.com/python/)

### Libros Recomendados
- "Python for Data Analysis" by Wes McKinney
- "Hands-On Machine Learning" by Aurélien Géron
- "Streamlit for Data Science" by Tyler Richards

### Papers y Artículos
- "Principal Component Analysis: A Review" (Jolliffe, 2016)
- "k-means++: The Advantages of Careful Seeding" (Arthur & Vassilvitskii, 2007)

---

## 📝 Changelog y Versiones

### Versión 2.0 (Actual)
- ✅ Sistema de tour interactivo
- ✅ Arquitectura modular completa
- ✅ Suite de testing con pytest
- ✅ Documentación técnica completa
- ✅ Sistema de logging estructurado

### Versión 1.5
- ✅ Machine Learning (PCA + K-Means)
- ✅ Sistema de exportaciones
- ✅ Validación de archivos
- ✅ Múltiples temas visuales

### Versión 1.0
- ✅ Aplicación base Streamlit
- ✅ Análisis estadístico básico
- ✅ Visualizaciones con Plotly/Matplotlib
- ✅ Carga de archivos CSV/Excel

### Roadmap Futuro
- 🔄 Integración con bases de datos
- 🔄 API REST para integraciones
- 🔄 Sistema de usuarios y autenticación
- 🔄 Dashboard en tiempo real
- 🔄 Análisis predictivo avanzado

---

*Documentación Técnica v2.0*  
*Última actualización: Septiembre 2025*  
*Equipo de Desarrollo: Sistema Zambranos*
