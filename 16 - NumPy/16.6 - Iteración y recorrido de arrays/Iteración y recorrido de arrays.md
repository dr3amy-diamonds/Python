# 🧠 ¿Por qué existe la iteración en NumPy?

NumPy está pensado para **operaciones vectorizadas**, no para bucles
tradicionales.\
Entonces... ¿por qué aprender iteración?

Porque:

-   No siempre se puede vectorizar todo
-   Necesitas entender código existente
-   Hay casos complejos (lógica condicional, estructuras irregulares)
-   Ayuda a entender cómo está organizado un array

👉 **Iterar es una herramienta, no el objetivo.**

------------------------------------------------------------------------

## 🧠 Idea clave del tema

En NumPy, **iterar es posible, pero casi nunca es lo óptimo**.

El buen analista:

-   Sabe iterar
-   Sabe cuándo **NO** hacerlo

------------------------------------------------------------------------

## 🔹 Iteración básica en arrays 1D

Conceptualmente:

-   Recorres elemento por elemento
-   Igual que una lista

Útil para:

-   Inspección
-   Depuración
-   Lógica condicional simple

❌ **No es eficiente para grandes datos**

------------------------------------------------------------------------

## 🔹 Iteración en arrays 2D

Aquí aparecen dos niveles:

-   Filas
-   Columnas

### Iterar por filas

-   Común
-   Fácil de entender

### Iterar por columnas

-   Menos intuitivo
-   Requiere entender `shape` y ejes

👉 Aquí empiezas a pensar en **estructura de datos**, no solo valores.

------------------------------------------------------------------------

## 🔹 Iterar con índices

Permite:

-   Saber dónde estás
-   Modificar valores con control

Pero:

-   Más código
-   Más propenso a errores

📌 Recomendado solo cuando: - Necesitas la posición - No hay alternativa
vectorizada

------------------------------------------------------------------------

## 🔹 Iteración avanzada: `nditer`

`nditer` es el iterador interno de NumPy.

Permite:

-   Recorrer arrays de cualquier dimensión
-   Controlar lectura/escritura
-   Manejar broadcasting manual

👉 Potente, pero **rara vez necesario** en análisis básico.

------------------------------------------------------------------------

## 🔹 Orden de iteración (muy importante)

NumPy almacena datos en memoria en:

-   **C-order (por filas)** por defecto

Iterar siguiendo este orden:

✔ Más rápido\
❌ Cambiar el orden puede ser costoso

👉 El orden de memoria **afecta el rendimiento**.

------------------------------------------------------------------------

## 🔹 Cuándo sí usar iteración

✔ Inspección de datos\
✔ Lógica compleja por elemento\
✔ Prototipos rápidos\
✔ Casos muy específicos

------------------------------------------------------------------------

## 🔹 Cuándo NO usar iteración

❌ Operaciones matemáticas masivas\
❌ Transformaciones simples\
❌ Filtrado\
❌ Agregaciones

👉 Para eso existen:

-   Vectorización
-   Broadcasting
-   Funciones de NumPy

------------------------------------------------------------------------

## 🔹 Alternativas a la iteración

Antes de iterar, pregúntate:

-   ¿Puedo usar operaciones vectorizadas?
-   ¿Puedo usar indexado booleano?
-   ¿Puedo usar funciones de NumPy?

👉 Casi siempre la respuesta es **sí**.

------------------------------------------------------------------------

## 🔹 Errores comunes

❌ Usar `for` como en listas\
❌ Iterar cuando basta una operación vectorizada\
❌ No entender qué eje se recorre\
❌ Modificar datos innecesariamente\
❌ Crear bucles anidados costosos

------------------------------------------------------------------------

## 🔹 Buenas prácticas

✔ Evita bucles si puedes\
✔ Usa iteración solo cuando sea necesario\
✔ Prefiere funciones nativas\
✔ Piensa en filas y columnas\
✔ Revisa `shape` antes de iterar

------------------------------------------------------------------------

## 🔹 Métodos de iteración (conceptual)

  Método                    Uso
  ------------------------- ---------------------
  `for elemento in array`   Arrays 1D
  `for fila in matriz`      Recorrer filas
  `range + índices`         Control de posición
  `nditer`                  Casos avanzados
  `enumerate`               Índice + valor

------------------------------------------------------------------------

## 🧠 Conexión con análisis de datos

En análisis real:

-   Iteras poco
-   Seleccionas mucho
-   Transformas masivamente

👉 **Iteración = último recurso**\
👉 **Vectorización = camino principal**

------------------------------------------------------------------------

## 🧭 Resumen mental

✔ Iterar es posible\
✔ No siempre es buena idea\
✔ Conocerla evita malas decisiones\
✔ Saber cuándo **NO** iterar es clave
