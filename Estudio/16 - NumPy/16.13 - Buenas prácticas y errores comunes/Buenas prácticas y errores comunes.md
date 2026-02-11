# 16.13 --- BUENAS PRÁCTICAS Y ERRORES COMUNES EN NUMPY

## 🧠 ¿Por qué este tema es tan importante?

Porque NumPy no suele fallar con errores visibles, sino con:

-   resultados incorrectos\
-   datos modificados sin querer\
-   cálculos mal hechos pero "válidos"

👉 Este tema no es opcional si quieres análisis de datos serio,
portafolio o trabajo real.

------------------------------------------------------------------------

## 🔹 1. Entender SIEMPRE la forma de los datos (shape)

### ❌ Error común

Trabajar sin saber si el array es: - (n,)\
- (n,1)\
- (1,n)\
- (n,m)

### ✅ Buena práctica

Antes de operar: - revisar `shape` - revisar `ndim`

👉 El 80% de los errores en NumPy vienen de aquí.

------------------------------------------------------------------------

## 🔹 2. Confundir vistas y copias

### ❌ Error común

Modificar un array pensando que es independiente.

### ✅ Buena práctica

-   Usar `.copy()` si vas a modificar\
-   Usar vistas solo para lectura o rendimiento

👉 Regla de oro:\
**Si dudas → copy()**

------------------------------------------------------------------------

## 🔹 3. No especificar axis

### ❌ Error común

Usar funciones estadísticas sin pensar en el eje.

### ✅ Buena práctica

-   `axis=0` → opera por columnas\
-   `axis=1` → opera por filas

👉 NumPy no adivina tu intención.

------------------------------------------------------------------------

## 🔹 4. Usar bucles de Python en lugar de operaciones vectorizadas

### ❌ Error común

Usar `for` para operaciones matemáticas.

### ✅ Buena práctica

-   Usar operaciones vectorizadas\
-   Aprovechar broadcasting

👉 Es: - más rápido\
- más claro\
- más profesional

------------------------------------------------------------------------

## 🔹 5. Ignorar valores NaN

### ❌ Error común

Calcular estadísticas sin revisar NaN.

### ✅ Buena práctica

-   Usar funciones `nan*`\
-   Limpiar o imputar antes de analizar

👉 NaN puede arruinar todo un análisis.

------------------------------------------------------------------------

## 🔹 6. No controlar el tipo de dato (dtype)

### ❌ Error común

Mezclar enteros, floats y strings sin revisar.

### ✅ Buena práctica

-   Revisar `dtype`\
-   Convertir cuando sea necesario

👉 El tipo afecta: - precisión\
- memoria\
- resultados

------------------------------------------------------------------------

## 🔹 7. Usar reshape sin validar tamaño

### ❌ Error común

Forzar `reshape()` sin pensar en `size`.

### ✅ Buena práctica

-   Verificar que el número total de elementos coincida\
-   Usar `-1` solo cuando tenga sentido

------------------------------------------------------------------------

## 🔹 8. Comparaciones mal hechas con arrays

### ❌ Error común

Usar `and`, `or`, `if` directamente con arrays.

### ✅ Buena práctica

-   Usar operadores vectorizados\
-   Usar funciones como `any()` o `all()`

👉 NumPy no funciona como listas normales.

------------------------------------------------------------------------

## 🔹 9. Usar nombres poco claros

### ❌ Error común

Variables genéricas (`a`, `x`, `temp`).

### ✅ Buena práctica

-   Usar nombres que representen datos reales\
-   Facilita lectura y depuración

------------------------------------------------------------------------

## 🔹 10. No documentar transformaciones

### ❌ Error común

Aplicar muchas operaciones sin comentarios.

### ✅ Buena práctica

-   Comentar **por qué**, no solo **qué**\
-   Pensar en "yo dentro de 3 meses"

------------------------------------------------------------------------

## 🔹 11. Optimización prematura

### ❌ Error común

Intentar hacer el código "ultra eficiente" desde el inicio.

### ✅ Buena práctica

1.  Que funcione\
2.  Que sea claro\
3.  Luego optimizar

------------------------------------------------------------------------

## 🔹 12. No validar resultados

### ❌ Error común

Confiar ciegamente en el output.

### ✅ Buena práctica

-   Comprobar valores esperados\
-   Imprimir resultados intermedios\
-   Usar estadísticas básicas como verificación

------------------------------------------------------------------------

## 🚨 ERRORES CRÍTICOS A EVITAR SÍ O SÍ

-   ❌ Modificar datos originales sin copia\
-   ❌ Mezclar shapes incompatibles\
-   ❌ Ignorar NaN\
-   ❌ No entender axis\
-   ❌ Usar loops innecesarios\
-   ❌ No revisar dtype

------------------------------------------------------------------------

## 🧭 MENTALIDAD CORRECTA CON NUMPY

✔ Los datos tienen forma\
✔ La forma importa tanto como los valores\
✔ Las operaciones deben ser explícitas\
✔ La claridad es más importante que la velocidad\
✔ Si algo "funciona raro", revisa `shape`, `dtype`, `axis`

------------------------------------------------------------------------

## 🎯 RESUMEN FINAL

Este tema: - no se memoriza\
- se interioriza\
- te evita errores silenciosos\
- te separa de principiantes

👉 Dominar esto es lo que te hace **intermedio real**.
