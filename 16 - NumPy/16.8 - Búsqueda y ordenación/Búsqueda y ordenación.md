# 🟩 16.8 — BÚSQUEDA Y ORDENACIÓN DE ARRAYS (NumPy)

## 🧠 ¿POR QUÉ ESTE TEMA ES TAN IMPORTANTE?

En análisis de datos no basta con tener datos, necesitas:

- encontrar valores relevantes  
- ordenar información  
- filtrar resultados  
- preparar datos para modelos  
- optimizar rendimiento  

📌 **El 80% del análisis real es búsqueda + ordenación + filtrado.**

Si no dominas esto:

- tu código será lento  
- cometerás errores lógicos  
- tus resultados serán incorrectos  

---

## 🧭 ¿QUÉ PROBLEMAS RESUELVE ESTE TEMA?

Con búsqueda y ordenación puedes:

- encontrar máximos, mínimos y posiciones  
- ordenar datos por prioridad  
- detectar *outliers*  
- preparar rankings  
- filtrar datos según condiciones  
- acelerar cálculos posteriores  

---

## 🔹 BÚSQUEDA EN NUMPY

### 🔹 1. Búsqueda lógica (booleana)

**Concepto**  
NumPy permite buscar usando **condiciones**, no bucles.

En vez de:
- revisar elemento por elemento  

Usas:
- expresiones vectorizadas  

**¿Qué devuelve?**
- arrays booleanos  
- índices  
- valores filtrados  

**Ventajas**
- ✔ Muy rápida  
- ✔ Muy clara  
- ✔ Escala bien con millones de datos  

**Mala práctica**
- ❌ Usar `for` para buscar condiciones  
- ❌ Convertir a listas para filtrar  

---

### 🔹 2. `where` — búsqueda condicional

**Concepto**  
Permite:
- encontrar posiciones  
- seleccionar valores  
- reemplazar valores según condición  

Es más flexible que una condición simple.

**Uso típico**
- localizar datos problemáticos  
- aplicar reglas condicionales  
- limpieza de datos  

**Buenas prácticas**
- ✔ Usar cuando necesitas posiciones  
- ✔ Usar para reemplazos masivos  

**Mala práctica**
- ❌ Usarlo cuando solo necesitas un booleano simple  

---

### 🔹 3. `argmax` / `argmin`

**Concepto**  
No devuelve el valor, devuelve **la posición** del máximo o mínimo.

**Importancia**
En análisis de datos:
- la posición importa más que el valor  
- necesitas saber *dónde* ocurre algo  

**Buen uso**
- ✔ Identificar picos  
- ✔ Detectar registros extremos  

**Error común**
- ❌ Pensar que devuelve el valor  
- ❌ No considerar el eje (`axis`)  

---

### 🔹 4. `nonzero`

**Concepto**  
Encuentra índices donde la condición es verdadera.

**Uso real**
- detección de valores válidos  
- filtrado por presencia  
- análisis binario  

---

### 🔹 5. `isin`

**Concepto**  
Busca si los valores de un array pertenecen a otro.

**Uso típico**
- filtros por categorías  
- validación de datos  
- cruces simples de datasets  

---

## 🔸 ORDENACIÓN EN NUMPY

### 🧠 ¿POR QUÉ ORDENAR DATOS?

Ordenar no es solo estética. Sirve para:

- rankings  
- percentiles  
- detección de tendencias  
- preparación para búsqueda binaria  
- análisis estadístico  

---

### 🔹 6. `sort` — ordenación directa

**Concepto**  
Ordena los valores de un array.

**Importante**
- Devuelve una copia  
- No modifica el original (por defecto)  

**Buen uso**
- ✔ Cuando no necesitas conservar el orden original  

**Mala práctica**
- ❌ Ordenar grandes arrays innecesariamente  

---

### 🔹 7. `argsort` — ordenación por índices

**Concepto**  
Devuelve los índices que ordenarían el array.

**Por qué es poderoso**
Permite:
- ordenar múltiples arrays con el mismo criterio  
- mantener relación entre datos  

📌 **Una de las herramientas más importantes en análisis real.**

---

### 🔹 8. Ordenación por eje (`axis`)

**Concepto**  
Puedes ordenar:
- por filas  
- por columnas  

**Importancia**
En tablas:
- ordenar registros  
- ordenar variables  

**Error común**
- ❌ Confundir `axis=0` y `axis=1`  

---

### 🔹 9. Métodos de ordenación (eficiencia)

NumPy usa algoritmos distintos internamente.

**🔻 mergesort**
- estable  
- más lento  
- útil cuando el orden previo importa  

**⚖️ heapsort**
- consumo de memoria predecible  
- no estable  

**🔺 quicksort (por defecto)**
- muy rápido  
- no estable  
- ideal para la mayoría de casos  

📌 En análisis de datos: **rapidez > estabilidad** (casi siempre)

---

### 🔹 10. Ordenación parcial

**Concepto**  
No siempre necesitas ordenar todo.

A veces solo:
- top 5  
- valores más grandes  
- valores más pequeños  

NumPy permite ordenación parcial, mucho más rápida.

**Buen uso**
- ✔ Rankings  
- ✔ Detección de extremos  

---

## 🚨 ERRORES COMUNES

- ❌ Usar bucles para buscar  
- ❌ Ordenar sin necesidad  
- ❌ No revisar `axis`  
- ❌ Perder relación entre arrays  
- ❌ Confundir valor vs índice  
- ❌ Modificar datos originales sin querer  

---

## 🧠 BUENAS PRÁCTICAS PROFESIONALES

- ✔ Piensa si necesitas índices o valores  
- ✔ Usa búsqueda vectorizada  
- ✔ Usa `argsort` con múltiples arrays  
- ✔ Ordena solo cuando sea necesario  
- ✔ Prefiere NumPy a Python puro  

---

## 🧭 RESUMEN MENTAL

| Necesidad | Herramienta |
|---------|------------|
| Buscar condición | Máscaras booleanas |
| Buscar posiciones | `where`, `nonzero` |
| Máximo / mínimo | `argmax`, `argmin` |
| Cruces | `isin` |
| Ordenar valores | `sort` |
| Ordenar por relación | `argsort` |
| Optimizar | Ordenación parcial |

---

## 🎯 IDEA CLAVE FINAL

**Buscar y ordenar bien es pensar bien los datos.**  
Un analista que domina esto escribe menos código, más rápido y con menos errores.
