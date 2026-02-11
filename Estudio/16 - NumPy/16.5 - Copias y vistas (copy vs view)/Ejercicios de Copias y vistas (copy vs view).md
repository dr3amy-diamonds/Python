# 🟩 EJERCICIOS --- 16.5 COPIAS Y VISTAS (NUMPY)

## 🟢 Ejercicio 1 --- Vista básica

Crea un array 1D con los valores del 1 al 10.

Luego: 
- Obtén una subparte del array usando slicing 
- Modifica un valor de la subparte 
- Observa qué ocurre en el array original

📌 **Objetivo:** comprobar que el slicing devuelve una vista.

------------------------------------------------------------------------

## 🟢 Ejercicio 2 --- Copia segura

Usando el mismo array del ejercicio anterior: 
- Obtén una subparte 
- Crea una copia explícita usando `.copy()` 
- Modifica la copia 
- Verifica que el original no cambia

📌 **Objetivo:** diferenciar vista vs copia.

------------------------------------------------------------------------

## 🟡 Ejercicio 3 --- reshape y memoria

Crea un array 1D con 6 elementos.

Luego: 
- Cambia su forma a `(2, 3)` 
- Modifica un valor del array reestructurado 
- Observa si el array original cambia

📌 **Objetivo:** entender que `reshape()` suele devolver una vista.

------------------------------------------------------------------------

## 🟡 Ejercicio 4 --- flatten vs ravel

Crea un array 2D.

Luego: 
- Convierte el array a 1D usando `flatten()` 
- Modifica el resultado 
- Verifica si el original cambió

Repite: - usando `ravel()` - compara los resultados

📌 **Objetivo:** entender seguridad vs eficiencia.

------------------------------------------------------------------------

## 🟠 Ejercicio 5 --- Transposición

Crea un array 2D.

Luego: 
- Obtén su transpuesta usando `.T` 
- Modifica un valor de la transpuesta 
- Observa el efecto en el array original

📌 **Objetivo:** confirmar que `.T` devuelve una vista.

------------------------------------------------------------------------

## 🟠 Ejercicio 6 --- Referencias en Python

Crea un array y asígnalo a otra variable.

Luego: 
- Modifica el segundo 
- Observa el primero

📌 **Objetivo:** entender que `b = a` no crea copia.

------------------------------------------------------------------------

## 🔵 Ejercicio 7 --- Identifica el tipo (mental)

Para cada caso, indica si se obtiene **vista** o **copia**:

-   `arr[2:5]`
-   `arr.copy()`
-   `arr.flatten()`
-   `arr.ravel()`
-   `arr.T`
-   `b = arr`

📌 **Objetivo:** razonamiento sin ejecutar.

------------------------------------------------------------------------

## 🔵 Ejercicio 8 --- Regla de oro (reflexión)

Responde en un comentario o archivo `.md`:

**¿Por qué es peligroso modificar arrays sin saber si son vistas o
copias?**

## Respuesta
Porque puedes alterar datos originales sin darse cuenta, introduciendo errores silenciosos y difíciles de depurar.
