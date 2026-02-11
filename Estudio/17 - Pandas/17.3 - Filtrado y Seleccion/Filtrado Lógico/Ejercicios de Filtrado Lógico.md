# 🧠 Ejercicios de Filtrado y Lógica con Pandas

Este documento contiene una serie de ejercicios prácticos diseñados para
aprender y reforzar el uso de **máscaras booleanas**, **operadores
lógicos** y **métodos profesionales de filtrado** en Pandas.\
No incluye soluciones en código: el objetivo es que practiques el
razonamiento y la implementación por tu cuenta.

------------------------------------------------------------------------

## 🟢 Ejercicio 1: El Portero de Discoteca (Filtro Simple)

### Contexto

Eres el guardia de seguridad de un club exclusivo. Tu única orden es
dejar pasar a las personas que sean **mayores de edad (18 años o
más)**.\
Tienes una lista de personas esperando en la fila.

### Datos de Entrada

-   **Columna Nombre**: Juan, Sofia, Mateo, Lucia, Pedro\
-   **Columna Edad**: 15, 19, 25, 17, 18

### Tu Misión

1.  Crear el DataFrame `df_club`.
2.  Crear una variable llamada `mascara_mayores` que contenga la
    condición lógica *(edad \>= 18)*.
3.  Imprimir la máscara para observar los valores `True` y `False`.
4.  Usar esa máscara para filtrar el DataFrame.
5.  Guardar el resultado en `df_admitidos`.
6.  Mostrar el DataFrame filtrado.

📌 **Resultado esperado**: Deberían aparecer **Sofia, Mateo y Pedro**.

------------------------------------------------------------------------

## 🟡 Ejercicio 2: Recursos Humanos (Lógica AND)

### Contexto

Estás contratando un **Programador Senior**.\
La empresa tiene **dos requisitos obligatorios**, y el candidato debe
cumplir **ambos**:

-   Saber **Python**.
-   Tener **más de 3 años de experiencia**.

### Datos de Entrada

-   **Columna Candidato**: Ana, Luis, Marta, Javi\
-   **Columna Lenguaje**: Python, Java, Python, Python\
-   **Columna Experiencia**: 2, 5, 4, 1

### Tu Misión

1.  Crear el DataFrame `df_rrhh`.
2.  Crear una máscara lógica compleja usando el operador `&`.
3.  Recordar encerrar **cada condición entre paréntesis**.
4.  Filtrar el DataFrame usando esa máscara.
5.  Mostrar el candidato que cumple **ambos requisitos**.

📌 **Pista lógica**:\
- Lenguaje igual a Python **Y** experiencia mayor a 3.

------------------------------------------------------------------------

## 🟠 Ejercicio 3: El Bibliotecario Eficiente (`isin` y `between`)

### Contexto

Tienes un catálogo de libros.\
Un cliente solicita:

> "Libros publicados en los **años 90 (1990--1999)** y que sean de
> **Terror** o **Ciencia Ficción**."

Para evitar código largo con muchos operadores OR y AND, usarás métodos
más limpios y profesionales.

### Datos de Entrada

-   **Columna Título**: Libro A, Libro B, Libro C, Libro D, Libro E\
-   **Columna Año**: 1995, 2005, 1998, 1992, 2020\
-   **Columna Género**: Terror, Romance, Ciencia Ficcion, Terror,
    Historia

### Tu Misión

1.  Crear el DataFrame `df_biblioteca`.
2.  Crear una máscara para el año usando `.between(1990, 1999)`.
3.  Crear una máscara para el género usando
    `.isin(['Terror', 'Ciencia Ficcion'])`.
4.  Combinar ambas máscaras con el operador `&`.
5.  Mostrar los libros que cumplen **ambas condiciones**.

------------------------------------------------------------------------

## 🔴 Ejercicio 4: Control de Calidad (`~ NOT` y `.query()`)

### Contexto

En una fábrica, los productos pueden tener los estados:

-   OK\
-   Defectuoso\
-   Pendiente

Tu jefe solicita:

> "Dame el reporte de **todo lo que NO esté 'OK'** y que además tenga un
> **peso menor a 50 gramos**."

### Datos de Entrada

-   **Columna Producto**: Tornillo, Tuerca, Clavo, Arandela\
-   **Columna Estado**: OK, Defectuoso, OK, Pendiente\
-   **Columna Peso**: 10, 45, 12, 30

### Tu Misión (Doble Vía)

#### 🔹 Vía Clásica (Negación)

1.  Crear una máscara usando el operador `~` para expresar **NO es OK**.
2.  Combinar esa condición con `peso < 50` usando `&`.
3.  Filtrar el DataFrame con la máscara resultante.

#### 🔹 Vía Harrison (`.query()`)

1.  Realizar el mismo filtrado usando una sola línea con `.query()`.
2.  Escribir la condición completa dentro de una cadena de texto.

📌 **Pista para `.query()`**:\
- Puedes usar expresiones como:\
`Estado != 'OK' and Peso < 50`

### Paso Final

-   Comparar ambos resultados.
-   Verificar si los DataFrames obtenidos son **idénticos**.

------------------------------------------------------------------------

📘 **Objetivo general**\
Dominar el filtrado de datos con Pandas usando: - Máscaras booleanas -
Operadores lógicos (`&`, `|`, `~`) - Métodos avanzados (`isin`,
`between`, `query`)

Cuando estos patrones se vuelven automáticos, Pandas deja de ser confuso
y empieza a sentirse elegante.
