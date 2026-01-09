# ¿Qué es un Array en NumPy?

## Definición

Un array de NumPy es un objeto llamado **ndarray** (*n-dimensional
array*).

Es:

-   Una estructura de datos **numéricos**
-   **Homogénea** (un solo tipo de dato)
-   Muy **eficiente**
-   **Multidimensional**

> 📌 En análisis de datos, todo termina siendo un array.

------------------------------------------------------------------------

## Diferencia clave: Lista vs Array

### Lista (Python)

-   Puede mezclar tipos
-   Pensada para lógica general
-   Más lenta con muchos datos

### Array (NumPy)

-   Un solo tipo de dato
-   Pensado para cálculos
-   Mucho más rápido

👉 **Regla mental:**

-   Lógica → listas\
-   Datos → NumPy

------------------------------------------------------------------------

## Dimensiones de un Array

### 🔹 Array 0D (Escalar)

-   Un solo valor
-   Rara vez se usa solo

### 🔹 Array 1D (Vector)

    [10 20 30]

Uso típico: - Listas de valores - Una columna de datos

### 🔹 Array 2D (Matriz)

    [[1 2 3]
     [4 5 6]]

Uso típico: - Tablas - Datasets - Filas y columnas

### 🔹 Array 3D o más

Uso típico: - Imágenes - Series de datos - Machine Learning

👉 En análisis de datos se usan principalmente arrays **1D y 2D**.

------------------------------------------------------------------------

## Propiedades importantes del ndarray

  Propiedad   Qué indica
  ----------- -----------------------
  ndim        Número de dimensiones
  shape       Tamaño por dimensión
  size        Total de elementos
  dtype       Tipo de dato

👉 **Siempre revisa estas propiedades antes de analizar datos.**

------------------------------------------------------------------------

## Homogeneidad (Muy importante)

En NumPy:

    [1, 2, 3]      → OK
    [1, 2, "hola"] → NO recomendable

Si mezclas tipos: - NumPy convierte todo - Pierdes eficiencia - Puedes
tener errores silenciosos
