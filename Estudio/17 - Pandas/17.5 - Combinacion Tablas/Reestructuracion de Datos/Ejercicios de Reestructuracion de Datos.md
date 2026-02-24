# Taller Avanzado de Transformación y Análisis de Datos con Pandas

## Introducción

En este taller trabajarás con un caso práctico del área de Recursos
Humanos.\
El objetivo es transformar estructuras de datos poco eficientes en
formatos analíticos óptimos, limpiar información intermedia y construir
tablas dinámicas de alto nivel para toma de decisiones.

⚠️ Importante:\
No debes escribir código dentro de este documento. Aquí solo se
describen las misiones analíticas.

------------------------------------------------------------------------

# 🟢 Ejercicio 1: "Derretir" el Sistema Antiguo (melt)

## Contexto

Los sistemas heredados suelen almacenar la información en formato ancho,
donde cada mes aparece como una columna diferente (por ejemplo:
`Ene_2024_Hrs`).

Este formato es visualmente cómodo para humanos, pero es ineficiente
para análisis, visualizaciones y modelado estadístico.

Necesitamos convertir la estructura a formato largo (vertical).

------------------------------------------------------------------------

## Tu Misión

1.  Utilizar el método de transformación adecuado para convertir
    `df_rrhh_ancho` a formato largo.
2.  Definir correctamente las columnas ancla (`id_vars`):
    -   empleado\
    -   departamento\
    -   rol\
3.  Definir como columnas a aplastar (`value_vars`) todas las columnas
    correspondientes a los meses.
4.  Nombrar correctamente:
    -   La columna de etiquetas como **mes_registro**
    -   La columna de valores como **horas_trabajadas**
5.  Guardar el resultado en la variable **df_largo**.

🎯 Resultado esperado:\
Una tabla vertical limpia, ideal para análisis y gráficos.

------------------------------------------------------------------------

# 🟡 Ejercicio 2: Limpiando la Basura en el Pipeline (Repaso .str)

## Contexto

Después de transformar la tabla, la columna `mes_registro` contiene
valores como:

Ene_2024_Hrs\
Feb_2024_Hrs\
Mar_2024_Hrs

Este formato no es adecuado para visualizaciones ejecutivas.\
Queremos conservar únicamente el nombre del mes.

Además, existe un valor faltante en las horas trabajadas que debe ser
corregido.

------------------------------------------------------------------------

## Tu Misión

1.  Trabajando sobre `df_largo`, limpiar la columna `mes_registro` para
    que contenga solo:
    -   Ene\
    -   Feb\
    -   Mar
2.  Puedes:
    -   Separar el texto usando el carácter `_`, o\
    -   Reemplazar directamente la parte innecesaria.
3.  Corregir los valores faltantes en la columna `horas_trabajadas`,
    asegurando que no queden vacíos en el análisis posterior.

🎯 Resultado esperado:\
Una tabla completamente limpia, consistente y lista para agregaciones.

------------------------------------------------------------------------

# 🟠 Ejercicio 3: La Tabla Dinámica del Director (pivot_table)

## Contexto

El Director de RRHH no necesita el detalle por empleado.\
Quiere una vista estratégica:

¿Cuántas horas en total trabajó cada Departamento por cada Mes?

Aquí pasamos del nivel operativo al nivel gerencial.

------------------------------------------------------------------------

## Tu Misión

Construir una tabla dinámica con las siguientes características:

-   Filas (index): departamento\
-   Columnas (columns): mes_registro\
-   Valores (values): horas_trabajadas\
-   Función matemática (aggfunc): suma

🎯 Resultado esperado:\
Una tabla resumen de 3x3 que muestre la suma total de horas por
departamento y mes.

Este es el tipo de tabla que se presenta en reuniones ejecutivas.

------------------------------------------------------------------------

# 🔴 Ejercicio 4: El Reto Financiero Nivel Senior (pivot_table + Lógica)

## Contexto

Finanzas necesita un análisis más estratégico.

En lugar de sumar horas, desean conocer el **promedio de horas
trabajadas**, cruzando:

-   Rol del empleado\
-   Mes

Además, desean una fila y columna adicional con totales generales
automáticos.

------------------------------------------------------------------------

## Tu Misión

Construir una nueva tabla dinámica con:

-   Filas (index): rol\
-   Columnas (columns): mes_registro\
-   Valores (values): horas_trabajadas\
-   Función matemática (aggfunc): promedio

Luego:

-   Activar el parámetro que permite agregar totales automáticos en
    filas y columnas.

🎯 Resultado esperado:\
Una tabla comparativa que muestre promedios por rol y mes, incluyendo
totales generales.

Reflexiona al final:

¿Qué información adicional aparece cuando activas los totales? ¿Por qué
es tan útil en análisis financiero?

------------------------------------------------------------------------

# Cierre Académico

Este taller integra:

-   Transformación estructural de datos\
-   Limpieza avanzada de texto\
-   Corrección de valores faltantes\
-   Construcción de tablas dinámicas estratégicas

Dominar estos conceptos es esencial para cualquier analista de datos,
científico de datos o profesional que trabaje con información
estructurada.

El verdadero poder no está en el código, sino en comprender qué
estructura necesita el negocio para tomar decisiones.
