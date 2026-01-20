# 🟩 16.9 --- GENERACIÓN DE NÚMEROS ALEATORIOS (NumPy)

## 🧠 ¿POR QUÉ ES IMPORTANTE `numpy.random`?

En análisis de datos lo aleatorio no es caos, es una herramienta.

Se usa para:

-   simulaciones\
-   muestreo\
-   pruebas estadísticas\
-   generación de datasets\
-   validación de modelos\
-   machine learning\
-   experimentos reproducibles

📌 **Sin números aleatorios no hay ciencia de datos moderna.**

------------------------------------------------------------------------

## 🔹 ¿QUÉ ES `numpy.random`?

Es el módulo de NumPy que permite:

-   generar números pseudoaleatorios\
-   trabajar con distribuciones estadísticas\
-   controlar la aleatoriedad\
-   reproducir resultados

👉 No es "azar puro", es **azar controlado**.

------------------------------------------------------------------------

## 🧠 Pseudoaleatoriedad (concepto clave)

Los números generados:

-   parecen aleatorios\
-   siguen algoritmos deterministas\
-   pueden reproducirse

Esto es fundamental para:

-   depuración\
-   investigación\
-   machine learning\
-   ciencia

------------------------------------------------------------------------

## 🔹 SEMILLA (`seed`)

### Concepto

La semilla define el punto inicial del generador aleatorio.

Si usas la misma semilla:

-   obtienes los mismos números\
-   siempre

### Importancia

✔ Reproducibilidad\
✔ Comparar experimentos\
✔ Debugging

### Mala práctica

❌ No fijar semilla en experimentos científicos\
❌ Cambiar semilla sin control

------------------------------------------------------------------------

## 🔹 GENERACIÓN DE NÚMEROS ALEATORIOS

### 🔹 Números uniformes

Valores distribuidos:

-   de forma uniforme\
-   todos tienen la misma probabilidad

Uso típico:

-   simulaciones simples\
-   pruebas de rendimiento\
-   valores base

------------------------------------------------------------------------

### 🔹 Números enteros aleatorios

Permite generar:

-   IDs\
-   índices\
-   selecciones aleatorias\
-   simulaciones discretas

Uso real:

-   muestreo\
-   partición de datos\
-   simulación de eventos

------------------------------------------------------------------------

### 🔹 Distribución normal (gaussiana)

Muy importante en análisis de datos.

Características:

-   media\
-   desviación estándar\
-   forma de campana

Uso real:

-   errores experimentales\
-   fenómenos naturales\
-   machine learning\
-   estadística

📌 **La mayoría de datos reales tienden a una normal.**

------------------------------------------------------------------------

## 🔹 Otras distribuciones importantes

-   **binomial** → éxito / fracaso\
-   **poisson** → eventos por intervalo\
-   **exponencial** → tiempos entre eventos

👉 No necesitas dominarlas todas ahora, pero sí entender que existen.

------------------------------------------------------------------------

## 🔹 MUESTREO ALEATORIO

### Concepto

Seleccionar elementos al azar de un conjunto.

Permite:

-   seleccionar datos\
-   crear conjuntos de entrenamiento\
-   bootstrap\
-   validación cruzada

------------------------------------------------------------------------

## 🔹 SHUFFLE vs PERMUTATION

### Shuffle

-   mezcla el array\
-   modifica el original

### Permutation

-   devuelve una copia mezclada\
-   no modifica el original

📌 Esto conecta con **copia vs vista**.

------------------------------------------------------------------------

## 🔹 GENERADORES MODERNOS (`default_rng`)

NumPy moderno recomienda:

-   usar generadores explícitos\
-   no usar funciones globales antiguas

### Ventajas

✔ mejor calidad aleatoria\
✔ más control\
✔ código más profesional

------------------------------------------------------------------------

## 🚨 ERRORES COMUNES

❌ Pensar que random = impredecible\
❌ No fijar semilla\
❌ Usar random sin entender la distribución\
❌ Modificar datos originales sin querer\
❌ Mezclar métodos antiguos y modernos

------------------------------------------------------------------------

## 🧠 BUENAS PRÁCTICAS

✔ Fija semilla en análisis y ML\
✔ Usa distribuciones correctas\
✔ Prefiere generadores modernos\
✔ Documenta la aleatoriedad\
✔ No abuses del azar

------------------------------------------------------------------------

## 🧭 RESUMEN MENTAL

  Necesidad               Herramienta
  ----------------------- -----------------------
  Reproducir resultados   seed
  Uniforme                random uniforme
  Enteros                 random enteros
  Normal                  distribución normal
  Muestreo                choice
  Mezclar datos           shuffle / permutation
  Código moderno          default_rng

------------------------------------------------------------------------

## 🎯 IDEA CLAVE FINAL

**Lo aleatorio en ciencia de datos no es suerte: es control.**\
Dominar `numpy.random` te acerca mucho al nivel profesional.
