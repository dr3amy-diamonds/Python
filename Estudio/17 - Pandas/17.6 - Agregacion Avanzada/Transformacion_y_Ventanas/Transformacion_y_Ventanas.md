# 📘 `.transform()` y Funciones de Ventana en Pandas

Guía Teórica y Aplicación en Contexto Corporativo

------------------------------------------------------------------------

# 🧠 Parte 1: La Teoría de `.transform()` (El Difusor)

## ¿Qué es `.transform()`?

En Pandas, cuando utilizas `groupby()`, la operación natural suele ser
aplicar:

-   `.agg()`
-   `.sum()`
-   `.mean()`

Estas funciones **colapsan** la tabla.

👉 Si agrupas 100 ventas en 3 ciudades, el resultado tendrá **3 filas**.

`.transform()` hace exactamente lo contrario.

Produce un objeto del **mismo tamaño que el original**.\
Calcula la métrica del grupo, pero en lugar de reducir la tabla,
**difunde el resultado a cada fila original**.

Si tenías 100 filas, sigues teniendo 100 filas.

------------------------------------------------------------------------

## 🎯 ¿Cuándo se usa en la vida real?

Es la herramienta reina para **Feature Engineering**, porque permite que
una fila "conozca" el contexto de su grupo sin alterar la estructura del
dataset.

------------------------------------------------------------------------

## 📌 Casos de Uso Corporativos

### 1️⃣ Cálculo de porcentajes dentro del grupo

Pregunta del negocio:

> ¿Qué porcentaje del total de ventas de su sucursal representa cada
> vendedor?

Necesitas que cada fila tenga el total de su sucursal.

``` python
df['total_sucursal'] = df.groupby('sucursal')['ingresos_usd'].transform('sum')
df['porcentaje'] = df['ingresos_usd'] / df['total_sucursal']
```

------------------------------------------------------------------------

### 2️⃣ Imputación inteligente de valores nulos

En vez de usar el promedio global:

``` python
df['edad'] = df.groupby('pais')['edad'].transform('mean')
```

Cada país se rellena con su propio promedio.

------------------------------------------------------------------------

### 3️⃣ Filtro de anomalías

> Mostrar empleados que ganan por encima del promedio de su
> departamento.

``` python
promedio = df.groupby('departamento')['salario'].transform('mean')
df_filtrado = df[df['salario'] > promedio]
```

------------------------------------------------------------------------

## 🧩 Sintaxis Base

``` python
df['promedio_sucursal'] = (
    df.groupby('sucursal')['ingresos_usd']
      .transform('mean')
)
```

# 📘 Parte 2: Funciones de Ventana (Window Functions)

## ¿Qué son?

Son operaciones matemáticas que dependen del **orden de las filas**.

Se aplican sobre una "ventana" de datos que:

-   Puede tener tamaño fijo
-   Puede crecer progresivamente
-   Puede desplazarse entre filas

Son fundamentales en **Series de Tiempo**.

------------------------------------------------------------------------

# 🔹 1. Ventana Móvil --- `.rolling()`

## ¿Qué hace?

Define un número fijo de filas hacia atrás.

Ejemplo:

``` python
df['promedio_7_dias'] = (
    df['ingresos_usd']
      .rolling(window=7)
      .mean()
)
```

## 🎯 Uso empresarial

-   Suavizar ventas
-   Eliminar picos de fines de semana
-   Detectar tendencias reales

------------------------------------------------------------------------

# 🔹 2. Ventana Expansiva --- `.expanding()` y `.cumsum()`

## ¿Qué hace?

Empieza en la primera fila y crece acumulando todo el historial.

``` python
df['gasto_acumulado'] = df['gastos'].cumsum()
```

(`cumsum()` es un atajo optimizado de `.expanding().sum()`)

## 🎯 Uso empresarial

-   Year To Date (YTD)
-   Control presupuestal
-   Seguimiento acumulado de metas

------------------------------------------------------------------------

# 🔹 3. Desplazamiento --- `.shift()`

## ¿Qué hace?

Mueve los valores hacia arriba o abajo cierta cantidad de filas.

``` python
df['venta_ayer'] = df['ingresos_usd'].shift(1)
df['crecimiento_diario'] = (
    df['ingresos_usd'] - df['venta_ayer']
)
```

## 🎯 Uso empresarial

-   Comparaciones MoM (Month over Month)
-   Comparación diaria
-   Cálculo de variaciones porcentuales

# 🧠 Framework Mental para Resolver Problemas

Antes de escribir código, pregúntate:

### ✅ ¿Quiero resumir y destruir detalle?

➡️ Usa `groupby().agg()`

### ✅ ¿Quiero comparar cada fila contra su grupo sin perder detalle?

➡️ Usa `groupby().transform()`

### ✅ ¿La respuesta depende del tiempo o acumulación?

➡️ Ordena por fecha y usa: - `.rolling()` - `.cumsum()` - `.shift()`

------------------------------------------------------------------------

# 🚀 Conclusión

`.transform()` y las funciones de ventana son herramientas clave para:

-   Ingeniería de características
-   Análisis corporativo
-   Series de tiempo
-   Construcción de métricas avanzadas

Dominar estas herramientas te permite pensar en términos analíticos y no
solo en términos de código.
