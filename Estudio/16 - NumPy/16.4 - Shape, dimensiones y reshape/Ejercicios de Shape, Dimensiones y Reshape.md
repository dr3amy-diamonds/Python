# Ejercicios — Formas y Dimensiones en NumPy

🟢 **Ejercicio 1 — Identificando la forma**

Crea un array con los valores del 1 al 8.

Luego:

- Imprime el array  
- Imprime su `shape`  
- Imprime su `ndim`  
- Imprime su `size`  

---

🟢 **Ejercicio 2 — Cambiando la forma**

Usando el array del ejercicio anterior:

- Cambia su forma a `(2, 4)`  
- Cambia su forma a `(4, 2)`  
- Verifica que los datos no cambian  

---

🟢 **Ejercicio 3 — Uso de -1**

A partir del mismo array:

- Usa `reshape()` con `-1` para obtener un array con 2 filas  
- Usa `reshape()` con `-1` para obtener un array con 4 columnas  

---

🟡 **Ejercicio 4 — Comparando dimensiones**

Crea los siguientes arrays:

- Un vector `(n,)`  
- Un array `(n, 1)`  
- Un array `(1, n)`  

Luego:

- Imprime sus `shape`  
- Imprime sus `ndim`  

Reflexiona:  
> ¿Cuál usarías como columna y por qué?

---

🟡 **Ejercicio 5 — Flatten vs Ravel**

Crea un array 2D cualquiera.

Luego:

- Convierte el array a 1D usando `flatten()`  
- Modifica el primer elemento del resultado  
- Verifica si el array original cambió  

Repite:

- Usando `ravel()`  
- Observa la diferencia  

---

🟠 **Ejercicio 6 — Reshape inválido**

Intenta cambiar la forma de un array de 6 elementos a `(4, 4)`.

Luego:

- Observa el error  
- Explica con tus palabras por qué ocurre  

---

🟠 **Ejercicio 7 — Transposición**

Crea un array 2D de tamaño `(3, 2)`.

Luego:

- Imprime el array  
- Transpón el array  
- Imprime el nuevo `shape`  

---

🟠 **Ejercicio 8 — Ejes (conceptual)**

Crea un array 2D y responde en un comentario:

- ¿Qué representa `axis=0`?  
- ¿Qué representa `axis=1`?  

*(No operaciones aún, solo comprensión.)*

---

🔵 **Ejercicio 9 — Preparando datos (mentalidad analista)**

Imagina que tienes:

- 10 observaciones  
- 3 variables  

Responde:

- ¿Qué `shape` debería tener el array?  
- ¿Por qué?  

*(No código, solo razonamiento.)*
