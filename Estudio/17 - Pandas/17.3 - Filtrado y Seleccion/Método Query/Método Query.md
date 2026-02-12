# 📘 Teoría: El Método `.query()` en Pandas

## 📌 Definición Técnica

El método `.query()` es una función de los DataFrames de Pandas que
permite **filtrar filas** basándose en una expresión lógica escrita como
una cadena de texto (string).

En lugar de evaluar la condición directamente con la sintaxis estándar
de Python (que requiere corchetes `[]` y referencias repetitivas al
objeto), `.query()` toma esa cadena de texto y la procesa internamente
--- a menudo usando un motor optimizado llamado `numexpr` --- para
devolver un nuevo DataFrame con las filas que cumplen la condición.

------------------------------------------------------------------------

## 🎯 ¿Para qué es y para qué sirve?

Su propósito principal es la **legibilidad y la concisión**.

### 1️⃣ Simplificación Sintáctica

Elimina el "ruido visual" del código.\
En la sintaxis tradicional debes repetir el nombre del DataFrame
múltiples veces. Con `.query()`, Pandas asume que cualquier nombre
dentro del texto se refiere a una columna del DataFrame.

### 2️⃣ Expresividad Natural

Permite escribir reglas de filtrado que se leen casi como oraciones en
inglés o sentencias SQL.\
Esto facilita que cualquier persona entienda qué datos se están
buscando, incluso sin dominar Python.

### 3️⃣ Optimización de Memoria (Backend)

En conjuntos de datos grandes (millones de filas), `.query()` puede ser
más eficiente que el filtrado tradicional porque evita crear copias
intermedias innecesarias en memoria durante la evaluación.

------------------------------------------------------------------------

## 🚦 ¿Cuándo debería usarse? (Best Practices)

Según recomendaciones como las del libro *Effective Pandas*, conviene
usar `.query()` cuando:

### ✔ Tienes múltiples condiciones

Si tu filtro involucra varias reglas unidas por operadores lógicos, la
sintaxis es más limpia y fácil de leer.

### ✔ Estás encadenando métodos

Cuando construyes una tubería de procesamiento (cargar → limpiar →
filtrar → analizar), `.query()` mantiene la fluidez y legibilidad.

### ✔ Comparas columnas entre sí

Es especialmente útil cuando necesitas comparar directamente valores
entre columnas.

------------------------------------------------------------------------

## 🚫 ¿Cuándo NO debería usarse?

### ❌ Asignación o modificación de datos

`.query()` solo filtra y devuelve datos.\
No permite modificar valores. Para eso debe utilizarse `.loc`.

### ❌ Nombres de columna complejos

Si las columnas tienen espacios, símbolos especiales o comienzan con
números, usar `.query()` puede volverse incómodo porque requiere
comillas especiales (backticks). En esos casos, la sintaxis tradicional
puede ser más clara.

------------------------------------------------------------------------

## ⚙️ Operadores y Funcionalidades Disponibles dentro de `.query()`

Dentro de las comillas de `.query("...")`, se permite una sintaxis
específica:

### 1️⃣ Operadores Lógicos (en inglés)

Se utilizan palabras en lugar de símbolos:

-   `and` → Intersección lógica\
-   `or` → Unión lógica\
-   `not` → Negación

------------------------------------------------------------------------

### 2️⃣ Operadores de Comparación

Se mantienen los operadores estándar:

-   `==` Igual a\
-   `!=` Diferente de\
-   `>` Mayor que\
-   `<` Menor que\
-   `>=` Mayor o igual que\
-   `<=` Menor o igual que

------------------------------------------------------------------------

### 3️⃣ Listas y Pertenencia

Permite verificar si un valor pertenece a un conjunto de opciones:

-   `in`\
-   `not in`

------------------------------------------------------------------------

### 4️⃣ Referencia a Variables Externas (`@`)

Si necesitas usar una variable definida fuera del DataFrame, debes
anteponer `@` al nombre de la variable dentro de la cadena.

Esta es una de las funcionalidades más potentes del método.

------------------------------------------------------------------------

### 5️⃣ Referencia al Índice (`index`)

Se puede filtrar utilizando directamente la etiqueta del índice del
DataFrame mediante la palabra reservada `index`.

------------------------------------------------------------------------

### 6️⃣ Métodos de Strings (`.str`)

Es posible utilizar métodos de cadenas cuando el motor lo permite, como
búsquedas parciales de texto.

------------------------------------------------------------------------

### 7️⃣ Operaciones Matemáticas

Se pueden realizar cálculos directamente dentro de la expresión lógica,
permitiendo filtros basados en operaciones aritméticas entre columnas.

------------------------------------------------------------------------

# 🧠 Conclusión

El método `.query()` es una herramienta poderosa para filtrar datos en
Pandas de forma más limpia, expresiva y, en algunos casos, más
eficiente.

Su mayor ventaja es la legibilidad, especialmente en análisis complejos
con múltiples condiciones o en flujos de procesamiento encadenados.

Sin embargo, no debe utilizarse para modificar datos ni cuando las
columnas tienen nombres problemáticos que dificulten su uso dentro de
cadenas de texto.
