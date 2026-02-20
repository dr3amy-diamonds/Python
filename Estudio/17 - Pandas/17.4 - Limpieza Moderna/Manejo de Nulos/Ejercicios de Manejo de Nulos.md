# 🧹 Limpieza Profesional de Datos --- Ejercicios Prácticos

Este documento contiene una serie de ejercicios enfocados en escenarios
reales de limpieza y preparación de datos en un contexto logístico y
financiero.

------------------------------------------------------------------------

## 🟢 Ejercicio 1: Paquetes Fantasmas (Eliminación Crítica)

### 📦 Contexto Real

En logística, un paquete sin **tracking_id** es basura.\
No se puede escanear, no se puede cobrar y no se puede entregar.\
Mantener esa fila solo genera errores en el sistema.

### 🎯 Tu Misión

-   Crea un nuevo DataFrame llamado **df_limpio** (para no dañar el
    original).
-   Elimina las filas que no tengan **tracking_id**.
-   Imprime el resultado.
-   Pista: Usa la opción nuclear, pero quirúrgica.

------------------------------------------------------------------------

## 🟡 Ejercicio 2: Costos Perdidos (Relleno Financiero)

### 💰 Contexto Real

Tienes paquetes (como el TRK-004) que no tienen **costo_envio**.

El departamento financiero necesita cerrar caja hoy.\
La regla de negocio es:

> "Si no hay costo registrado, asume que es una bonificación o error y
> ponle 0 para que la suma no dé error".

### 🎯 Tu Misión

-   Sobre **df_limpio**, selecciona la columna **costo_envio**.
-   Rellena los huecos (NaN) con el valor **0.0**.
-   Verifica imprimiendo la columna.

------------------------------------------------------------------------

## 🟠 Ejercicio 3: El Cronograma Roto (Continuidad de Fechas)

### 📅 Contexto Real

Observa la columna **fecha_registro**.

Solo aparece la fecha cuando cambia el día (01, 02, 03), y las filas
intermedias están vacías.\
Esto es típico de reportes exportados desde Excel.

Necesitas que cada paquete tenga la fecha del día en que fue procesado
(la misma del paquete anterior).

### 🎯 Tu Misión

-   Aplica el método de **relleno hacia adelante (forward fill)** en la
    columna **fecha_registro**.
-   Asegúrate de que no queden fechas vacías (NaT o NaN).

------------------------------------------------------------------------

## 🔴 Ejercicio 4: Auditoría de Estados (Detective de Datos)

### 🕵️ Contexto Real

El paquete **TRK-005** no tiene **estado_entrega**.\
No sabemos dónde está.

El jefe de operaciones te dice:

> "Ponle 'Investigar', pero marca esa fila para que yo sepa que nosotros
> alteramos el dato manualmente".

### 🎯 Tu Misión

-   Crea una columna nueva llamada **estado_desconocido** que sea `True`
    si el estado original era nulo.
-   Rellena los nulos de la columna **estado_entrega** con el texto
    **'Investigar'**.
-   Imprime las columnas **tracking_id**, **estado_entrega** y
    **estado_desconocido** para revisar el resultado.

------------------------------------------------------------------------

## 📌 Objetivo General

Estos ejercicios están diseñados para reforzar habilidades críticas en:

-   Eliminación selectiva de datos inválidos.
-   Imputación controlada de valores faltantes.
-   Continuidad temporal en registros.
-   Auditoría y trazabilidad de modificaciones.

------------------------------------------------------------------------

**Recuerda:**\
No modifiques el DataFrame original directamente.\
Trabaja siempre sobre una copia cuando estés limpiando datos críticos.
