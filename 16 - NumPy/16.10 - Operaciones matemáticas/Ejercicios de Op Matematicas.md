# 🟩 16.10 — EJERCICIOS: OPERACIONES MATEMÁTICAS (NumPy)

---

## 🟢 Ejercicio 1 — Operaciones básicas elemento a elemento

**Consigna:**  
Crea dos arrays 1D del mismo tamaño con números enteros.

**Debes:**
- Sumar ambos arrays  
- Restarlos  
- Multiplicarlos  
- Dividirlos  

**Imprime:**
- El resultado de cada operación  
- El *shape* final  

---

## 🟢 Ejercicio 2 — Broadcasting con escalar

**Consigna:**  
Crea un array 1D con al menos 6 valores.

**Debes:**
- Sumar un número escalar  
- Multiplicar por otro escalar  

**Condición:**
- No usar bucles  
- Explicar en un comentario qué es *broadcasting*  

---

## 🟢 Ejercicio 3 — Broadcasting 2D con vector

**Consigna:**  
Crea una matriz 2D de tamaño `(3, 4)` y un vector 1D de tamaño `(4,)`.

**Debes:**
- Sumar el vector a la matriz  
- Verificar que la operación funciona sin `reshape`  

---

## 🟡 Ejercicio 4 — Funciones universales (ufuncs)

**Consigna:**  
Crea un array 1D con valores positivos y negativos.

**Debes aplicar:**
- Valor absoluto  
- Raíz cuadrada (solo a los valores positivos)  
- Potencia al cuadrado  

---

## 🟡 Ejercicio 5 — Estadísticas globales

**Consigna:**  
Crea un array 1D con al menos 10 valores.

**Debes calcular:**
- Suma total  
- Media  
- Máximo  
- Mínimo  
- Desviación estándar  

---

## 🟡 Ejercicio 6 — Estadísticas por eje

**Consigna:**  
Crea una matriz 2D de tamaño `(4, 3)`.

**Debes:**
- Calcular la suma por columnas  
- Calcular la media por filas  
- Imprimir los resultados y sus *shapes*  

---

## 🟠 Ejercicio 7 — Operaciones acumulativas

**Consigna:**  
Crea un array 1D que represente valores diarios.

**Debes:**
- Calcular la suma acumulada  
- Calcular el producto acumulado  

**Reflexión (comentario):**
- ¿En qué tipo de análisis usarías esto?  

---

## 🟠 Ejercicio 8 — Comparaciones y filtrado

**Consigna:**  
Crea un array 1D con valores variados.

**Debes:**
- Filtrar los valores mayores que un umbral  
- Filtrar valores dentro de un rango específico  
- Mostrar solo los valores que cumplen la condición  

---

## 🟠 Ejercicio 9 — `np.where()` con lógica

**Consigna:**  
Crea un array 1D con valores numéricos.

**Debes:**
- Duplicar los valores mayores a un umbral  
- Mantener iguales los demás  
- Usar solo `np.where()`  

---

## 🔴 Ejercicio 10 — Operaciones *in-place* vs copia

**Consigna:**  
Crea un array original.

**Debes:**
- Modificarlo usando una operación *in-place*  
- Crear una copia  
- Modificar la copia  
- Verificar que el original no cambia  

---

## 🔴 Ejercicio 11 — Control de valores extremos

**Consigna:**  
Crea un array 1D con valores fuera de un rango razonable.

**Debes:**
- Limitar los valores a un rango específico  
- Verificar que ningún valor lo sobrepasa  

---

## 🔴 Ejercicio 12 — Integrador (nivel análisis real)

**Consigna:**  
Crea un array 2D con valores aleatorios.

**Debes:**
- Escalar los valores  
- Calcular estadísticas por eje  
- Filtrar valores extremos  
- Obtener una versión acumulativa  
- Documentar cada paso con comentarios claros  

---

## 🎯 OBJETIVO FINAL

✔ Pensar vectorialmente  
✔ Dominar *broadcasting*  
✔ Aplicar estadísticas reales  
✔ Evitar bucles  
✔ Escribir código de analista  
