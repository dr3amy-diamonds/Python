# 🟩 16.6 --- EJERCICIOS DE ITERACIÓN EN NUMPY

## 🟢 Ejercicio 1 --- Recorrido básico (1D)

-   Crea un array 1D con 10 números enteros.
-   Recorre el array usando un `for`.
-   Imprime cada elemento.
-   Luego imprime el total de elementos recorridos.

------------------------------------------------------------------------

## 🟢 Ejercicio 2 --- Iterar y filtrar

Dado un array de números enteros: 
- Recorre el array. 
- Guarda en una lista solo los números mayores que 50. 
- Imprime la lista final.

------------------------------------------------------------------------

## 🟢 Ejercicio 3 --- Iteración con índices

-   Crea un array con 5 números.
-   Recorre el array usando índices (`range`).
-   Imprime el índice y el valor correspondiente.

------------------------------------------------------------------------

## 🟢 Ejercicio 4 --- `enumerate()`

-   Usa `enumerate()` para recorrer un array.
-   Imprime el índice.
-   Imprime el valor.
-   Muestra ambos en una sola línea.

------------------------------------------------------------------------

## 🟡 Ejercicio 5 --- Iteración en array 2D (filas)

-   Crea una matriz de tamaño `(3, 4)`.
-   Recorre la matriz por filas.
-   Imprime cada fila completa.

------------------------------------------------------------------------

## 🟡 Ejercicio 6 --- Iteración elemento a elemento (2D)

Usando la misma matriz: 
- Recorre cada elemento individualmente. 
-Imprime cada valor.

------------------------------------------------------------------------

## 🟡 Ejercicio 7 --- Iterar por columnas

-   Usa la transposición `.T`.
-   Recorre la matriz por columnas.
-   Imprime cada columna.

------------------------------------------------------------------------

## 🟡 Ejercicio 8 --- `nditer` básico

-   Usa `np.nditer()` para recorrer:
    -   un array 1D
    -   un array 2D
-   Imprime cada elemento.

------------------------------------------------------------------------

## 🟠 Ejercicio 9 --- Modificación con `nditer`

-   Crea un array de números.
-   Usa `np.nditer()` con `readwrite`.
-   Multiplica cada elemento por 2.
-   Imprime el array final.

------------------------------------------------------------------------

## 🔴 Ejercicio 10 --- Orden de iteración

-   Crea una matriz `2x3`.
-   Recorre usando `order='C'`.
-   Recorre usando `order='F'`.
-   Imprime el orden de los valores en cada caso.

------------------------------------------------------------------------

## 🔴 Ejercicio 11 --- Pensamiento crítico

Dado un array grande: 
- Escribe una solución usando **iteración**. 
- Escribe otra usando **vectorización**. 
- Reflexiona (en un comentario) cuál es mejor y por qué.

------------------------------------------------------------------------

## 🧠 Ejercicio 12 --- Caso real (análisis)

-   Simula datos de temperatura (array 1D).
-   Recorre los datos.
-   Guarda solo las temperaturas fuera de un rango normal.
-   Imprime los valores detectados.

------------------------------------------------------------------------

## 🧭 Ejercicio final --- Decisión correcta

Para cada caso, indica **en comentarios** si usarías **iteración** o
**vectorización** y explica brevemente por qué:

-   Sumar todos los valores. 
-   Aplicar una fórmula matemática.
-   Aplicar lógica condicional compleja.
-   Inspeccionar valores manualmente.

## Respuesta
**1.** Vectorización ya que se aplicara un calculo matematico. Es más eficiente para estas necesidades(Respondo de una la pregunta 2 y 3. La 4ta es iteración)
