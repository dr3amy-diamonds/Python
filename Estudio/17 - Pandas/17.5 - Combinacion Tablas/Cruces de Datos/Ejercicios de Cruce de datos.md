# 📊 Taller Práctico: Consolidación y Cruce de Datos con Pandas

------------------------------------------------------------------------

## 🎯 Objetivo del Taller

Este taller tiene como propósito reforzar conceptos fundamentales en el
manejo y cruce de datos utilizando Pandas. Trabajarás situaciones
similares a un entorno laboral real donde deberás:

-   Consolidar información.
-   Enriquecer datos con tablas externas.
-   Auditar cobertura de registros.
-   Generar métricas financieras finales.

⚠️ Importante:\
No debes resolver los ejercicios aquí. El objetivo es que desarrolles
las soluciones por tu cuenta.

------------------------------------------------------------------------

# 🟢 Ejercicio 1: Consolidación de Información (Uso de `pd.concat`)

## 📌 Problema Laboral

Tu supervisor te solicita un único reporte consolidado con todos los
envíos realizados durante el día. Actualmente, la información está
separada en dos tablas:

-   Envíos de la mañana (`envios_am`)
-   Envíos de la tarde (`envios_pm`)

El supervisor no quiere ver reportes separados por horario.

## 🧠 Tu Misión

-   Crear un nuevo DataFrame llamado **`df_dia_completo`**.
-   Unir ambas tablas una debajo de la otra.
-   Asegurarte de que el índice final sea limpio y consecutivo.

## 💡 Concepto que Practicas

**Concat** se utiliza cuando: - Las tablas tienen la misma estructura. -
Solo deseas apilarlas verticalmente. - Estás consolidando información de
distintos momentos o fuentes homogéneas.

------------------------------------------------------------------------

# 🟡 Ejercicio 2: Enriquecimiento de Datos (Uso de `pd.merge` - Left Join)

## 📌 Problema Laboral

Ahora que tienes todos los envíos del día en una sola tabla, necesitas
calcular cuánto se debe cobrar por cada uno.

El inconveniente es que: - La tabla de envíos tiene la columna
**`ciudad_destino`** - La tabla de tarifas tiene la columna **`ciudad`**

Los nombres no coinciden.

## 🧠 Tu Misión

-   Cruzar `df_dia_completo` con la tabla `tarifas`.
-   Utilizar un **Left Join**.
-   Indicar correctamente qué columna corresponde en cada tabla.
-   Llamar al resultado **`df_con_precios`**.

## 💡 Concepto que Practicas

**Merge (Left Join)** se utiliza cuando: - Deseas mantener todos los
registros originales. - Traes información adicional desde una tabla
maestra. - No quieres perder datos aunque no exista coincidencia.

------------------------------------------------------------------------

# 🟠 Ejercicio 3: Auditoría de Cobertura (Uso de `pd.merge` - Inner Join)

## 📌 Problema Laboral

El departamento de operaciones quiere saber cuáles envíos pueden
procesarse inmediatamente.

Solo pueden procesarse aquellos que: - Tengan una tarifa oficial
registrada.

## 🧠 Tu Misión

-   Realizar el mismo cruce del ejercicio anterior.
-   Esta vez utilizar un **Inner Join**.
-   Comparar la cantidad de filas con el resultado del Ejercicio 2.
-   Analizar qué ciudad quedó por fuera y por qué ocurrió esto.

## 💡 Concepto que Practicas

**Merge (Inner Join)** se utiliza cuando: - Solo quieres los registros
que existen en ambas tablas. - Necesitas validar coincidencias reales. -
Estás auditando cobertura o consistencia de datos.

------------------------------------------------------------------------

# 🔴 Ejercicio 4: Reporte Financiero Final (Uso de `.assign()`)

## 📌 Problema Laboral

El jefe ahora quiere ver el costo total de cada envío.

La fórmula para calcularlo es:

> peso_kg × precio_por_kg

Sin embargo, existe un detalle importante:

Si una ciudad no tiene tarifa registrada, el costo total generará un
valor nulo.

## 🧠 Tu Misión

-   Trabajar sobre `df_con_precios`.
-   Crear una nueva columna llamada **`costo_total`**.
-   Aplicar la fórmula indicada.
-   Asegurarte de que los valores nulos se transformen en 0.

## 💡 Concepto que Practicas

**Assign** permite: - Crear columnas nuevas de manera limpia. -
Encadenar transformaciones. - Mantener un estilo funcional y claro en el
procesamiento de datos.

------------------------------------------------------------------------

# 🧠 ¿Qué Estamos Practicando en Este Taller?

  Concepto        Propósito
  --------------- --------------------------------------------------
  Concat          Unir archivos iguales en distintos momentos
  Merge (Left)    Traer información adicional sin perder registros
  Merge (Inner)   Filtrar únicamente coincidencias válidas
  Assign          Procesar y calcular métricas después del cruce

------------------------------------------------------------------------

## 🏁 Cierre Académico

Este conjunto de ejercicios simula un flujo real de trabajo en análisis
de datos:

1.  Consolidar información.
2.  Enriquecer con tablas maestras.
3.  Validar cobertura operativa.
4.  Generar indicadores financieros.

Si dominas estos pasos, estás trabajando al nivel esperado en un entorno
profesional de análisis de datos.

------------------------------------------------------------------------

✍️ Recomendación:\
Resuelve cada ejercicio paso a paso y valida los resultados intermedios
antes de continuar.
