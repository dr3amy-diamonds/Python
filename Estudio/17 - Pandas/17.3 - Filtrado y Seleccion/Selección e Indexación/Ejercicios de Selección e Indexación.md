# Ejercicios de Manipulación y Selección de Datos con Pandas

Documento de ejercicios enfocado en comprender el uso de índices,
posiciones y accesos rápidos en DataFrames.\
No incluye código resuelto, solo enunciados y misiones.

------------------------------------------------------------------------

## 🟢 Ejercicio 1: El Menú de la Cafetería

### Contexto

Eres el dueño de una cafetería hipster. Necesitas consultar precios
rápidamente usando el nombre de la bebida como índice.

### Datos de Entrada

**Columna Bebida (ÍNDICE):** - Capuchino - Mocca - Espresso -
Frappuccino - Americano

**Columnas y valores:**

  Bebida        Precio   Calorias   Ventas_Dia
  ------------- -------- ---------- ------------
  Capuchino     3.50     250        10
  Mocca         4.00     300        15
  Espresso      2.50     150        8
  Frappuccino   5.00     450        5
  Americano     3.00     200        12

### Tu Misión

-   **Selección Humana (.loc):** Extrae toda la fila correspondiente a
    **Mocca**.
-   **Selección Robot (.iloc):** Extrae la fila ubicada en la posición
    **2** (el conteo inicia en 0).\
    Identifica qué bebida corresponde a esa posición.
-   **Dato Exacto:** Usa selección por etiqueta para obtener únicamente
    las **Calorias** del **Frappuccino**.

------------------------------------------------------------------------

## 🟡 Ejercicio 2: El Ranking de Netflix

### Contexto

Tienes el Top 5 de películas más vistas hoy. Necesitas crear sub-listas
para analizar el ranking, prestando atención a cómo se realizan los
cortes.

### Datos de Entrada

**Columna Título (ÍNDICE):** - Matrix - Titanic - John Wick - Shrek -
Saw

**Columnas y valores:**

  Título      Vistas   Género
  ----------- -------- ---------
  Matrix      1000     Sci‑Fi
  Titanic     950      Drama
  John Wick   800      Acción
  Shrek       750      Comedia
  Saw         600      Terror

### Tu Misión

-   **Corte con Etiquetas (.loc):** Crea un sub‑DataFrame que vaya desde
    **Matrix** hasta **John Wick**.\
    Observa si el último elemento se incluye.
-   **Corte con Posiciones (.iloc):** Obtén las mismas tres películas
    usando posiciones numéricas.
-   **Reto Mental:** Recuerda que el límite final en selección por
    posición es **exclusivo**.\
    ¿Qué número debes usar para incluir la película ubicada en la
    posición 2?

------------------------------------------------------------------------

## 🟠 Ejercicio 3: El Corrector de Errores

### Contexto

Un pasante ingresó datos incorrectos en el inventario. Debes corregir
precios exagerados y stocks negativos sin dañar el DataFrame.

### Datos de Entrada

  Producto   Stock   Precio
  ---------- ------- --------
  Monitor    10      120
  Mouse      -5      25
  Teclado    50      5000

### Tu Misión

-   Corrige el **Precio** del **Teclado** y cámbialo a **50**.
-   Corrige el **Stock** del **Mouse** y cámbialo a **20**.
-   Muestra el DataFrame final para verificar que los cambios se
    aplicaron correctamente.

------------------------------------------------------------------------

## 🔴 Ejercicio 4: El Francotirador (.at vs .iat)

### Contexto

Velocidad pura. Necesitas extraer un solo dato específico usando accesos
directos optimizados.

### Datos de Entrada

Utiliza el mismo DataFrame del **Ejercicio 1: Cafetería**.

### Tu Misión

-   Usa acceso por etiqueta para obtener el valor exacto de
    **Ventas_Dia** correspondiente al **Americano**.
-   Usa acceso por posición numérica para obtener ese mismo valor.
    -   **Pista:** Identifica la posición de la fila **Americano** y la
        posición de la columna **Ventas_Dia**, contando desde cero.

------------------------------------------------------------------------

📌 **Objetivo General**\
Comprender la diferencia entre selección por etiquetas y por posiciones,
el comportamiento inclusivo y exclusivo de los cortes, y la modificación
segura de datos específicos.
