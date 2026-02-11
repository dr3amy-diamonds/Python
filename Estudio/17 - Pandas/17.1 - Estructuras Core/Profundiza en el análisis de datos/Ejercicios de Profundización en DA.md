# Ejercicios Prácticos --- Pandas (Series)

## 🟢 Ejercicio 1: Conversión de Divisas (Broadcasting)

### Contexto

Trabajas en el departamento de finanzas. Tienes una lista de precios
base en **Dólares (USD)** y necesitas proyectar esos costos en **Pesos
Colombianos (COP)** usando una tasa de cambio fija.

### Datos de Entrada

-   **Lista de Productos:**\
    `['Monitor', 'Mouse', 'Teclado', 'Auriculares']`

-   **Lista de Precios (USD):**\
    `[250, 25, 40, 60]`

-   **Tasa de Cambio:**\
    `4050`

### Instrucciones

-   Construye una **Serie** llamada `s_precios_usd` asignando la lista
    de productos como índice y los precios como valores.
-   Aplica una operación matemática directa (**multiplicación**) entre
    la Serie y la tasa de cambio para crear una nueva Serie llamada
    `s_precios_cop`.
-   Muestra el resultado final.

------------------------------------------------------------------------

## 🟡 Ejercicio 2: Fusión de Inventarios (Alineación de Índices)

### Contexto

Recibes el recuento de stock de dos bodegas distintas. Debes consolidar
el inventario total. Ten en cuenta que algunos productos están en ambas
bodegas, pero otros son exclusivos de una sola.

### Datos de Entrada

**Bodega A (Serie):** - Índice: `['Laptop', 'Tablet', 'Móvil']` -
Valores: `[10, 5, 20]`

**Bodega B (Serie):** - Índice: `['Laptop', 'Reloj', 'Móvil']` -
Valores: `[15, 30, 10]`

### Instrucciones

-   Crea las dos Series (`bodega_a` y `bodega_b`) con los datos
    proporcionados.
-   Suma ambas Series y guarda el resultado en una variable llamada
    `stock_total`.
-   Analiza el resultado: observarás valores vacíos (**NaN**) en los
    productos que no estaban en ambas bodegas.
-   Utiliza el método de relleno adecuado para convertir esos NaN en
    ceros (`0.0`) y obtener un inventario limpio.

------------------------------------------------------------------------

## 🟠 Ejercicio 3: Datos de Sensores (Manejo de Nulos)

### Contexto

Un sensor ambiental registra la temperatura cada cierto tiempo. Debido a
fallos en la red, algunas lecturas se perdieron (son nulas). Debes
limpiar la data sin borrar los registros, imputando un valor promedio.

### Datos de Entrada

-   **Lecturas:**\
    `[22.5, np.nan, 23.0, 21.8, np.nan, 22.2]`\
    *(np.nan representa un valor nulo)*

### Instrucciones

-   Crea una Serie con estas lecturas.
-   Calcula y muestra cuántos datos nulos existen exactamente en la
    Serie.
-   Calcula el promedio matemático **solo** de los valores válidos.
-   Genera una nueva Serie donde los valores nulos hayan sido
    reemplazados por el promedio calculado.

------------------------------------------------------------------------

## 🔴 Ejercicio 4: Clasificación de Estudiantes (Método Apply)

### Contexto

Tienes las notas finales de un curso. El sistema de la universidad no
acepta números, solo etiquetas de texto (**"Aprobado"** o
**"Reprobado"**). Debes transformar los datos numéricos aplicando una
lógica personalizada.

### Datos de Entrada

-   **Estudiantes:**\
    `['Ana', 'Carlos', 'Luis', 'Maria']`

-   **Notas:**\
    `[4.8, 2.5, 3.0, 3.9]`

### Reglas de Negocio

-   Si la nota es **3.0 o superior** → **Aprobado**
-   Si la nota es **inferior a 3.0** → **Reprobado**

### Instrucciones

-   Crea la Serie de notas usando los estudiantes como índice.
-   Define una función de Python (con `def`) que reciba una nota y
    retorne `"Aprobado"` o `"Reprobado"` según las reglas.
-   Utiliza el método `.apply()` para generar una nueva Serie con los
    resultados textuales.
