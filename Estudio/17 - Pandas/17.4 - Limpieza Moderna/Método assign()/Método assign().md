# 📘 Teoría Profunda: El Método `.assign()` en Pandas

------------------------------------------------------------------------

## 1️⃣ ¿Qué es `.assign()`?

El método `.assign()` es una herramienta de **Pandas** diseñada
específicamente para:

-   Crear nuevas columnas.
-   Sobrescribir columnas existentes.
-   Mantener un estilo de programación funcional y limpio.

### 🔥 Su Superpoder: Inmutabilidad

`.assign()` **nunca modifica el DataFrame original**.

En lugar de alterar los datos existentes, devuelve **una nueva copia**
del DataFrame con las columnas añadidas o modificadas.

Esto permite: - Mayor seguridad en transformaciones. - Menor riesgo de
errores accidentales. - Código más profesional y reproducible.

------------------------------------------------------------------------

## 2️⃣ El "Frente a Frente": Tradicional vs Moderno

### 🧱 Forma Tradicional (Mutación Directa)

``` python
df['precio_con_iva'] = df['precio'] * 1.19
df['ganancia'] = df['precio_con_iva'] - df['costo']
```

-   Modifica directamente el DataFrame original.
-   Puede generar efectos secundarios si no se tiene cuidado.
-   Rompe el flujo de transformación si se abusa de variables
    temporales.

------------------------------------------------------------------------

### 🚀 Forma Moderna (Effective Pandas con `.assign()`)

``` python
df_final = (df
    .assign(precio_con_iva = lambda x: x['precio'] * 1.19)
    .assign(ganancia = lambda x: x['precio_con_iva'] - x['costo'])
)
```

✔ Crea un flujo continuo (pipeline).\
✔ Permite encadenar transformaciones.\
✔ Mejora la legibilidad.\
✔ Mantiene el DataFrame original intacto.

### 💡 ¿Por qué usamos `lambda x:`?

Porque `x` representa el DataFrame **en ese momento exacto del flujo**.

Esto permite usar columnas recién creadas dentro del mismo pipeline.

------------------------------------------------------------------------

## 3️⃣ ¿Para qué se usa y cuándo usarlo? ✅

### 🔗 1. Para crear Pipelines (Cadenas de Transformación)

Permite:

-   Filtrar
-   Limpiar
-   Transformar
-   Crear columnas

Todo dentro de un único bloque fluido y legible.

En vez de: - `df_1` - `df_2` - `df_3`

Tienes una única transformación elegante.

------------------------------------------------------------------------

### 🧮 2. Para Cálculos Dependientes

Puedes crear una columna y usarla inmediatamente después.

Ejemplo: - Crear `precio_con_iva` - Luego usarla para calcular
`ganancia`

Esto mejora claridad y evita errores.

------------------------------------------------------------------------

### 📖 3. Para Legibilidad Profesional

Se lee como una receta:

1.  Toma el DataFrame.
2.  Aplica transformación.
3.  Añade columna.
4.  Añade otra.
5.  Devuelve resultado final.

------------------------------------------------------------------------

## 4️⃣ ¿Cuándo NO usar `.assign()`? ❌

### 🧠 1. Cuando la RAM es Crítica (Big Data Extremo)

Como `.assign()` devuelve una copia nueva:

-   Si el dataset pesa 50GB
-   Y tienes poca memoria

Podría colapsar tu sistema.

En esos casos, la asignación tradicional puede ser más eficiente.

------------------------------------------------------------------------

### 🚫 2. Nombres de Columnas con Espacios

`.assign()` usa argumentos tipo palabra clave.

No puedes hacer:

``` python
.assign(Precio Final = ...)
```

Porque Python no permite espacios en nombres de variables.

------------------------------------------------------------------------

### 🔄 3. Crear Decenas de Columnas Dinámicas

Si necesitas generar muchas columnas dentro de un bucle `for`,
`.assign()` no es la herramienta ideal.

------------------------------------------------------------------------

# 🧰 Las Herramientas Compañeras dentro de `.assign()`

`.assign()` es la olla.\
Las funciones internas son los ingredientes.

------------------------------------------------------------------------

## A️⃣ Operaciones Matemáticas (Vectorizadas)

No necesitas bucles.

Ejemplos comunes:

-   Suma / resta / multiplicación
-   Cálculo de porcentajes
-   Ratios y métricas

Ejemplo conceptual:

``` python
lambda x: x['ventas'] / x['visitas']
```

Pandas opera sobre columnas completas de forma eficiente.

------------------------------------------------------------------------

## B️⃣ Lógica Condicional con `np.where()` 🔥

La herramienta más poderosa para crear reglas de negocio.

Equivalente al `SI()` de Excel, pero optimizado para millones de filas.

### 📌 Estructura:

``` python
np.where(CONDICIÓN, VALOR_SI_CUMPLE, VALOR_SI_NO_CUMPLE)
```

### 📌 ¿Para qué sirve?

-   Crear categorías
-   Crear banderas (flags)
-   Aplicar reglas empresariales

Ejemplo conceptual:

``` python
.assign(categoria_peso = lambda x: np.where(x['peso'] > 10, 'Pesado', 'Ligero'))
```

------------------------------------------------------------------------

## C️⃣ Métodos de Texto y Fechas

Todo lo aprendido sobre:

-   `.str.upper()`
-   `.str.lower()`
-   `.str[0:4]`
-   `.dt.year`
-   `.dt.month`

Se usa dentro de `.assign()` para crear columnas derivadas como:

-   Extraer año
-   Obtener dominio de correo
-   Formatear nombres

------------------------------------------------------------------------

# 🧠 Resumen Final del Concepto

`.assign()` cambia tu mentalidad.

Dejas de pensar en:

> "Modificar tablas"

Y empiezas a pensar en:

> "Transformar flujos de datos"

📥 Entra dato crudo.\
🔄 Pasa por el pipeline.\
📤 Sale dato enriquecido, limpio y listo para análisis.

------------------------------------------------------------------------

## 🎯 Conclusión

`.assign()` no es solo una función.

Es una filosofía de trabajo profesional en Pandas.

-   Más limpio.
-   Más seguro.
-   Más legible.
-   Más escalable.

Si dominas `.assign()`, estás dando un salto de nivel hacia el análisis
de datos avanzado.
