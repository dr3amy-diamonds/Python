# 🟩 16.4 — SHAPE, DIMENSIONES Y RESHAPE (NumPy)

## 🧠 ¿Por qué este tema es clave?

En análisis de datos los valores no lo son todo.  
La forma en la que los datos están organizados es igual de importante.

Un mismo conjunto de datos puede representarse como:
- una fila
- una columna
- una matriz
- un tensor

Cada forma sirve para un propósito distinto.

---

## 🔹 ¿Qué es `shape`?

`shape` describe la **forma del array**.

Indica:
- cuántos ejes tiene
- cuántos elementos hay en cada eje

Ejemplos:
- `(5,)` → vector de 5 elementos
- `(3, 4)` → 3 filas, 4 columnas
- `(2, 3, 4)` → array de 3 dimensiones

👉 `shape` es el mapa mental del array.

---

## 🔹 Dimensiones (`ndim`)

Una dimensión es un **eje de datos**.

- 1D → lista de valores  
- 2D → tabla (filas y columnas)  
- 3D → conjunto de tablas  

En análisis de datos:
- filas = observaciones
- columnas = variables

`ndim` indica cuántas dimensiones tiene el array.

---

## 🔹 `size` — cantidad total de elementos

`size` indica cuántos valores hay en total, sin importar la forma.

Ejemplo:
- `(2, 3)` → size = 6  
- `(6,)` → size = 6  

👉 Los datos no cambian, solo la forma.

---

## 🔹 `reshape()`

`reshape()` cambia la forma del array **sin cambiar los datos**.

Conceptualmente:
- reorganiza
- redistribuye
- no crea valores nuevos

### ⚠️ Regla de oro
El número total de elementos debe coincidir.

Si no:
❌ error

### 🔹 Uso de `-1`

```python
arr.reshape(2, -1)
```

NumPy calcula automáticamente el tamaño faltante.

---

## 🔹 Ejes (`axis`)

En un array 2D con shape `(filas, columnas)`:

- `axis=0` → trabaja por columnas  
- `axis=1` → trabaja por filas  

👉 Muchos errores vienen de confundir los ejes.

---

## 🔹 Diferencia crítica: `(n,)`, `(n,1)` y `(1,n)`

| Shape | Descripción | Uso típico |
|------|-------------|-----------|
| `(n,)` | Vector 1D | cálculos simples |
| `(n,1)` | Columna | machine learning |
| `(1,n)` | Fila | álgebra lineal |

⚠️ Aunque tengan los mismos datos, no se comportan igual.

---

## 🔹 `flatten()` vs `ravel()`

Ambos convierten un array multidimensional en 1D.

- `flatten()` → devuelve una copia  
- `ravel()` → devuelve una vista  

👉 `ravel()` es más eficiente, pero puede modificar el original.

---

## 🔹 `view` vs `copy` (concepto importante)

Algunas operaciones:
- devuelven vistas
- otras crean copias

| Operación | Resultado |
|---------|-----------|
| slicing | vista |
| ravel | vista |
| flatten | copia |
| reshape | vista o copia |

👉 Entender esto evita bugs silenciosos.

---

## 🔹 `transpose()`

`transpose()` intercambia ejes del array.

- `.T` → atajo para arrays 2D  
- `transpose()` → control total en arrays ND  

Fundamental para:
- matrices
- álgebra lineal
- machine learning

---

## 🚨 Errores comunes

❌ Confundir `(n,)` con `(n,1)`  
❌ No revisar `shape` antes de operar  
❌ `reshape` incompatible  
❌ No entender qué eje se modifica  

---

## 🧭 Resumen mental

✔ `shape` → mapa del array  
✔ `ndim` → profundidad  
✔ `size` → cantidad total  
✔ `reshape()` → reorganiza  
✔ Los datos no cambian, la forma sí  

---

## 🧠 Idea clave final

Dominar la forma de los datos es obligatorio para avanzar en:

- análisis de datos
- visualización
- machine learning
- deep learning
