# Inspección Inicial de Datos (EDA -- Fase 0)

## 1. Definición y Filosofía

La **Inspección Inicial de Datos**, también conocida como *Sanity
Check*, es el proceso de diagnóstico inmediato que se ejecuta justo
después de cargar un DataFrame y **antes de escribir una sola línea de
código de análisis o limpieza**.

Según Harrison, muchos errores de análisis no nacen de modelos
complejos, sino de saltarse este paso básico.\
Los analistas novatos asumen que los datos están limpios; los expertos
asumen que los datos son un desastre **hasta que se demuestre lo
contrario**.

### ¿Para qué sirve?

La inspección inicial responde tres preguntas vitales:

#### 1. Integridad estructural

-   ¿Se cargaron correctamente las filas y columnas?\
-   ¿Los encabezados están donde deben estar?

#### 2. Salud de los tipos de datos (*dtypes*)

-   ¿Los números son realmente números?\
-   ¿Las fechas son fechas?\
    Este punto es crítico para evitar errores silenciosos en cálculos y
    transformaciones.

#### 3. Dimensión del problema

-   ¿Tengo 100 filas o 10 millones?\
-   ¿Mi equipo puede manejar este volumen sin colapsar la memoria RAM?

------------------------------------------------------------------------

## 2. Toolbox de Funciones (Ranking de Utilidad)

Herramientas nativas de Pandas ordenadas por **densidad de información
por comando**.

### 🥇 1. El Escáner Completo: `.info()`

La función reina de la inspección inicial.\
McKinney la define como el **punto de partida obligatorio**.

**Qué hace**\
Proporciona una radiografía técnica completa del DataFrame.

**Qué revela** - Tipo y rango del índice (`RangeIndex`). - Nombres de
todas las columnas. - Conteo de valores **no nulos** por columna. - Tipo
de dato (`dtype`) de cada columna. - Uso aproximado de memoria RAM.

**Nota Pro (Harrison)**\
Se recomienda usar:

``` python
df.info(memory_usage="deep")
```

Esto permite conocer el peso real de las columnas de texto, que Pandas
suele subestimar por defecto.

------------------------------------------------------------------------

### 🥈 2. La Mirada Imparcial: `.sample()` vs `.head()`

#### Enfoque clásico: `.head()`

-   Muestra las primeras 5 filas.
-   Útil para verificar encabezados.

#### Enfoque moderno: `.sample(n)`

Matt Harrison recomienda priorizar `.sample()` sobre `.head()`.

**¿Por qué?**\
Los datos suelen estar ordenados (por fecha, ID, etc.).\
`.head()` ofrece una visión sesgada.\
`.sample()` muestra filas aleatorias, revelando anomalías ocultas en el
centro o final del dataset.

Ejemplo:

``` python
df.sample(5)
```

------------------------------------------------------------------------

### 🥉 3. El Resumen Estadístico: `.describe()`

La herramienta del **sentido común matemático**.

#### Para datos numéricos

Calcula: - Media - Desviación estándar - Mínimos y máximos - Cuartiles

**Uso principal**\
Detección de *outliers*.\
Ejemplos de alerta: - Edad máxima de 200 años. - Precios negativos.

#### Para texto u objetos

``` python
df.describe(include="O")
```

Muestra: - Conteo total - Número de valores únicos - Valor más
frecuente - Frecuencia del valor más común

------------------------------------------------------------------------

## 3. Otras Herramientas Clave

### 📐 `.shape`

-   Atributo que devuelve `(filas, columnas)`.
-   Confirmación rápida de volumen.

Ejemplo de alerta: Esperabas `(1_000_000, 10)` y obtienes `(500, 10)` →
la carga falló.

------------------------------------------------------------------------

### 🚨 Radar de Nulos: `.isna().sum()`

Cuenta los valores faltantes por columna.

Uso estratégico: - 90% de nulos → eliminar columna. - 1% de nulos →
imputar valores.

Ejemplo:

``` python
df.isna().sum()
```

------------------------------------------------------------------------

## 4. ¿Por qué es obligatorio usar esta fase?

### Detección de basura oculta

Algunos CSV contienen notas o pies de página.\
Usar `.tail()` ayuda a detectarlos.

### Validación de tipos

Si `.info()` indica que una columna "Ventas" es `object`, probablemente
contiene símbolos como `$` o texto mezclado.\
Sin esta validación, los cálculos fallarán más adelante.

### Gestión de recursos

Si `.info()` muestra un DataFrame de 4 GB y tu equipo tiene 8 GB de
RAM: - Optimiza tipos. - Usa `category`. - Reduce memoria antes de
analizar.

Ignorar esto puede congelar el sistema.

------------------------------------------------------------------------

## 5. Flujo de Trabajo Profesional Recomendado

Orden lógico de ejecución:

1.  Cargar los datos.
2.  `.shape` → ¿Llegó todo?
3.  `.info()` → Tipos de datos y memoria.
4.  `.sample(5)` → Vista real sin sesgo.
5.  `.describe()` → Validación matemática.

**Solo después** de pasar este checklist se procede a limpieza o
análisis.

------------------------------------------------------------------------

## 6. Idea Central

La Inspección Inicial no es opcional.\
Es el equivalente a revisar los instrumentos antes de despegar.

Saltársela no ahorra tiempo.\
Solo retrasa el error.
