# 🧹 Taller de Limpieza y Optimización de Datos en Pandas

Este documento contiene una serie de ejercicios prácticos enfocados en
la limpieza, transformación y optimización de datos dentro de un
DataFrame de Recursos Humanos.

------------------------------------------------------------------------

## 🟢 Ejercicio 1: Limpieza Financiera (Strings a Floats)

### 📌 Contexto

La columna `salario_mensual` contiene símbolos como `$`, `€` y comas
`,`.\
Mientras el dato esté en formato texto, no es posible realizar cálculos
matemáticos correctamente.

### 🎯 Tu misión

1.  Convertir la columna a tipo **string**.
2.  Eliminar:
    -   El símbolo `$`
    -   El símbolo `€`
    -   Las comas `,`
3.  Convertir el resultado limpio a números decimales (**float**).
4.  Imprimir la suma total de los salarios para verificar que la
    conversión fue exitosa.

------------------------------------------------------------------------

## 🟡 Ejercicio 2: El Calendario Corporativo (Fechas Mixtas)

### 📌 Contexto

La columna `fecha_ingreso` contiene fechas en diferentes formatos: - Con
barras - Con guiones - Con nombres de mes

Esto impide calcular correctamente la antigüedad de los empleados.

### 🎯 Tu misión

1.  Convertir la columna al tipo fecha usando la función adecuada.
2.  Configuración clave:
    -   Activar `dayfirst=True`
    -   Usar `format='mixed'` para soportar múltiples formatos
3.  Verificar el resultado revisando los tipos de datos del DataFrame.

------------------------------------------------------------------------

## 🟠 Ejercicio 3: Optimización Categórica (Ahorro de RAM)

### 📌 Contexto

La columna `departamento` contiene valores repetidos como: - Ventas -
Finanzas - IT

En bases de datos grandes, repetir miles de veces la misma palabra
desperdicia memoria.

### 🎯 Tu misión

1.  Convertir la columna `departamento` al tipo **category**.
2.  Comprender el cambio:
    -   Antes: Se almacenaban strings completos repetidos.
    -   Ahora: Se almacenan pequeños identificadores numéricos que
        apuntan a etiquetas únicas.

------------------------------------------------------------------------

## 🔴 Ejercicio 4: Banderas Booleanas (Lógica Binaria)

### 📌 Contexto

La columna `bono_anual` contiene los valores: - "Si" - "No"

Para una bandera lógica, usar texto es ineficiente.

### 🎯 Tu misión

1.  Crear un diccionario llamado `mapa_bono` donde:
    -   `'Si'` → `True`
    -   `'No'` → `False`
2.  Aplicar el mapeo a la columna.
3.  Convertir inmediatamente el resultado al tipo booleano.
4.  Verificar que ahora la columna muestre únicamente `True` y `False`.

------------------------------------------------------------------------

## 🟣 Ejercicio 5: IDs Perdidos (Modern Pandas Int64)

### 📌 Contexto

La columna `id_empleado` contiene un valor faltante (`NaN`).

Problemas comunes: - Convertir a `int` tradicional genera error. -
Permitir que Pandas decida lo convierte en `float`, lo cual añade
decimales innecesarios para un ID.

### 🎯 Tu misión

1.  Convertir la columna utilizando el tipo moderno `Int64` (con I
    mayúscula).
2.  Verificar que:
    -   Los IDs no tengan punto decimal.
    -   Los valores faltantes aparezcan como `<NA>`.

------------------------------------------------------------------------

## 🦁 Ejercicio 6: Downcasting (Micro-Optimización)

### 📌 Contexto

La columna `edad` contiene valores como: - 34 - 28 - 45

Por defecto, Pandas usa `int64`, capaz de almacenar números
extremadamente grandes.

Para edades humanas, ese rango es innecesario.

### 🎯 Tu misión

1.  Convertir la columna `edad` a `int8`.
2.  Ejecutar un resumen de información del DataFrame para observar:
    -   Los nuevos tipos de datos.
    -   La reducción en el uso de memoria.
3.  Analizar mentalmente la mejora obtenida.

------------------------------------------------------------------------

# 🧠 Objetivo General del Taller

Este conjunto de ejercicios busca que comprendas:

-   Conversión correcta de tipos de datos
-   Limpieza estructural de información
-   Manejo moderno de valores nulos
-   Optimización de memoria
-   Buenas prácticas en manipulación de datos con Pandas

------------------------------------------------------------------------

📘 En ciencia de datos, limpiar y optimizar no es un paso secundario...\
es la base sobre la cual todo análisis serio se construye.
