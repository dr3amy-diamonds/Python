# 📘 Teoría Profunda: Type Casting (Conversión de Tipos)

------------------------------------------------------------------------

## 1. ¿Qué es el Type Casting?

En términos simples, es el proceso de transformar la naturaleza interna
de una columna de datos.\
Es decirle a Pandas:

> "No trates esta columna como texto genérico, trátala como una fecha, o
> como un número pequeño, o como una categoría repetitiva".

Es cambiar el **"envase" donde guardas el dato** para que ocupe menos
espacio y sea más fácil de manipular.

------------------------------------------------------------------------

## 2. ¿Cómo funciona "bajo el capó"? (Arquitectura)

Para entender esto, hay que mirar cómo guarda Pandas los datos en la
memoria RAM.

### 🔥 El Infierno (`object`)

Cuando cargas un CSV, si Pandas ve texto o una mezcla de cosas, usa el
tipo `object`.

Esto significa que: - Crea una lista de punteros (direcciones de
memoria). - El dato real está disperso por la memoria. - Es más lento y
más pesado.

------------------------------------------------------------------------

### 🌟 El Paraíso (Tipos NumPy)

Cuando conviertes una columna a un tipo específico (`int8`, `float32`,
etc.), Pandas usa NumPy para:

-   Reservar un bloque sólido y contiguo de memoria.
-   Permitir que la CPU procese el bloque a gran velocidad.
-   Reducir el consumo de RAM.

------------------------------------------------------------------------

## 3. ¿Para qué sirve y por qué DEBE usarse? (Mundo Laboral)

En el trabajo real, no se usa Type Casting por capricho. Se usa por tres
razones críticas.

------------------------------------------------------------------------

### A. 🔓 Desbloqueo de Funcionalidades

Si una fecha es texto ("2023-01-01"), es solo una palabra.\
No puedes sumar días ni saber si fue lunes.

Al convertir:

-   Texto → `datetime`\
    Desbloqueas métodos como:
    -   `.dt.year`
    -   `.dt.day_name()`
    -   `.dt.week`
-   Texto → `numeric`\
    Desbloqueas:
    -   Sumas
    -   Promedios
    -   Gráficos

------------------------------------------------------------------------

### B. 💾 Optimización de Memoria RAM (Big Data)

Imagina una columna **"País"** con 1 millón de filas, pero solo 5 países
distintos.

**Como `object`:** - Pandas guarda la palabra completa miles de veces. -
Alto consumo de memoria.

**Como `category`:** - Pandas guarda un diccionario interno (0 =
Argentina, 1 = Chile, etc.). - En la tabla solo guarda el número
pequeño.

📉 Impacto real:\
Puedes reducir un archivo de 1 GB a 50 MB solo optimizando tipos.

Esto permite trabajar con grandes volúmenes de datos en una laptop
común.

------------------------------------------------------------------------

### C. ⚡ Velocidad de Cómputo

Las operaciones matemáticas en tipos nativos (`int`, `float`) pueden ser
hasta 100 veces más rápidas que en tipo `object`.

------------------------------------------------------------------------

## 4. Métodos y Funciones Clave

Estos son los métodos fundamentales.

------------------------------------------------------------------------

### A. `.astype()` (El Estándar)

Es el método principal cuando los datos están limpios.

Tipos comunes:

-   `int8`, `int16`, `int32`
-   `float32`
-   `bool`
-   `category`

------------------------------------------------------------------------

### B. `pd.to_numeric()` (El Cirujano)

Se usa cuando los números están sucios:

Ejemplos: - "1,000" - "\$50" - "Vendido"

Permite convertir datos problemáticos sin romper el programa.

Argumento clave:

-   `errors='coerce'`\
    Convierte valores inválidos en `NaN`.

------------------------------------------------------------------------

### C. `pd.to_datetime()` (El Relojero)

Convierte texto en objetos de fecha.

Reconoce múltiples formatos:

-   "15/01/2023"
-   "2023-Jan-15"
-   "2023-01-15"

------------------------------------------------------------------------

## 5. Los Tipos de Datos (Jerarquía de Optimización)

  ------------------------------------------------------------------------
  Tipo de Dato         ¿Cuándo usarlo?           Ventaja Laboral
  -------------------- ------------------------- -------------------------
  `category`           Texto con pocos valores   Ahorro masivo de RAM
                       únicos repetidos          (hasta 90%)

  `int8` / `int16`     Números enteros pequeños  Evita usar `int64`
                                                 innecesariamente

  `float32`            Números decimales         Mitad de memoria que
                                                 `float64`

  `Int64` (nullable)   Enteros con valores nulos Mantiene enteros sin
                                                 convertir a float

  `bool`               Solo dos valores posibles Ocupa 1 byte
  ------------------------------------------------------------------------

------------------------------------------------------------------------

## 📝 Resumen Práctico

1.  Carga los datos.
2.  Analiza cada columna.
3.  Castea inmediatamente:

-   Texto repetitivo → `category`
-   Fechas en texto → `pd.to_datetime()`
-   Números sucios → `pd.to_numeric(..., errors='coerce')`
-   Números pequeños → `int8` o `int16`

------------------------------------------------------------------------

## 🎯 Conclusión

El Type Casting no es un detalle menor.

Es una práctica profesional clave que:

-   Reduce memoria.
-   Aumenta velocidad.
-   Desbloquea funcionalidades avanzadas.
-   Permite trabajar con grandes volúmenes de datos eficientemente.

Optimizar tipos de datos es una de las habilidades más importantes en
análisis de datos profesional.
