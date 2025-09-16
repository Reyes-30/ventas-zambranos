# 📚 Manual de Usuario - Sistema de Análisis de Ventas Zambranos

## 🎯 Introducción

¡Bienvenido al Sistema de Análisis de Ventas Zambranos! Esta aplicación web te permite analizar datos de ventas de manera profesional, generar reportes ejecutivos y descubrir patrones ocultos usando inteligencia artificial.

### ✨ Características Principales

- **📊 Análisis Estadístico Completo**: Métricas clave, tendencias temporales y análisis por categorías
- **🤖 Machine Learning Integrado**: PCA y Clustering para descubrir patrones avanzados
- **📈 Gráficas Interactivas**: Visualizaciones dinámicas con Plotly y Matplotlib
- **📥 Exportaciones Profesionales**: CSV, ZIP, reportes Word con un clic
- **🎨 Interfaz Moderna**: UI responsiva con temas personalizables
- **🔒 Manejo Seguro de Archivos**: Validación, logging y persistencia automática

---

## 🚀 Primeros Pasos

### 1. **Tour Interactivo** (¡RECOMENDADO!)

Al abrir la aplicación, encontrarás un botón **"❓ Tour Interactivo"** en el panel lateral. Este tour te guiará paso a paso por todas las funcionalidades de manera visual e interactiva.

**¿Por qué usar el tour?**
- 📋 Explicación completa de cada sección
- 💡 Consejos y mejores prácticas
- 🎯 Flujo recomendado de análisis
- ⚡ Aprende en 5-10 minutos

### 2. **Carga de Datos**

#### Formatos Soportados
- **CSV**: Con cualquier delimitador (coma, punto y coma, tab)
- **Excel**: Archivos .xlsx y .xls

#### Columnas Requeridas
Tu archivo debe contener estas columnas obligatorias:
- `Mes`: Nombre del mes (ej: "Enero", "Febrero")
- `Categoría`: Categoría del producto
- `Cantidad Vendida`: Unidades vendidas (numérico)
- `Ingreso Total`: Ingresos totales (numérico)
- `ISV`: Impuesto sobre ventas (numérico)
- `Utilidad Bruta`: Ganancia bruta (numérico)

#### Columnas Opcionales (para análisis avanzado)
- `Precio Unitario`, `Costo Unitario`, `Costo Total`, `Ingreso Neto`

#### Pasos para Cargar
1. Ve al **Panel de Control Lateral** → **📁 Cargar Datos**
2. Haz clic en **"Selecciona tu archivo de datos"**
3. Elige tu archivo CSV o Excel
4. Si es CSV, selecciona el delimitador (o deja "Auto")
5. ¡El sistema validará y cargará automáticamente!

#### 💡 Archivos Recientes
Una vez subido, tu archivo se guarda de forma segura y aparece en **"Archivos recientes"** para reutilizar sin volver a subirlo.

---

## 📊 Guía por Secciones

### **Tab 1: 📊 Resumen Ejecutivo**

Tu dashboard principal con las métricas más importantes.

#### Métricas Clave Automáticas
- **💰 Ingresos Totales**: Suma de todos los ingresos
- **🏛️ ISV Total**: Impuesto total generado
- **📈 Utilidad Promedio**: Media de utilidad bruta
- **🛒 Unidades Vendidas**: Total de productos vendidos
- **🏪 Categorías**: Número de categorías diferentes
- **📅 Meses Activos**: Meses con datos

#### Vista de Datos Interactiva
- **Filtro por Mes**: Ver datos específicos de un mes
- **Filtro por Categoría**: Analizar una categoría particular
- **Filas Visibles**: Ajustar cuántos registros mostrar

#### Exportaciones Disponibles
- **📥 CSV**: Datos filtrados para Excel
- **📝 Reporte DOCX**: Documento Word profesional con métricas
- **📦 ZIP**: Paquete completo con todos los datos

### **Tab 2: 📈 Análisis Temporal**

Descubre cómo evoluciona tu negocio mes a mes.

#### Tipos de Análisis
1. **📈 Ingresos por Mes**
   - Gráfico de barras con valores
   - Identificación automática del mejor y peor mes
   - Descarga individual en PNG

2. **🏛️ ISV por Mes**
   - Línea de tiempo del impuesto generado
   - Estadísticas de ISV total y promedio mensual

3. **📊 Comparativo Mensual**
   - Ingresos vs ISV en una sola gráfica
   - Visualización con doble eje Y

#### Características Especiales
- **Orden Cronológico**: Los meses siempre en secuencia correcta
- **Gráficas Interactivas**: Hover para detalles (si está activado)
- **📦 ZIP Masivo**: Descarga todas las gráficas temporales de una vez

### **Tab 3: 🎯 Análisis por Categoría**

Identifica qué productos impulsan tu negocio.

#### Análisis Disponibles
1. **🥧 Distribución de Ventas**
   - Gráfico de pastel con porcentajes
   - Estadísticas detalladas por categoría
   - Exportación CSV automática

2. **💰 Utilidad por Categoría**
   - Selector: Promedio vs Total
   - Gráfico horizontal ordenado
   - Tabla resumen exportable

3. **🏆 Ranking de Categorías**
   - **Top 3 Visual**: Medallas oro, plata, bronce
   - **Métrica Configurable**: Ingresos, ventas, utilidad, ISV
   - **Tabla Completa**: Ranking con posiciones

#### 📥 Exportaciones por Análisis
Cada tipo de análisis tiene su botón de exportación CSV individual.

### **Tab 4: 🔍 Análisis Estadístico**

Herramientas avanzadas para analistas de datos.

#### Análisis Disponibles
1. **📊 Histogramas**
   - Multiselección de variables
   - Detección de distribución normal
   - Bins configurables automáticamente

2. **📦 Boxplots**
   - Identificación automática de outliers
   - Estadísticas de dispersión
   - Comparación visual entre variables

3. **🔗 Correlaciones**
   - Matriz de calor interactiva
   - **Top 5 Correlaciones** automáticas con interpretación:
     - 🟢 Fuerte positiva (>0.7)
     - 🔴 Fuerte negativa (<-0.7)
     - 🔵 Moderada (0.3-0.7)

4. **📈 Estadísticas Descriptivas**
   - Resumen completo: media, mediana, desviación estándar
   - **Datos Faltantes**: Detección por variable
   - **Rangos**: Valores mínimos y máximos

#### 💡 Interpretación Automática
El sistema proporciona interpretaciones automáticas de outliers, correlaciones y calidad de datos.

### **Tab 5: 🧮 Machine Learning**

Inteligencia artificial aplicada a tus datos de ventas.

#### Algoritmos Disponibles
1. **🔍 Análisis PCA (Componentes Principales)**
   - Reducción dimensional para visualizar patrones
   - **Varianza Explicada**: % por componente
   - Gráfico 2D de los datos transformados

2. **🎯 Clustering (K-Means)**
   - Segmentación automática de datos
   - **K Configurable**: 2-8 grupos (slider en sidebar)
   - **Perfil por Clúster**: Heatmap con características promedio
   - **Score de Silueta**: Calidad de la segmentación

3. **📊 Análisis Combinado**
   - PCA + Clustering integrado
   - **Recomendaciones Automáticas**:
     - Varianza >80%: Excelente reducción
     - Silueta >0.5: Clusters bien definidos

#### Configuración
- **Sidebar** → **⚙️ Configuración** → **Número de clústeres**
- Ajusta K según tus necesidades de segmentación

---

## ⚙️ Configuración Avanzada

### Panel de Control Lateral

#### 🎨 Temas Visuales
- **Moderno**: Colores vibrantes, gradientes
- **Clásico**: Estilo tradicional de análisis
- **Oscuro**: Ideal para presentaciones

#### 📱 Modo de Gráficas
- **Interactivas ON**: Plotly (zoom, hover, filtros)
- **Interactivas OFF**: Matplotlib (estáticas, más rápidas)

#### 🔢 Parámetros Machine Learning
- **Número de Clústeres**: Para K-Means
- **Componentes PCA**: 2-5 dimensiones

---

## 📥 Sistema de Exportaciones

### Tipos de Exportación

#### 📊 Gráficas
- **Individual**: PNG alta resolución (300 DPI)
- **Masivo por Sección**: ZIP con todas las gráficas de temporal/categoría
- **Formato**: Optimizado para presentaciones e informes

#### 📋 Datos
- **CSV Procesados**: Tablas con análisis aplicado
- **Datos Filtrados**: Según filtros activos
- **Compatibilidad**: Excel, Google Sheets, R, Python

#### 📝 Reportes
- **Word (DOCX)**: Formato ejecutivo profesional
- **Contenido**: Métricas clave + interpretación
- **Personalizable**: Agregar notas propias

#### 📦 Paquetes Completos
- **ZIP Todo Incluido**: Datos + Gráficas + Reporte
- **Archival**: Ideal para documentar análisis completos

### Flujo Recomendado de Exportación
1. **Explora** todas las secciones
2. **Genera** las gráficas necesarias
3. **Descarga ZIP** por sección o completo
4. **Exporta reporte** Word para ejecutivos
5. **Guarda CSV** de datos clave para seguimiento

---

## 💡 Consejos y Mejores Prácticas

### 📁 Preparación Óptima de Datos
- **Nombres de Mes**: Usar español ("Enero", "Febrero")
- **Números Limpios**: Sin símbolos de moneda en datos numéricos
- **Categorías Consistentes**: Evitar variaciones ("Electrónicos" vs "Electronico")
- **Celdas Completas**: Minimizar datos faltantes en columnas clave

### 📊 Flujo de Análisis Efectivo
1. **Inicio**: Resumen Ejecutivo para KPIs generales
2. **Temporal**: Identificar tendencias y estacionalidad
3. **Categorías**: Segmentar por productos/servicios
4. **Estadístico**: Profundizar en distribuciones y correlaciones
5. **ML**: Descubrir patrones ocultos y segmentaciones naturales

### 🚀 Optimización de Rendimiento
- **Archivos <10MB**: Para fluidez óptima
- **Gráficas Estáticas**: Si experimentas lag con interactivas
- **Filtros Activos**: Para datasets muy grandes (>50k filas)
- **Sesiones Cortas**: Recargar si el análisis se vuelve lento

### 📈 Interpretación de Resultados

#### Métricas Clave
- **Crecimiento Mensual**: Comparar mes actual vs anterior
- **Categoría Dominante**: >30% de ventas indica dependencia
- **Correlación Fuerte**: >0.7 sugiere relación causal
- **Outliers Frecuentes**: Revisar calidad de datos

#### Machine Learning
- **PCA Varianza >60%**: Reducción dimensional válida
- **Clusters Balanceados**: Evitar 1 grupo con >80% de datos
- **Silueta <0.3**: Considerar cambiar número de clústeres

---

## 🔧 Solución de Problemas (Troubleshooting)

### Errores Comunes

#### ❌ "Faltan columnas requeridas"
**Causa**: El archivo no tiene las columnas obligatorias
**Solución**: 
1. Verificar nombres exactos de columnas
2. Revisar que no haya espacios extra
3. Usar plantilla con columnas correctas

#### ❌ "No se pudo leer el archivo"
**Causa**: Formato no soportado o archivo corrupto
**Solución**:
1. Verificar extensión (.csv, .xlsx, .xls)
2. Abrir archivo en Excel para validar formato
3. Guardar como CSV UTF-8 si hay caracteres especiales

#### ❌ "Datos insuficientes para análisis"
**Causa**: Muy pocas filas para ML o estadísticas
**Solución**:
1. Mínimo 10 filas para estadísticas básicas
2. Mínimo 50 filas para ML
3. Revisar filtros activos que limiten datos

### Problemas de Rendimiento

#### 🐌 "Aplicación lenta"
**Soluciones**:
1. Reducir tamaño de archivo (<5MB)
2. Desactivar gráficas interactivas
3. Usar filtros para limitar datos visualizados
4. Recargar navegador para limpiar memoria

#### 📊 "Gráficas no aparecen"
**Soluciones**:
1. Verificar que hay datos para el período seleccionado
2. Revisar filtros activos
3. Cambiar a gráficas estáticas temporalmente
4. Verificar conexión a internet (para Plotly)

### Archivos y Datos

#### 💾 "No encuentro mi archivo subido"
- Los archivos se guardan automáticamente en "Archivos recientes"
- Buscar por nombre con hash (ej: "datos-a1b2c3.csv")
- Persistencia por sesión del navegador

#### 📋 "Los datos se ven extraños"
1. Verificar delimitador CSV correcto
2. Revisar codificación de caracteres (UTF-8 recomendado)
3. Validar tipos de datos (números vs texto)

---

## ❓ Preguntas Frecuentes (FAQ)

### General

**Q: ¿Mis datos están seguros?**
A: Sí. Los archivos se procesan localmente y se almacenan con hash único. No se envían a servidores externos.

**Q: ¿Puedo usar datos de otros países/idiomas?**
A: Sí, pero los nombres de meses deben estar en español para el análisis temporal.

**Q: ¿Hay límite de tamaño de archivo?**
A: No hay límite estricto, pero recomendamos <10MB para rendimiento óptimo.

### Funcionalidades

**Q: ¿Puedo añadir más columnas a mi análisis?**
A: Sí, cualquier columna numérica adicional se incluye automáticamente en estadísticas y ML.

**Q: ¿Cómo interpretar los clusters de ML?**
A: Usa el heatmap de perfil promedio. Clusters con valores similares representan segmentos de datos parecidos.

**Q: ¿Las gráficas se pueden personalizar?**
A: Los temas y tipos (interactivo/estático) sí. Para personalización avanzada, exporta los datos y usa tu herramienta preferida.

### Exportaciones

**Q: ¿En qué formato son las gráficas descargadas?**
A: PNG de alta resolución (300 DPI), ideal para documentos e presentaciones.

**Q: ¿Puedo editar el reporte Word?**
A: Completamente. El DOCX se puede abrir en Word, Google Docs o LibreOffice para personalizar.

**Q: ¿Los ZIP incluyen datos originales?**
A: Incluyen los datos procesados/filtrados, no necesariamente los originales completos.

---

## 🚀 Próximos Pasos

### Para Usuarios Avanzados
1. **Automatización**: Considera usar Python/R para análisis repetitivos
2. **Integración**: Los CSV exportados se pueden conectar con BI tools (Power BI, Tableau)
3. **Seguimiento**: Usa este sistema mensualmente para tracking de KPIs

### Feedback y Mejoras
- El sistema incluye logging automático para mejoras futuras
- Patrones de uso ayudan a optimizar funcionalidades
- Reportar bugs o sugerencias al equipo de desarrollo

---

## 📞 Soporte

### Recursos de Ayuda
- **🎯 Tour Interactivo**: Dentro de la aplicación
- **❓ Ayuda Contextual**: En cada sección de análisis
- **📚 Manual Técnico**: Para desarrolladores
- **🔧 Logs**: En `logs/app.log` para debugging

### Contacto
Para soporte técnico o consultas avanzadas:
- **Documentación**: Ver `docs/documentacion_tecnica.md`
- **Código**: Revisar comentarios en `src/app/`
- **Testing**: Ejecutar `pytest` para validaciones

---

*Última actualización: Septiembre 2025*
*Versión: 2.0 - Sistema de Análisis Avanzado*
