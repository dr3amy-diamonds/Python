# 📘 Teoría: Manipulación de Texto en Pandas

------------------------------------------------------------------------

## 1️⃣ ¿Qué es y para qué sirve?

La **manipulación de texto** (String Manipulation) es el proceso de
limpiar, transformar y extraer información de columnas que contienen
cadenas de caracteres (tipo *object* o *string*).

Su objetivo es convertir datos **sucios y heterogéneos** en datos
estructurados y comparables.

Sin esta etapa, no sería posible agrupar correctamente valores como:

-   bogota\
-   BOGOTA\
-   Bogotá\
-   Bogotá

Todos representan lo mismo, pero el sistema los interpreta como
diferentes si no se normalizan.

------------------------------------------------------------------------

## 2️⃣ ¿Para qué funciona el accesor `.str`?

En Python tradicional, limpiar una lista de nombres implicaría usar un
bucle.

En Pandas, eso es ineficiente.

El accesor **`.str`** permite aplicar funciones de texto a toda una
columna simultáneamente (operación vectorizada), lo que hace el proceso
más rápido y profesional.

------------------------------------------------------------------------

## 3️⃣ ¿En qué momento se debe usar?

Se utiliza principalmente en las primeras etapas del **Data Wrangling
(Limpieza de Datos)**.

### 🔹 Normalización

Cuando deseas que todos los valores estén en el mismo formato (por
ejemplo, todo en minúsculas o sin espacios).

### 🔹 Extracción

Cuando una columna contiene múltiples datos en un solo texto (por
ejemplo, un código como FACT-2024-001 y solo necesitas el año).

### 🔹 Limpieza

Para eliminar caracteres especiales o símbolos antes de convertir el
tipo de dato.

### 🔹 Filtrado

Para buscar filas que contengan ciertas palabras clave.

------------------------------------------------------------------------

# 🧰 Métodos y Funciones Principales

Las herramientas se pueden clasificar según su misión en el trabajo
real:

------------------------------------------------------------------------

## A. Limpieza de Formato (Estandarización)

Funciones básicas para que los datos tengan un formato uniforme.

-   Eliminación de espacios al inicio y final del texto.\
-   Conversión completa a minúsculas o mayúsculas.\
-   Formato tipo título (primera letra de cada palabra en mayúscula).

Estas acciones son esenciales después de importar datos desde Excel o
CSV.

------------------------------------------------------------------------

## B. Transformación y Reemplazo

Permiten modificar partes específicas del texto.

-   Reemplazo de símbolos o caracteres no deseados.\
-   División de texto en varias partes según un separador.\
-   Conversión de partes divididas en nuevas columnas.

Muy útil cuando un solo campo contiene información compuesta.

------------------------------------------------------------------------

## C. Extracción (Slicing)

Permite obtener fragmentos específicos de un texto.

Ejemplos comunes:

-   Extraer los primeros caracteres para obtener un año.\
-   Extraer los últimos caracteres para obtener un código identificador.

Funciona bajo la misma lógica de indexación de texto en Python.

------------------------------------------------------------------------

## D. Búsqueda y Filtrado (Lógica)

Estas operaciones devuelven valores booleanos (Verdadero/Falso), ideales
para filtrado.

Permiten:

-   Verificar si un texto contiene una palabra específica.\
-   Comprobar si un texto inicia o termina con ciertos caracteres.

Son equivalentes conceptualmente al operador LIKE en SQL.

------------------------------------------------------------------------

# 💼 Importancia en el Mundo Laboral

En los libros académicos, los datos suelen estar limpios.\
En el entorno real, no.

### 🔹 Unión de Datos (Merging)

Si una tabla dice "iPhone" y otra "iphone", el cruce fallará.\
La estandarización es obligatoria antes de unir tablas.

### 🔹 Prevención de Duplicados Invisibles

Espacios ocultos o diferencias en mayúsculas pueden generar reportes
incorrectos.

### 🔹 Clasificación Automática

Se pueden crear categorías automáticamente buscando palabras clave
dentro del texto (por ejemplo, detectar reclamaciones).

------------------------------------------------------------------------

# ⚠️ Regla de Oro: Manejo de Nulos en Texto

Cuando se aplican operaciones de texto sobre columnas que contienen
valores nulos (NaN), Pandas mantiene esos valores como nulos.

Esto evita errores y hace que el proceso sea seguro.

------------------------------------------------------------------------

## ✅ Conclusión

La manipulación de texto es una etapa crítica en cualquier proceso de
análisis de datos.

Permite:

-   Estandarizar información\
-   Evitar errores en cruces de tablas\
-   Preparar datos para análisis avanzados\
-   Garantizar reportes confiables

Sin una correcta limpieza textual, cualquier análisis posterior puede
estar comprometido.
