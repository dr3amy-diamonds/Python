# 16.7 — EJERCICIOS DE UNIÓN DE ARRAYS (NumPy)

## 🟢 Ejercicio 1 — Unión básica por filas

- Crea dos arrays 2D con el mismo número de columnas.
- Únelos por filas.
- Imprime el array resultante.
- Imprime su `shape`.

---

## 🟢 Ejercicio 2 — Unión básica por columnas

- Crea dos arrays 2D con el mismo número de filas.
- Únelos por columnas.
- Imprime el array resultante.
- Imprime su `shape`.

---

## 🟢 Ejercicio 3 — `concatenate` vs funciones especializadas

- Usa:
  - `concatenate(axis=0)`
  - `vstack`
- Para unir los mismos arrays.
- Verifica que los resultados sean iguales.
- Reflexiona cuál es más legible.

---

## 🟡 Ejercicio 4 — Error por incompatibilidad

- Crea dos arrays con `shape` incompatibles.
- Intenta unirlos.
- Observa el error.
- Escribe un comentario explicando por qué ocurre.

---

## 🟡 Ejercicio 5 — Verificación previa

- Antes de unir dos arrays:
  - Imprime sus `shape`.
  - Decide si es posible unirlos.
- Realiza la unión solo si es válida.

---

## 🟡 Ejercicio 6 — Uso incorrecto de `stack`

- Crea dos arrays iguales.
- Únelos con `stack`.
- Observa el `shape` resultante.
- Explica por qué **NO** es lo mismo que unir filas.

---

## 🟠 Ejercicio 7 — Pensamiento estructural

Dado un array base:

- Decide si necesitas:
  - más filas
  - más columnas
  - una nueva dimensión
- Elige la función correcta.
- Justifica tu decisión en un comentario.

---

## 🟠 Ejercicio 8 — Simulación de dataset

- Simula:
  - un array de datos
  - un array de nuevas observaciones
- Únelos correctamente como si fueran datos reales.

---

## 🔴 Ejercicio 9 — Detección de errores conceptuales

Lee estos objetivos y decide:

- qué función usarías
- por qué las otras no

**Objetivos:**
- agregar variables
- agregar observaciones
- crear un tensor

---

## 🔴 Ejercicio 10 — Autodiagnóstico

Para cada función:

- `concatenate`
- `vstack`
- `hstack`
- `stack`

Escribe:
- qué hace
- cuándo usarla
- qué error evita

---

## 🧠 OBJETIVO FINAL DEL TEMA

✔ Pensar en dimensiones  
✔ Elegir la función correcta  
✔ Evitar errores silenciosos  
✔ Prepararte para división de arrays  
