# 📊 Taller Práctico de Análisis con GroupBy en Pandas

Este documento presenta una serie de misiones analíticas orientadas al
uso profesional de **groupby()**, agregaciones y construcción de
pipelines de datos.

El objetivo es desarrollar pensamiento estructurado en análisis de
información financiera, comercial y operativa.

------------------------------------------------------------------------

## 🟢 Misión 1: El Resumen Básico (Análisis Unidimensional)

### 🎯 Contexto

El área de Finanzas necesita conocer el total de dinero generado por
cada categoría de producto.

### 📌 Objetivo Analítico

Construir un resumen que permita visualizar claramente cuánto dinero
ingresó en total por cada categoría.

### 🧠 Competencias que se evalúan

-   Agrupación por una sola dimensión.
-   Selección específica de columnas numéricas.
-   Aplicación de una función de agregación simple.

### 📎 Entregable esperado

Una tabla resumen donde: 
- Cada fila represente una categoría. 
- Se muestre el total acumulado de ingresos por categoría.

------------------------------------------------------------------------

## 🟡 Misión 2: Análisis de Rentabilidad (Multi‑dimensión)

### 🎯 Contexto

No basta con conocer ingresos. La dirección necesita evaluar
rentabilidad promedio por sucursal dependiendo del tipo de producto.

### 📌 Objetivo Analítico

1.  Construir una métrica de ganancia neta.
2.  Analizar cómo se comporta dicha ganancia según:
    -   Sucursal
    -   Categoría

### 🧠 Competencias que se evalúan

-   Creación de nuevas columnas derivadas.
-   Agrupaciones por múltiples dimensiones.
-   Cálculo de promedios como métrica comparativa.
-   Interpretación de rentabilidad promedio.

### 📎 Entregable esperado

Una tabla bidimensional donde: - Las filas representen combinaciones de
sucursal y categoría. - Se muestre la ganancia neta promedio.

------------------------------------------------------------------------

## 🟠 Misión 3: Reporte Maestro del Equipo de Ventas (.agg)

### 🎯 Contexto

Recursos Humanos necesita evaluar el desempeño individual de cada
vendedor mediante múltiples indicadores simultáneos.

### 📌 Objetivo Analítico

Construir un reporte consolidado que incluya:

-   Número total de transacciones realizadas.
-   Total de ingresos generados.
-   Valor de la venta más costosa realizada.

### 🧠 Competencias que se evalúan

-   Agrupación por entidad individual (vendedor).
-   Uso de múltiples funciones de agregación en una sola operación.
-   Construcción de reportes ejecutivos claros.
-   Renombrado estratégico de métricas.

### 📎 Entregable esperado

Una tabla donde: - Cada fila represente un vendedor. - Se incluyan tres
columnas métricas claramente nombradas.

------------------------------------------------------------------------

## 🔴 Misión 4: El Pipeline Senior (Código Limpio y Profesional)

### 🎯 Contexto

Marketing quiere identificar cuál sucursal mueve más dinero, pero
únicamente considerando pagos realizados con tarjeta.

El análisis debe realizarse siguiendo principios de código limpio y
encadenamiento estructurado de transformaciones.

### 📌 Objetivo Analítico

Construir un flujo de transformación que:

1.  Filtre únicamente las compras pagadas con tarjeta.
2.  Agrupe la información por sucursal.
3.  Calcule el total de ingresos.
4.  Ordene el resultado de mayor a menor.

### 🧠 Competencias que se evalúan

-   Filtrado condicional.
-   Construcción de pipelines encadenados.
-   Ordenamiento de resultados agregados.
-   Claridad estructural en el flujo analítico.

### 📎 Entregable esperado

Una tabla ordenada donde: 
- Las filas representen sucursales. 
- - Se observe claramente cuál genera mayor volumen de ingresos mediante pagos
con tarjeta.

------------------------------------------------------------------------

# ✅ Criterios de Calidad Esperados

Un trabajo bien realizado debe:

-   Presentar tablas limpias y legibles.
-   Tener nombres de columnas claros y profesionales.
-   Mostrar coherencia entre el objetivo de negocio y el análisis
    técnico.
-   Mantener orden lógico en cada transformación de datos.
-   Evitar pasos innecesarios o redundantes.

------------------------------------------------------------------------

# 🎓 Objetivo Académico del Taller

Este ejercicio busca reforzar:

-   Pensamiento analítico estructurado.
-   Comprensión profunda del método groupby().
-   Uso estratégico de funciones de agregación.
-   Construcción de reportes ejecutivos basados en datos.
-   Diseño de pipelines profesionales y mantenibles.

------------------------------------------------------------------------

📌 Importante:\
Este documento describe únicamente los objetivos y requerimientos
analíticos.\
Las soluciones deben desarrollarse por separado como parte del ejercicio
práctico.
