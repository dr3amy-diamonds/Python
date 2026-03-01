# Proyecto de Análisis Inmobiliario

## Misión 1: El Pulso del Mercado (Gráfico de Líneas)

### Contexto de Negocio

La junta directiva necesita comprender la evolución del mercado
inmobiliario en el tiempo. El interés principal no es el volumen total
de ventas, sino el comportamiento del precio promedio de las propiedades
vendidas mes a mes.

### Objetivo

Construir un gráfico de líneas que represente el precio promedio
(`precio_usd`) de las propiedades vendidas, agrupado por mes.

### Fundamentación Teórica

-   Se debe utilizar una técnica de remuestreo temporal mensual
    (`resample('ME')`) combinada con el cálculo del promedio (`mean()`).
-   El gráfico de líneas es la representación visual adecuada para
    mostrar tendencias a lo largo del tiempo.
-   Es obligatorio incluir:
    -   Título claro y profesional.
    -   Etiqueta del eje X: Meses.
    -   Etiqueta del eje Y: Precio Promedio USD.
    -   Tamaño adecuado del gráfico (`figsize`) para asegurar
        legibilidad.

------------------------------------------------------------------------

## Misión 2: El Inventario Más Popular (Gráfico de Barras)

### Contexto de Negocio

El equipo de adquisiciones necesita identificar qué tipo de propiedad
tiene mayor rotación en el mercado, con el fin de optimizar futuras
inversiones y reventas.

### Objetivo

Construir un gráfico de barras horizontales que muestre la cantidad de
propiedades vendidas por cada `tipo_propiedad` (Apartamento, Casa,
Penthouse, etc.).

### Fundamentación Teórica

-   Se debe utilizar el método `value_counts()` para contabilizar la
    frecuencia de cada categoría.
-   Antes de graficar, es obligatorio aplicar `sort_values()` para que
    el gráfico funcione como un ranking ordenado, facilitando la lectura
    inmediata.
-   El gráfico debe incluir:
    -   Título descriptivo.
    -   Etiquetas de ejes correctamente definidas.
    -   Tamaño adecuado (`figsize`) para evitar compresión visual.

------------------------------------------------------------------------

## Misión 3: El Estándar de Construcción (Histograma)

### Contexto de Negocio

Una constructora aliada busca determinar cuál es el tamaño más demandado
en el mercado para ajustar sus futuros proyectos inmobiliarios.

### Objetivo

Generar un histograma de la variable `metros_cuadrados` utilizando 30
intervalos (`bins=30`).

### Fundamentación Teórica

-   El histograma permite visualizar la distribución estadística de una
    variable numérica.
-   Es importante añadir un color de borde (`edgecolor`) para
    diferenciar claramente los intervalos y evitar que el gráfico se
    perciba como una masa uniforme.
-   El gráfico debe incluir:
    -   Título profesional.
    -   Eje X: Metros Cuadrados.
    -   Eje Y: Frecuencia.
    -   Dimensiones adecuadas para una visualización clara.

------------------------------------------------------------------------

## Misión 4: Micro-Análisis de Zona (Dispersión + Filtro)

### Contexto de Negocio

Existe la hipótesis de que en el barrio "Centro" el precio de las
propiedades depende principalmente de la ubicación y no tanto del
tamaño. Se requiere validar si sigue existiendo una relación directa
entre tamaño y precio en esta zona específica.

### Objetivo

Filtrar el conjunto de datos para incluir únicamente las propiedades
vendidas en el barrio "Centro". Sobre ese subconjunto, construir un
gráfico de dispersión donde: - Eje X: `metros_cuadrados` - Eje Y:
`precio_usd`

### Fundamentación Teórica

-   Se debe aplicar un filtro lógico o el método `query()` para aislar
    el subconjunto deseado.
-   El gráfico de dispersión permite observar correlaciones entre
    variables numéricas.
-   Es recomendable utilizar el parámetro `alpha` para ajustar la
    transparencia y visualizar mejor la densidad de puntos.
-   El gráfico debe contener:
    -   Título claro.
    -   Etiquetas de ejes correctamente definidas.
    -   Tamaño adecuado (`figsize`) para análisis profesional.

------------------------------------------------------------------------

## Criterios de Excelencia

-   Evitar variables innecesarias: cada solución debe ser un flujo
    directo desde el DataFrame hasta el método de graficación.
-   Mantener formato profesional en todos los gráficos.
-   Garantizar claridad visual mediante dimensiones adecuadas.
-   Cada gráfico debe ser interpretable sin explicación adicional.
