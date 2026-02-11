# 🧪 Ejercicios de Diagnóstico y Exploración de Datos con Pandas

Este documento contiene una serie de ejercicios diseñados para
desarrollar habilidades de diagnóstico, exploración y análisis de datos
usando Pandas.\
⚠️ **Importante:** Este archivo contiene únicamente los enunciados y
preguntas de análisis. No incluye código ni soluciones.

------------------------------------------------------------------------

## 🟢 Ejercicio 1: El Diagnóstico Técnico (.info)

### 📌 Contexto

Acabas de cargar un pequeño reporte de empleados. A simple vista parece
estar bien, pero tu intuición te dice que hay problemas con los tipos de
datos que impedirán hacer cálculos de fechas o salarios.

### 📥 Datos de Entrada (Texto)

-   **Columna Nombre:**\
    Ana, Carlos, Luis, Maria

-   **Columna Fecha_Ingreso:**\
    2020-01-01, 2021-05-20, 2019-11-15, 2022-03-10\
    *(Nota: Son textos)*

-   **Columna Salario:**\
    2500, 3000, None, 4000\
    *(Nota: Hay un valor nulo None)*

### 🎯 Misiones

1.  Crear el DataFrame con los datos proporcionados.
2.  Ejecutar el método `.info()` activando el conteo real de memoria con
    `memory_usage='deep'`.
3.  Analizar el resultado obtenido.

### 🧠 Preguntas de Análisis

-   ¿Qué tipo de dato (`dtype`) tiene la columna **Fecha_Ingreso** y por
    qué eso es un problema para analizar la antigüedad de los empleados?
-   ¿Cuántos valores **non-null** tiene la columna **Salario**?
-   ¿Ese número coincide con el total de filas del DataFrame? ¿Qué
    implica esa diferencia?

------------------------------------------------------------------------

## 🟡 Ejercicio 2: Sherlock Holmes Matemático (.describe)

### 📌 Contexto

Estás analizando datos médicos de pacientes. Los datos numéricos no
pueden mentir... ¿o sí?\
Debes usar estadística descriptiva para encontrar errores de digitación
que son imposibles en la vida real.

### 📥 Datos de Entrada (Texto)

-   **Pacientes:** A, B, C, D, E
-   **Edad:** 25, 30, -5, 45, 150
-   **Altura_cm:** 170, 165, 180, 160, 10

### 🎯 Misiones

1.  Crear el DataFrame con los datos indicados.
2.  Ejecutar el método `.describe()` sobre el DataFrame.
3.  Interpretar los resultados estadísticos.

### 🧠 Preguntas de Análisis

-   Observando los valores mínimos (`min`) y máximos (`max`), ¿qué error
    lógico encuentras en la columna **Edad**?
-   ¿Es posible que una persona tenga esa edad?
-   ¿Qué error lógico encuentras en la columna **Altura_cm**?
-   ¿Es realista que una persona mida esa altura? ¿Qué tipo de error
    podría ser?

------------------------------------------------------------------------

## 🟠 Ejercicio 3: El Sesgo del Orden (.sample vs .head)

### 📌 Contexto

Tienes un registro de transacciones ordenado por fecha.\
Las primeras transacciones del día siempre son correctas, pero los
errores suelen ocurrir en momentos aleatorios.\
Si solo miras el inicio del dataset, podrías creer que todo está
perfecto.

### 📥 Datos de Entrada (Instrucción de Generación)

1.  Crear una lista con la palabra **"Correcto"** repetida 20 veces.
2.  Cambiar manualmente el elemento en la posición 15 (índice 14) para
    que diga **"ERROR CRÍTICO"**.
3.  Crear un DataFrame con esa lista.

### 🎯 Misiones

1.  Ejecutar `.head(5)` y observar los resultados.
2.  Ejecutar `.sample(10)` varias veces hasta que aparezca el error.
3.  Comparar los resultados entre `.head()` y `.sample()`.

### 🧠 Preguntas de Análisis

-   ¿Por qué `.head()` no muestra el error?
-   ¿Por qué `.sample()` sí puede mostrarlo?
-   Escribe una conclusión conceptual explicando por qué no es
    suficiente validar datos usando solo `.head()`.
-   Reflexiona sobre la idea de Matt Harrison respecto a la exploración
    aleatoria de datos.

------------------------------------------------------------------------

## 🔴 Ejercicio 4: El Mapa de Calor de Nulos (.isna)

### 📌 Contexto

Recibes una encuesta de satisfacción incompleta.\
Antes de presentar resultados, necesitas saber cuánta información falta
y en qué columnas.

### 📥 Datos de Entrada (Texto)

-   **Columna ID:**\
    1, 2, 3, 4, 5

-   **Columna Satisfaccion (1-10):**\
    8, None, 10, None, 5

-   **Columna Comentario:**\
    Bueno, Regular, None, None, Malo

### 🎯 Misiones

1.  Crear el DataFrame con los datos proporcionados, usando valores
    nulos adecuados.
2.  Utilizar `.isna()` y `.sum()` para generar un reporte del conteo de
    valores faltantes.
3.  Analizar el patrón de datos incompletos.

### 🧠 Preguntas de Análisis

-   ¿Cuál es la columna más "sucia" (con mayor cantidad de datos
    faltantes)?
-   ¿Cuántos registros (IDs) tienen datos completos en todas las
    columnas?
-   ¿Qué implicaciones tendría esta falta de datos en un análisis real?

------------------------------------------------------------------------

## 📌 Objetivo General

Estos ejercicios buscan desarrollar una habilidad clave en análisis de
datos:

> **No confiar ciegamente en los datos, sino aprender a diagnosticarlos
> antes de analizarlos.**

Dominar estas técnicas te permitirá detectar errores, inconsistencias y
problemas ocultos en cualquier dataset real.
