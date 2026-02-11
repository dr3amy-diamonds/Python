# Anatomía del DataFrame (pd.DataFrame)

## 1. ¿Qué problema resuelve un DataFrame?

En la programación de análisis de datos, existen estructuras nativas con
limitaciones teóricas:

-   **Matrices matemáticas (NumPy):** eficientes pero homogéneas (un
    solo tipo de dato) y sin etiquetas semánticas.
-   **Hojas de cálculo:** claras visualmente, pero poco escalables a
    nivel programático.
-   **Listas de diccionarios:** flexibles, pero ineficientes en memoria
    y rendimiento.

❌ **Sin DataFrame:** no existe una estructura que combine velocidad,
heterogeneidad y semántica.\
✅ **Con DataFrame:** se obtiene una estructura tabular 2D optimizada
para manipulación relacional y cálculo vectorial.

👉 Un DataFrame resuelve el problema de la **alineación de datos
heterogéneos** mediante un **índice compartido**.

------------------------------------------------------------------------

## 2. ¿Qué es realmente?

El **DataFrame** es la estructura de datos primaria de **Pandas**.

Características clave:

-   Estructura bidimensional (filas y columnas)
-   Heterogeneidad columnar (cada columna puede tener un tipo distinto)
-   Implementado como un **diccionario ordenado de Series** que
    comparten el mismo índice

------------------------------------------------------------------------

## 3. Mecánica de Creación (Sintaxis Teórica)

El constructor `pd.DataFrame()` acepta múltiples insumos:

### Insumos comunes

-   Diccionario de listas → columnas
-   Lista de diccionarios → filas
-   Arrays de NumPy → valores sin etiquetas semánticas

### Rol del índice

Si no se especifica, Pandas genera automáticamente un **RangeIndex
(0,1,2...)** para garantizar la integridad referencial.

------------------------------------------------------------------------

## 4. Los Dos Ejes (Fundamento Vectorial)

Pandas hereda el concepto de ejes de NumPy:

-   **Axis 0 (filas / índice):** operaciones verticales → resultado por
    columna
-   **Axis 1 (columnas):** operaciones horizontales → resultado por fila

👉 Comprender los ejes es esencial para agregaciones, limpieza y
transformaciones.

------------------------------------------------------------------------

## 5. Anatomía Interna del DataFrame

Un DataFrame posee tres componentes principales:

-   `.index` → etiquetas de filas
-   `.columns` → etiquetas de columnas
-   `.values` → matriz NumPy subyacente (sin etiquetas)

⚠️ Acceder a `.values` elimina el contexto semántico.

------------------------------------------------------------------------

## 6. Relación Estructural con Series

Relación jerárquica:

-   **DataFrame:** contenedor
-   **Series:** vector

Seleccionar una sola columna reduce la dimensión y devuelve una
**Series**, confirmando que el DataFrame es un conjunto de vectores
alineados.

------------------------------------------------------------------------

## 7. Estructura Mental Profesional

Visualiza un DataFrame como un **sistema de coordenadas etiquetado**:

-   Cada dato vive en `(etiqueta_fila, nombre_columna)`
-   No en `(i, j)` como en una matriz tradicional

📌 Esta perspectiva es clave para dominar indexación, alineación y
operaciones avanzadas.
