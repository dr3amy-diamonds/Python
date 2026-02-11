# 🟩 16.10 --- Operaciones Matemáticas en NumPy

## 🧠 ¿Por qué este tema es crítico?

NumPy **no existe para almacenar datos**.\
Existe para **operar matemáticamente sobre ellos de forma eficiente**.

Todo lo que viene después depende de esto:

-   Pandas\
-   Machine Learning\
-   Deep Learning

Si dominas este tema:

-   escribes menos código\
-   evitas bucles\
-   procesas millones de datos rápido\
-   piensas vectorialmente

------------------------------------------------------------------------

## 🔹 ¿Qué son las operaciones matemáticas en NumPy?

Son operaciones que:

-   se aplican **elemento a elemento**
-   funcionan sobre **arrays completos**
-   aprovechan código interno en **C** (alta velocidad)

Este enfoque se llama:

### 👉 **Vectorización**

------------------------------------------------------------------------

## 🔹 Operaciones aritméticas básicas

### Concepto

NumPy permite:

-   sumar\
-   restar\
-   multiplicar\
-   dividir

arrays **directamente**, sin recorrerlos con bucles.

### Regla clave

Los arrays deben ser:

-   del mismo tamaño\
-   **o compatibles mediante broadcasting**

------------------------------------------------------------------------

## 🔹 Broadcasting (idea central)

### Concepto

Capacidad de NumPy para:

-   "expandir" arrays pequeños\
-   y operar con arrays grandes

📌 **Broadcasting no copia datos**, solo adapta la forma.

### Importancia

✔ Código elegante\
✔ Menor uso de memoria\
✔ Mayor claridad

### Error común

❌ No entender por qué una operación falla\
❌ Forzar `reshape` sin pensar

------------------------------------------------------------------------

## 🔹 Operaciones elemento a elemento

Todas las operaciones matemáticas en NumPy:

-   se aplican **valor por valor**
-   no por filas o columnas (a menos que se indique)

Ejemplos conceptuales:

-   suma → cada elemento se suma con su par\
-   multiplicación → cada elemento se multiplica con su par

------------------------------------------------------------------------

## 🔹 Funciones universales (ufuncs)

### Concepto

Funciones matemáticas optimizadas para arrays.

Ejemplos conceptuales:

-   raíz cuadrada\
-   logaritmos\
-   exponenciales\
-   valores absolutos\
-   redondeo

📌 Son:

-   rápidas\
-   vectorizadas\
-   numéricamente estables

------------------------------------------------------------------------

## 🔹 Operaciones de reducción

### Concepto

Reducen un array a:

-   un solo valor\
-   o un array de menor dimensión

Ejemplos:

-   suma total\
-   promedio\
-   máximo\
-   mínimo\
-   desviación estándar

### Uso real

-   análisis estadístico\
-   métricas\
-   agregaciones

------------------------------------------------------------------------

## 🔹 Operaciones acumulativas

### Concepto

Muestran la evolución del cálculo.

Ejemplos conceptuales:

-   suma acumulada\
-   producto acumulado

📌 Útil para:

-   análisis temporal\
-   crecimiento\
-   tendencias

------------------------------------------------------------------------

## 🔹 Operaciones con ejes (`axis`)

### Concepto

Permiten elegir:

-   cómo se agrupan los cálculos\
-   por filas o por columnas

📌 Fundamental en matrices.

### Error común

❌ Confundir el eje con la orientación visual

------------------------------------------------------------------------

## 🔹 Comparaciones y lógica

### Concepto

NumPy permite:

-   comparaciones vectorizadas\
-   operaciones lógicas\
-   filtros complejos

📌 Devuelven **arrays booleanos**.

### Uso real

-   limpieza de datos\
-   filtrado\
-   validación

------------------------------------------------------------------------

## 🔹 Operaciones in-place

### Concepto

Operaciones que:

-   modifican el array original\
-   no crean copias

Ejemplos conceptuales:

-   `+=`\
-   `*=`

### Ventaja

✔ Ahorro de memoria

### Riesgo

❌ Pérdida de datos originales

------------------------------------------------------------------------

## 🚨 Errores comunes

-   ❌ Usar bucles `for`\
-   ❌ Operar arrays incompatibles\
-   ❌ Ignorar broadcasting\
-   ❌ Modificar arrays sin copia\
-   ❌ Confundir operaciones por eje

------------------------------------------------------------------------

## 🧠 Buenas prácticas

-   ✔ Piensa vectorialmente\
-   ✔ Revisa `shape` antes de operar\
-   ✔ Usa `axis` conscientemente\
-   ✔ Prefiere ufuncs\
-   ✔ Usa copias cuando sea necesario

------------------------------------------------------------------------

## 🧭 Resumen mental

  Necesidad          Solución
  ------------------ ----------------------
  Cálculos rápidos   Vectorización
  Operar arrays      Operaciones directas
  Escalar valores    Broadcasting
  Estadística        Reducciones
  Tendencias         Acumulativos
  Filtrar            Comparaciones

------------------------------------------------------------------------

## 🎯 Idea clave final

**NumPy no es Python con números.**\
Es **matemática vectorizada a gran escala**.
