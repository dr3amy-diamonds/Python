# 🛠️ Ejercicio Práctico: El Inventario de la Tienda

## 📝 Contexto

Te han enviado por correo los datos de inventario de una tienda de
tecnología, pero están desordenados en listas sueltas.\
Tu jefe necesita que conviertas esta información en una estructura
profesional usando **Pandas** y que puedas describir rápidamente cómo
están organizados los datos.

------------------------------------------------------------------------

## 📁 Datos Crudos

La información disponible es la siguiente:

-   **Productos:** Laptop, Mouse, Teclado, Monitor\
-   **Precios:** 1200, 25, 45, 300\
-   **Stock:** 5, 50, 20, 10\
-   **Disponible:** True, True, True, False

------------------------------------------------------------------------

## 🎯 Misión 1: La Construcción

Tu objetivo es:

-   Importar la librería **pandas**.
-   Crear un diccionario llamado `data_inventario` que contenga los
    datos anteriores.
-   Usar ese diccionario para construir un **DataFrame**.
-   Mostrar el DataFrame completo en pantalla.

📌 En esta misión practicas cómo pasar de listas sueltas a una
estructura tabular profesional.

------------------------------------------------------------------------

## 📐 Misión 2: El Informe de Dimensiones (Atributos)

Tu jefe te pregunta:

> "¿Cuántos productos tenemos y cuántas variables estamos midiendo?"

Debes:

-   Usar el atributo `.shape` para conocer filas y columnas.
-   Usar el atributo `.columns` para ver los nombres de las variables.
-   Usar el atributo `.index` para observar cómo Pandas etiqueta
    automáticamente las filas.

📌 Esta misión sirve para **entender la estructura interna** del
DataFrame.

------------------------------------------------------------------------

## 🧬 Misión 3: La Prueba de ADN (Heterogeneidad)

El objetivo es comprobar que un DataFrame puede contener **distintos
tipos de datos** al mismo tiempo.

Debes:

-   Consultar el atributo `.dtypes` del DataFrame.
-   Observar cómo Pandas identifica automáticamente texto, números y
    valores lógicos.

📌 Aquí confirmas que Pandas trabaja con datos del mundo real, no solo
números.

------------------------------------------------------------------------

## 🔍 Misión 4: Extracción (De DataFrame a Serie)

Ahora necesitas analizar solo los precios.

Debes:

-   Extraer la columna **Precio** del DataFrame.
-   Guardarla en una nueva variable llamada `serie_precios`.
-   Comprobar el tipo de dato resultante.

📌 Esta misión demuestra la relación entre **DataFrame** y **Series**.

------------------------------------------------------------------------

## ✅ Objetivo del Ejercicio

Al finalizar este ejercicio deberías ser capaz de:

-   Transformar datos crudos en un DataFrame.
-   Inspeccionar su tamaño y estructura.
-   Reconocer la mezcla de tipos de datos.
-   Extraer columnas individuales para su análisis.

📊 *Este ejercicio no busca resolver cálculos, sino comprender la
anatomía de un DataFrame.*
