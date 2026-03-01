# Visualización de Datos y EDA

## Fundamentos Teóricos Basados en la Industria

------------------------------------------------------------------------

## 1. ¿Qué es el EDA y la Visualización de Datos?

### EDA (Exploratory Data Analysis)

El Análisis Exploratorio de Datos (EDA) es un término acuñado por el
matemático John Tukey en los años 70. Consiste en "interrogar" a los
datos utilizando herramientas estadísticas y visuales antes de sacar
conclusiones definitivas.

Es el proceso de buscar: - Patrones - Valores atípicos (outliers) -
Relaciones inesperadas - Errores en los datos

El objetivo es comprender profundamente la estructura y el
comportamiento de la información antes de modelarla o presentarla.

### Visualización de Datos

La visualización de datos es la traducción de información numérica a un
formato visual como puntos, líneas o barras.

El cerebro humano no está diseñado para procesar miles de filas en una
tabla, pero sí puede detectar patrones visuales de manera casi
instantánea. Una tendencia descendente puede reconocerse en menos de un
segundo cuando se representa como línea.

### ¿Para qué se usa?

La visualización cumple dos funciones fundamentales:

**Descubrir (para el analista):** - Encontrar errores en los datos. -
Detectar correlaciones inesperadas. - Identificar distribuciones
inusuales.

**Comunicar (para el negocio):** - Explicar resultados a perfiles no
técnicos. - Justificar decisiones con evidencia visual. - Traducir
números en narrativas comprensibles.

------------------------------------------------------------------------

## 2. Los 4 Tipos de Gráficos Más Utilizados en la Industria

En la mayoría de entornos corporativos, el 95% de los análisis visuales
se resuelven con cuatro tipos de gráficos.

### A. Gráfico de Líneas (Line Chart)

**¿Qué es?**\
Puntos conectados por líneas a lo largo de un eje.

**¿Cuándo se usa?**\
Exclusivamente para series de tiempo o datos continuos. Permite observar
cómo cambia una métrica a lo largo del tiempo.

Ejemplos: - Evolución de ventas mensuales. - Crecimiento de usuarios
diarios. - Cambios en temperatura anual.

Es el gráfico ideal para analizar tendencias.

------------------------------------------------------------------------

### B. Gráfico de Barras (Bar Chart)

**¿Qué es?**\
Rectángulos cuya longitud representa el valor de una categoría.

**¿Cuándo se usa?**\
Para comparar categorías estáticas.

Ejemplos: - Ventas por país. - Ingresos por categoría de producto. -
Tráfico por tipo de dispositivo.

Las barras pueden ser verticales u horizontales. Las horizontales son
especialmente útiles cuando los nombres de las categorías son largos.

------------------------------------------------------------------------

### C. Histograma (Histogram)

**¿Qué es?**\
Similar a un gráfico de barras, pero con las barras unidas. Representa
la distribución de una sola variable numérica.

**¿Cuándo se usa?**\
Cuando se desea analizar cómo se agrupan los datos dentro de rangos.

Ejemplos: - Distribución de edades de clientes. - Distribución de montos
de compra. - Distribución de salarios.

El parámetro clave es el número de intervalos (bins), que define en
cuántos grupos se dividen los datos.

------------------------------------------------------------------------

### D. Gráfico de Dispersión (Scatter Plot)

**¿Qué es?**\
Una nube de puntos en un plano con eje X y eje Y.

**¿Cuándo se usa?**\
Para detectar correlaciones entre dos variables numéricas.

Ejemplos: - Años de experiencia vs salario. - Inversión en publicidad vs
ventas. - Horas de estudio vs calificación.

Si los puntos tienden a formar una línea ascendente, existe correlación
positiva. Si descienden, la correlación es negativa.

------------------------------------------------------------------------

## 3. Filosofía de Trabajo con Pandas y Visualización

Los referentes de la industria coinciden en un punto fundamental: Pandas
no dibuja gráficos desde cero.

Internamente utiliza la biblioteca matplotlib. Pandas actúa como un
"wrapper", es decir, una capa simplificada que automatiza
configuraciones y aprovecha la estructura del DataFrame (índices y
columnas) para generar visualizaciones rápidamente.

### Principios Fundamentales

#### La Regla del Índice

Antes de graficar, el índice del DataFrame debe representar
correctamente el eje principal del análisis.

-   Para gráficos de líneas: el tiempo debe ser el índice.
-   Para gráficos de barras por categoría: las categorías deben ser el
    índice.

Un índice mal definido produce gráficos confusos o incorrectos.

#### Encadenamiento de Transformaciones

El flujo profesional consiste en:

1.  Tomar datos crudos.
2.  Filtrar.
3.  Agrupar.
4.  Agregar.
5.  Visualizar.

Todo en un flujo continuo y limpio, evitando variables intermedias
innecesarias.

Esto mejora: - Legibilidad - Reproducibilidad - Mantenibilidad del
código

------------------------------------------------------------------------

## 4. Parámetros Clave para Visualizaciones Profesionales

Al generar un gráfico, es importante controlar ciertos parámetros para
mantener calidad visual y coherencia corporativa.

### Tamaño del Lienzo (figsize)

Define el ancho y alto del gráfico. Un tamaño inadecuado puede
dificultar la lectura.

### Título (title)

Debe describir claramente qué se está observando. Un gráfico sin título
pierde contexto.

### Color (color)

Permite mantener identidad visual o estándares corporativos.

### Transparencia (alpha)

Controla el nivel de opacidad. Es especialmente útil en histogramas
superpuestos.

------------------------------------------------------------------------

## Conclusión

La visualización de datos no es decoración. Es una herramienta
analítica.

El EDA combina estadística y visualización para comprender los datos
antes de interpretarlos formalmente. En entornos profesionales, dominar
los cuatro gráficos fundamentales y comprender la estructura del
DataFrame es suficiente para resolver la mayoría de los problemas de
análisis exploratorio.

Una visualización bien construida: - Descubre patrones. - Detecta
errores. - Comunica decisiones. - Reduce ambigüedad.

La calidad del análisis depende tanto de la interpretación como de la
claridad con la que se presenta.
