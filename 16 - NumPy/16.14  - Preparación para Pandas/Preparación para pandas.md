# 🟩 16.14 --- PREPARACIÓN PARA PANDAS

## Teoría completa (sin código)

## 🧠 ¿Qué es Pandas y por qué existe?

Pandas es una librería de análisis de datos construida encima de
**NumPy**.

-   👉 No reemplaza NumPy.\
-   👉 Lo extiende para trabajar con datos del mundo real.

### NumPy trabaja bien con:

-   números\
-   arrays homogéneos\
-   cálculos matemáticos

### Pandas trabaja con:

-   tablas\
-   columnas con nombres\
-   datos incompletos\
-   datos mixtos (números, texto, fechas)

------------------------------------------------------------------------

## 🔹 Problema que resuelve Pandas

### Con NumPy:

-   los datos no tienen nombre\
-   todo depende de posiciones\
-   manejar NaN es manual\
-   leer archivos es limitado

### Pandas soluciona:

-   datos etiquetados\
-   selección por nombre\
-   limpieza integrada\
-   lectura de CSV, Excel, SQL

👉 **Pandas no hace magia: organiza NumPy para ti.**

------------------------------------------------------------------------

## 🔹 Cambio de mentalidad clave

### 🧩 En NumPy piensas en:

-   arrays\
-   índices\
-   ejes (axis)\
-   formas (shape)

### 🧩 En Pandas piensas en:

-   filas (registros)\
-   columnas (variables)\
-   índices\
-   operaciones por columna

👉 Todo eso ya lo conoces conceptualmente.

------------------------------------------------------------------------

## 🔹 Relación directa NumPy ↔ Pandas

  NumPy                Pandas
  -------------------- ------------------------
  array 1D             Series
  array 2D             DataFrame
  axis=0               filas
  axis=1               columnas
  NaN manual           NaN integrado
  slicing por índice   selección por etiqueta

👉 Nada nuevo, solo mejor organizado.

------------------------------------------------------------------------

## 🔹 Datos reales NO son perfectos

Pandas existe porque los datos reales: - tienen valores faltantes\
- mezclan tipos\
- vienen desordenados\
- no están listos para analizar

👉 NumPy asume datos limpios\
👉 Pandas asume datos sucios

------------------------------------------------------------------------

## 🔹 Columnas con significado

### En NumPy:

-   la columna 0 "es algo"\
-   la columna 1 "es otra cosa"

### En Pandas:

-   cada columna tiene nombre\
-   cada nombre tiene significado\
-   el código se vuelve legible

👉 Esto reduce errores humanos.

------------------------------------------------------------------------

## 🔹 Índices: la gran diferencia

### En NumPy:

-   índices = posiciones

### En Pandas:

-   índices = identificadores

Un índice puede ser: - número\
- fecha\
- texto

👉 No es solo "contar filas", es **identificar registros**.

------------------------------------------------------------------------

## 🔹 Manejo de NaN (clave absoluta)

En Pandas: - NaN es ciudadano de primera clase\
- casi todas las funciones lo ignoran correctamente

Puedes: - eliminarlos\
- rellenarlos\
- analizarlos

👉 Todo lo que sufriste con NaN en NumPy... aquí está resuelto.

------------------------------------------------------------------------

## 🔹 Operaciones por columna (lo más usado)

En análisis real: - no operas "por posición"\
- operas "por variable"

Pandas está diseñado para: - estadísticas por columna\
- transformaciones por columna\
- filtros por condición

👉 Encaja perfecto con lo que ya aprendiste de **axis**.

------------------------------------------------------------------------

## 🔹 Lectura y escritura de datos

Pandas facilita: - CSV\
- Excel\
- JSON\
- bases de datos

👉 Aquí empieza el análisis real, no solo ejercicios.

------------------------------------------------------------------------

## 🔹 Rendimiento: NumPy sigue siendo el motor

-   Pandas usa NumPy internamente\
-   hereda su velocidad\
-   añade seguridad y claridad

👉 Saber NumPy bien te hace mejor usuario de Pandas.

------------------------------------------------------------------------

## 🔹 Errores comunes al empezar Pandas

❌ Pensar que Pandas reemplaza NumPy\
❌ Ignorar axis\
❌ No entender índices\
❌ Tratar DataFrames como listas\
❌ Copiar código sin entender

------------------------------------------------------------------------

## 🔹 Buenas prácticas desde el inicio

✔ Pensar en datos como tablas\
✔ Nombrar columnas con sentido\
✔ Validar datos antes de analizar\
✔ Limpiar antes de calcular\
✔ Comentar decisiones de limpieza

------------------------------------------------------------------------

## 🔹 Qué NO es Pandas

❌ No es base de datos\
❌ No es machine learning\
❌ No es visualización\
❌ No es magia

👉 Es la base para todo eso.

------------------------------------------------------------------------

## 🧭 Cuándo usar NumPy y cuándo Pandas

### Usa NumPy cuando:

-   necesitas cálculo matemático puro\
-   trabajas con matrices\
-   performance crítica

### Usa Pandas cuando:

-   tienes tablas\
-   analizas datos reales\
-   lees archivos\
-   limpias datos

👉 En la práctica: **usas ambos juntos**.

------------------------------------------------------------------------

## 🎯 Qué te permite hacer Pandas (a futuro)

-   análisis exploratorio\
-   dashboards\
-   machine learning\
-   ciencia de datos\
-   análisis financiero\
-   análisis académico

------------------------------------------------------------------------

## 🧠 Idea final (muy importante)

**Pandas no es un salto,\
es una consecuencia natural de lo que ya sabes.**

👉 Si NumPy te hace sentido → Pandas te va a gustar.

------------------------------------------------------------------------

## ✅ Estado actual

Con **16.14**: - NumPy queda cerrado\
- tu base es sólida\
- estás listo para Pandas sin miedo
