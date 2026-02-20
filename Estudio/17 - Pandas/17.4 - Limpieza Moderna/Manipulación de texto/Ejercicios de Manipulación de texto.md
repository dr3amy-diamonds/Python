# 📘 Ejercicios de Manipulación de Texto en Pandas

------------------------------------------------------------------------

## 🟢 Ejercicio 1: Limpieza de Nombres (Reemplazo y Formato)

### 🎯 Contexto Real

Necesitamos personalizar los correos (ejemplo: "Hola Juan...").

Problemas detectados en la columna `nombre_cliente`:

-   Los nombres tienen puntos (.) o guiones (-) en lugar de espacios.
-   Hay mayúsculas y minúsculas mezcladas.
-   Hay espacios basura al inicio y al final.

### 🧠 Tu Misión

1.  Crea `df_limpio` como una copia usando `.copy()`.
2.  En la columna `nombre_cliente`:
    -   Reemplaza los puntos `.` y guiones `-` por espacios vacíos.
    -   Elimina los espacios extra de los extremos.
    -   Pon el texto en formato Título.
3.  Imprime la columna arreglada.

------------------------------------------------------------------------

## 🟡 Ejercicio 2: Georreferenciación (Split & Expand)

### 🎯 Contexto Real

La columna `ubicacion` tiene la Ciudad y la Dirección pegadas con una
barra `|`.

El equipo de logística necesita la ciudad en una columna aparte para
asignar los vendedores.

### 🧠 Tu Misión

1.  Divide la columna `ubicacion` usando el separador `|`.
    -   Usa `expand=True` para crear columnas nuevas.
2.  Guarda:
    -   La primera parte en una columna nueva llamada `ciudad`.
    -   La segunda parte en una columna llamada `direccion`.
3.  **Reto Extra:**
    -   Es probable que queden espacios como `" Bogota "`.
    -   Aplica limpieza para eliminar espacios innecesarios en ambas
        columnas nuevas.

------------------------------------------------------------------------

## 🟠 Ejercicio 3: Extracción de Año (Slicing)

### 🎯 Contexto Real

La columna `id_campaña` tiene el código, el año y la temporada.

Finanzas necesita saber de qué año es cada lead para calcular el
presupuesto.

El año siempre está entre el carácter 5 y el 9 (ejemplo: 2024).

### 🧠 Tu Misión

1.  Normaliza `id_campaña`:
    -   Convierte todo a mayúsculas.
    -   Elimina espacios innecesarios.
2.  Crea una nueva columna llamada `año_campaña` extrayendo únicamente
    los números del año.
3.  Muestra el ID original y el año extraído.

------------------------------------------------------------------------

## 🔴 Ejercicio 4: Filtrado B2B (Contains + Lógica)

### 🎯 Contexto Real

Queremos separar a los clientes corporativos (B2B) de los personales.

Reglas:

-   Si el correo es `gmail` o `hotmail`, es personal.
-   Si es otro dominio (por ejemplo: empresa.net, tech-corp.com), es
    corporativo.

### 🧠 Tu Misión

1.  Crea una columna bandera llamada `es_correo_personal`.
2.  Detecta si el correo contiene:
    -   `gmail` o `hotmail`.
    -   Asegúrate de que la búsqueda no distinga mayúsculas y
        minúsculas.
3.  Imprime los correos y la bandera `True/False`.

------------------------------------------------------------------------

# ✅ Objetivo General

Practicar técnicas profesionales de manipulación de texto:

-   Reemplazo y normalización
-   División de columnas
-   Extracción por slicing
-   Filtrado por patrones
-   Creación de columnas bandera

⚠️ Importante: No resolver los ejercicios directamente. El objetivo es
practicar.
