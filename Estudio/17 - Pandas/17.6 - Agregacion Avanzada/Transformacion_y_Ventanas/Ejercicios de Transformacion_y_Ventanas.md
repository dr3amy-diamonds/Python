# 📊 Taller: Dominando `transform()` y Funciones de Ventana

------------------------------------------------------------------------

## 🟢 Misión 1: El Peso de la Categoría (`transform`)

### 📌 Contexto de Negocio

La dirección quiere saber qué tan relevante es cada venta individual
dentro de su propia categoría de producto.

### 🎯 Tu Objetivo

Crear una columna llamada:

    participacion_categoria

### 🧠 Lógica

Dividir el `ingreso_total` de cada fila entre la **suma total de
ingresos de su misma `categoria_producto`** y multiplicarlo por 100.

### 🏆 Competencia que desarrollas

Uso de `.transform()` para **difundir valores agregados grupales sin
colapsar el DataFrame**.

------------------------------------------------------------------------

## 🟡 Misión 2: Seguimiento de Metas por País (`cumsum`)

### 📌 Contexto de Negocio

El equipo de ventas de cada país necesita visualizar cómo crece su
"alcancía" de ingresos a medida que transcurre el tiempo.

### 🎯 Tu Objetivo

Crear una columna llamada:

    acumulado_pais

### 🧠 Lógica

1.  Agrupar por `pais`.
2.  Aplicar suma acumulada (`cumsum`) sobre `ingreso_total`.

### ⚠️ Advertencia Importante

Antes de aplicar la suma acumulada, los datos **deben estar ordenados
por fecha**.

### 🏆 Competencia que desarrollas

Combinación de agrupación con **funciones expansivas**.

------------------------------------------------------------------------

## 🟠 Misión 3: Filtro de Ruido en Ventas (`rolling`)

### 📌 Contexto de Negocio

Con miles de registros, la gráfica de ingresos presenta demasiados picos
y valles. Se necesita observar la tendencia real.

### 🎯 Tu Objetivo

Crear una columna llamada:

    tendencia_suavizada_100

### 🧠 Lógica

Calcular el **promedio móvil** (`mean`) de los últimos 100 registros de
la columna `ingreso_total`.

### 🏆 Competencia que desarrollas

Uso de **ventanas deslizantes (`rolling`)** para análisis de series
temporales.

------------------------------------------------------------------------

## 🔴 Misión 4: Alerta de Precios (`shift`)

### 📌 Contexto de Negocio

Se quiere detectar si el `precio_unitario` cambió drásticamente respecto
a la venta anterior dentro de la misma categoría.

### 🎯 Tu Objetivo

Crear una columna llamada:

    variacion_precio_cat

### 🧠 Lógica

1.  Agrupar por `categoria_producto`.
2.  Utilizar `.shift(1)` para traer el `precio_unitario` de la
    transacción anterior dentro de la misma categoría.
3.  Restar el precio actual menos el anterior.

### 🏆 Competencia que desarrollas

Uso avanzado de **desplazamiento dentro de grupos**.

------------------------------------------------------------------------

# 💡 Recomendación de Harrison (Effective Pandas)

Para lograr un código limpio, elegante y profesional:

-   Resolver las cuatro misiones dentro de un solo bloque lógico.
-   Utilizar `.assign()` para crear múltiples columnas.
-   Encadenar operaciones sin romper el flujo del DataFrame.
-   Mantener una estructura clara y legible.

------------------------------------------------------------------------

## 🚀 Objetivo Final del Taller

Dominar:

-   `groupby()`
-   `transform()`
-   `cumsum()`
-   `rolling()`
-   `shift()`
-   Encadenamiento con `.assign()`

Sin colapsar datos innecesariamente y aplicando correctamente el
concepto de **funciones de ventana en Pandas**.
