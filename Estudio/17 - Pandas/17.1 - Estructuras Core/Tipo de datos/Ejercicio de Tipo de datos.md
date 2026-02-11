# 🧠 Ejercicios de Conversión y Optimización de Datos en Pandas (Solo Enunciados)

Este documento contiene ejercicios diseñados para desarrollar
habilidades reales en limpieza, conversión y optimización de datos con
Pandas.

⚠️ Importante:\
- Este archivo contiene **solo los enunciados**.\
- No incluye código ni soluciones.\
- El objetivo es que resuelvas cada ejercicio por tu cuenta.

------------------------------------------------------------------------

## 🟢 Ejercicio 1 --- Limpieza de Números Corruptos

### 📌 Contexto

Un sistema de ventas exportó precios con errores. Algunos valores son
números válidos, pero otros contienen texto incorrecto.

### 📥 Datos de entrada

Lista de valores: - 150.5 - 200 - Error - 300.5 - Fallo - 50

### 🎯 Objetivo

Transformar los datos en valores numéricos reales y calcular
correctamente la suma.

### 📝 Instrucciones

1.  Crear una Serie con los valores proporcionados.
2.  Intentar sumar la serie sin convertir los datos.
3.  Convertir los valores a formato numérico, forzando la conversión de
    errores.
4.  Identificar los valores inválidos.
5.  Calcular la suma correcta ignorando los valores corruptos.

------------------------------------------------------------------------

## 🟡 Ejercicio 2 --- Interpretación de Fechas

### 📌 Contexto

Un reporte contiene fechas almacenadas como texto. Necesitas
convertirlas a fechas reales para analizarlas.

### 📥 Datos de entrada

Lista de fechas: - 2024-01-15 - 2024-02-10 - 2024-01-30 - 2024-03-01

### 🎯 Objetivo

Convertir las fechas a un formato temporal real y extraer información
del mes.

### 📝 Instrucciones

1.  Crear una Serie con las fechas.
2.  Verificar el tipo de dato original.
3.  Convertir los valores a fechas reales.
4.  Extraer el nombre del mes de cada fecha.
5.  Generar una nueva serie con los nombres de los meses.

------------------------------------------------------------------------

## 🟠 Ejercicio 3 --- Optimización de Memoria

### 📌 Contexto

Simulas una encuesta con miles de registros, pero solo existen pocas
categorías repetidas.

### 📥 Datos de entrada

Debes generar los datos siguiendo estas instrucciones: - Crear una lista
con tres ciudades: Bogotá, Medellín y Cali. - Repetir esa lista hasta
obtener 9,000 elementos.

### 🎯 Objetivo

Reducir el consumo de memoria al almacenar datos categóricos.

### 📝 Instrucciones

1.  Crear la lista de ciudades.
2.  Generar una lista grande repitiendo los valores.
3.  Convertir la lista en una Serie.
4.  Medir el uso de memoria inicial.
5.  Convertir el tipo de dato a categórico.
6.  Medir nuevamente el uso de memoria.
7.  Comparar los resultados.

------------------------------------------------------------------------

## 🔴 Ejercicio 4 --- Corrección de Valores Booleanos

### 📌 Contexto

Un formulario guardó respuestas booleanas como texto en lugar de valores
lógicos reales.

### 📥 Datos de entrada

Lista de estados: - True - False - True - True - False

### 🎯 Objetivo

Transformar los textos en valores booleanos reales y contar los valores
verdaderos.

### 📝 Instrucciones

1.  Crear una Serie con los valores de texto.
2.  Evitar convertir directamente los textos a booleanos.
3.  Generar una serie de valores booleanos reales mediante una
    comparación lógica.
4.  Contar cuántos valores verdaderos existen.

------------------------------------------------------------------------

## 🧩 Nivel de dificultad sugerido

-   Ejercicio 1: Básico -- Intermedio
-   Ejercicio 2: Básico -- Intermedio
-   Ejercicio 3: Intermedio
-   Ejercicio 4: Intermedio

------------------------------------------------------------------------

## 🎯 Propósito de estos ejercicios

Estos ejercicios están diseñados para ayudarte a:

-   Comprender cómo Pandas interpreta distintos tipos de datos.
-   Enfrentar problemas reales de datos sucios.
-   Optimizar el uso de memoria.
-   Aplicar lógica vectorizada.

Dominar estos conceptos es fundamental para el análisis de datos
profesional.

------------------------------------------------------------------------

📌 Recomendación:\
Intenta resolver cada ejercicio sin buscar soluciones inmediatas. El
verdadero aprendizaje está en el proceso.
