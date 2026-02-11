# 🗂️ Portafolio de Análisis de Datos

## 📝 TUS 4 MISIONES PARA EL PORTAFOLIO

A partir de aquí, tú escribes el código en celdas nuevas.

------------------------------------------------------------------------

## 🔻 Misión 1: La Carga Profesional

Carga el archivo que acabas de crear, pero hazlo como un analista real.

1.  Usa `pd.read_csv()` para leer `'propiedades_raw.csv'`.
2.  Dentro del `read_csv`, usa el parámetro `index_col='id_propiedad'`
    para que los IDs (`PROP_001`, etc.) se conviertan automáticamente en
    tu Índice.
3.  Guarda esto en una variable llamada `df`.
4.  Muestra las primeras 5 filas con `.head()` para comprobar que el
    índice se cargó bien.

------------------------------------------------------------------------

## 🔻 Misión 2: Limpieza Quirúrgica (Usando `.loc`)

El gerente detectó 3 errores graves en el sistema. Arréglalos usando
`.loc`:

1.  La propiedad **PROP_006** tiene un precio negativo. Cámbialo a
    **50000.00**.
2.  La propiedad **PROP_011** tiene el barrio mal escrito ('Palrrrmo').
    Cámbialo a **'Palermo'**.
3.  La propiedad **PROP_021** dice que tiene 0 habitaciones. Cámbialo a
    **1**.

> Recuerda la sintaxis general:\
> `df.loc['Nombre_Fila', 'Nombre_Columna'] = nuevo_valor`

------------------------------------------------------------------------

## 🔻 Misión 3: El Cliente Exigente (Boolean Masking)

Un cliente inversionista te pidió una lista de propiedades con estas
condiciones estrictas:

1.  El precio debe ser **menor a 200,000 USD**.
2.  **Y** el barrio debe ser **'Belgrano' o 'Recoleta'**.

Sugerencias:

-   Crea la máscara usando `&` y `|`.
-   Coloca cada condición entre paréntesis `()`.
-   Para el barrio puedes usar `.isin(['Belgrano', 'Recoleta'])`.

### Tarea:

-   Guarda las casas que pasen el filtro en una variable llamada
    `oportunidades`.
-   Muestra el resultado.

------------------------------------------------------------------------

## 🔻 Misión 4: El Reporte Rápido (Usando `.iloc`)

Tu jefe tiene una reunión en 5 minutos y te pide un resumen rápido:

1.  Extrae solo las propiedades que están en las **posiciones de la 10 a
    la 15** (recuerda que el límite final en `.iloc` no se incluye).
2.  De esas propiedades, muéstrale **solamente la columna en la posición
    1 (barrio) y la posición 2 (precio_usd)**.

Sintaxis de referencia:

`df.iloc[fila_inicio : fila_fin, [col_1, col_2]]`

------------------------------------------------------------------------

## 🎯 Objetivo del Portafolio

Demostrar dominio de:

-   Carga profesional de datos.
-   Corrección precisa con `.loc`.
-   Filtrado avanzado con máscaras booleanas.
-   Selección estratégica con `.iloc`.

Este documento contiene únicamente las instrucciones estructuradas.\
El código debe desarrollarse por separado.
