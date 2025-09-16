# 📊 Sistema de Análisis de Ventas Zambranos - Versión Simplificada

**Aplicación web esencial para análisis de datos de ventas**

## 🎯 Funcionalidades Esenciales

✅ **Carga de Datos**: CSV y Excel  
✅ **Métricas Principales**: Ingresos, ventas, utilidad  
✅ **Análisis Temporal**: Tendencias por mes  
✅ **Análisis por Categoría**: Distribución y ranking  
✅ **Machine Learning Básico**: PCA y K-Means  

## 🚀 Instalación Rápida

```bash
# 1. Instalar dependencias mínimas
pip install -r requirements_simple.txt

# 2. Ejecutar aplicación simplificada
streamlit run app_simple.py
```

## 📋 Formato de Datos

Tu archivo debe tener estas columnas:
- `Mes` - Enero, Febrero, etc.
- `Categoría` - Categoría del producto
- `Cantidad Vendida` - Unidades (numérico)
- `Ingreso Total` - Ingresos (numérico)
- `ISV` - Impuesto (numérico)
- `Utilidad Bruta` - Ganancia (numérico)

## 🎨 Características

- **Interface Limpia**: Solo lo esencial
- **Carga Rápida**: Dependencias mínimas
- **Análisis Completo**: 4 tabs principales
- **Visualizaciones**: Plotly interactivo
- **Machine Learning**: PCA y Clustering

## 📊 Tabs Disponibles

1. **📊 Resumen**: Métricas clave y vista de datos
2. **📈 Temporal**: Gráficas por mes
3. **🎯 Categorías**: Distribución y ranking
4. **🤖 ML**: PCA y K-Means clustering

## 📦 Dependencias (Solo 6)

- `streamlit` - Framework web
- `pandas` - Análisis de datos
- `numpy` - Operaciones numéricas
- `plotly` - Gráficas interactivas
- `scikit-learn` - Machine Learning
- `openpyxl` - Lectura de Excel

---

*Versión optimizada - Solo lo necesario para análisis efectivo*
