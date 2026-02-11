# Tipos de Datos en Pandas (dtypes)

## 1. Definición y Fundamentos Teóricos

En Python estándar (listas), el manejo de tipos es dinámico: una misma
lista puede contener un entero, un texto y un booleano:

`[1, "Hola", True]`

Esto es flexible, pero computacionalmente costoso y lento.

En **Pandas (y NumPy)**, el manejo de tipos es **estricto y homogéneo
por columna**. Cada **Serie** (o columna de un DataFrame) tiene asignado
un **dtype (Data Type)** específico.\
Esto significa que Pandas reserva un espacio de memoria exacto para cada
elemento, asumiendo que todos son del mismo tipo.

👉 **Concepto clave:**\
Un *dtype* es la metadata que le indica a la computadora cómo
interpretar los bytes almacenados\
(¿es un número?, ¿es texto?, ¿es una fecha?).

------------------------------------------------------------------------

## 2. Catálogo de Tipos (Taxonomía)

El analista debe dominar los siguientes tipos fundamentales para
optimizar memoria y evitar errores lógicos.

### A. Numéricos (El motor de cálculo)

-   **int64 (Enteros)**\
    Números sin decimales.\
    Usados para conteos, identificadores, edades.

    Existen variantes como `int8`, `int16`, `int32` para ahorrar memoria
    según el rango del número.

-   **float64 (Flotantes)**\
    Números con decimales.\
    Estándar para cálculos científicos, precios, promedios.

    **Nota crítica:**\
    Si una columna de enteros contiene al menos un valor nulo (`NaN`),
    Pandas la convertirá automáticamente a `float`, ya que los enteros
    nativos no soportan valores nulos.

------------------------------------------------------------------------

### B. Texto y Mixtos

-   **object (Objeto)**\
    Tipo comodín usado para:
    -   Texto (strings)
    -   Columnas con datos mezclados (números + letras)

    **Desventajas:**
    -   Es el tipo más lento.
    -   Consume más memoria RAM.
    -   Usa punteros a objetos de Python en lugar de memoria contigua.

------------------------------------------------------------------------

### C. Lógicos y Temporales

-   **bool (Booleano)**\
    Solo permite `True` o `False`.\
    Fundamental para máscaras y filtrados lógicos.

-   **datetime64 (Fecha y Hora)**\
    Tipo especializado para datos temporales.\
    Permite operaciones como:

    -   Restar fechas
    -   Extraer año, mes, día, día de la semana

    Si una fecha se almacena como `object`, pierde su funcionalidad
    analítica.

-   **timedelta**\
    Representa una duración o diferencia temporal\
    (ejemplo: *2 días y 5 horas*).

------------------------------------------------------------------------

### D. Tipos Especializados (Optimización)

-   **category (Categórico)**\
    Versión optimizada de `object`.\
    Ideal cuando una columna de texto tiene pocos valores únicos
    repetidos con frecuencia\
    (ejemplo: género, país, estado civil).

    **Ventaja clave:**\
    Reduce drásticamente el uso de memoria al almacenar códigos
    numéricos internos en lugar de repetir cadenas de texto.

------------------------------------------------------------------------

## 3. ¿Para Qué Sirve la Gestión de Tipos?

Controlar los *dtypes* no es un tecnicismo, es una necesidad operativa.

### Beneficios principales

-   **Eficiencia de Memoria (RAM)**\
    Una columna `"Sí/No"` como `object` ocupa mucho más que como `bool`
    o `category`.\
    En datasets grandes, esto define si los datos caben o no en la
    máquina.

-   **Habilitación de Funcionalidades**

    -   No puedes sumar texto (se concatenará).
    -   No puedes trabajar con fechas si están como `object`.
    -   Muchas operaciones avanzadas dependen del tipo correcto.

-   **Velocidad de Procesamiento**\
    Las operaciones vectorizadas sobre tipos nativos (`int`, `float`)
    son órdenes de magnitud más rápidas que sobre `object`.

------------------------------------------------------------------------

## 4. Funciones y Métodos Teóricos Clave

### A. Inspección (Diagnóstico)

-   **`.dtypes`**\
    Devuelve el tipo de dato de cada columna.

-   **`.info()`**\
    Resumen técnico del DataFrame:

    -   Tipos de datos
    -   Valores nulos
    -   Uso estimado de memoria RAM

------------------------------------------------------------------------

### B. Conversión Explícita (Casting)

-   **`.astype()`**\
    Fuerza la conversión de un tipo a otro.

    Características:

    -   Es estricta
    -   Fallará si la conversión no es lógicamente posible

------------------------------------------------------------------------

### C. Conversión Inteligente (Parsing)

Funciones diseñadas para limpiar datos reales:

-   **`pd.to_numeric()`**\
    Intenta convertir valores a numéricos.\
    Puede manejar errores sin romper el flujo del programa.

-   **`pd.to_datetime()`**\
    Motor avanzado de conversión de fechas.\
    Acepta múltiples formatos y los transforma a `datetime64`.

------------------------------------------------------------------------

### D. Selección por Tipo

-   **`.select_dtypes()`**\
    Permite seleccionar columnas según su tipo\
    (por ejemplo, solo columnas numéricas para análisis estadístico).

------------------------------------------------------------------------

## 5. Resumen Conceptual

El flujo de trabajo profesional correcto es:

1.  Cargar los datos.
2.  Diagnosticar tipos (`.info()`).
3.  Corregir tipos (`.astype()`, `to_datetime()`).
4.  Analizar.

⚠️ **Si el tipo de dato es incorrecto, el análisis será erróneo o
imposible.**
