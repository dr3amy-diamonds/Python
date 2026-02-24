# 📘 Cruce de Datos en Pandas

## 1. ¿Qué es y para qué sirve?

El **cruce de datos** es el proceso de combinar dos o más tablas
(DataFrames) basándose en:

-   Una columna en común (llamada *llave* o *key*).
-   O apilándolas una sobre otra.

Su propósito principal es **enriquecer los datos**.

### Ejemplo Conceptual

Si tienes una tabla de **Ventas** que solo contiene:

-   `id_producto = 101`

No puedes generar un reporte comprensible. Necesitas cruzarla con una
tabla de **Productos** para saber que:

-   El producto 101 es una *Laptop*.
-   Su precio es *\$1000*.

El cruce transforma datos técnicos en información útil para el negocio.

------------------------------------------------------------------------

# 2. Los Dos Gigantes del Cruce: `merge()` y `concat()`

En Pandas existen varias formas de unir datos, pero en el entorno
laboral el 95% de los casos se resuelven con:

-   `merge()` → Cruce inteligente basado en llaves.
-   `concat()` → Apilado de estructuras.

Ambas funciones cumplen propósitos completamente distintos.

------------------------------------------------------------------------

# 🛠️ Función 1: `pd.merge()` (El Cruce Inteligente)

Es el equivalente en Pandas a:

-   Los **JOINs** en SQL.
-   La función **BUSCARV (VLOOKUP)** en Excel.

Se utiliza cuando se desea unir columnas de dos tablas diferentes usando
un identificador común (ej. ID de cliente, código de producto, número de
pedido).

Su parámetro más importante es:

-   `how` → Define la regla del cruce.

------------------------------------------------------------------------

## Tipos de JOIN en `merge()`

### A. INNER JOIN (`how='inner'`) -- El Exclusivo

**¿Qué hace?**\
Mantiene únicamente las filas donde la llave existe en ambas tablas.

**Aplicación en el mundo real:**\
Si tienes una lista de:

-   Clientes que abrieron un correo.
-   Clientes que realizaron una compra.

Un INNER JOIN mostrará únicamente los clientes que hicieron ambas
acciones.

------------------------------------------------------------------------

### B. LEFT JOIN (`how='left'`) -- El Rey del Mundo Laboral 👑

**¿Qué hace?**\
Mantiene toda la tabla de la izquierda (tabla principal) y agrega la
información de la tabla derecha cuando exista coincidencia.\
Si no la hay, completa con valores nulos (NaN).

**Aplicación en el mundo real:**\
Si tienes una tabla de **Ventas** y quieres añadir la **Ubicación del
Cliente**, no deseas perder ninguna venta aunque el cliente no tenga
ubicación registrada.

Este es el tipo de cruce más utilizado en análisis de datos profesional.

------------------------------------------------------------------------

### C. RIGHT JOIN (`how='right'`) -- El Inverso

**¿Qué hace?**\
Mantiene toda la tabla de la derecha.

**Nota práctica:**\
Es poco utilizado, ya que normalmente se invierte el orden de las tablas
y se usa un LEFT JOIN.

------------------------------------------------------------------------

### D. OUTER JOIN / FULL JOIN (`how='outer'`) -- El Inclusivo

**¿Qué hace?**\
Incluye todos los registros de ambas tablas.\
No excluye ningún dato aunque no exista coincidencia.

**Aplicación en el mundo real:**\
En una fusión empresarial, se desea construir una lista maestra con
todos los empleados de ambas empresas, sin eliminar a nadie.

------------------------------------------------------------------------

# 🛠️ Función 2: `pd.concat()` (El Apilador)

A diferencia de `merge()`:

-   `merge()` busca coincidencias y une columnas por llave.
-   `concat()` simplemente apila estructuras.

Su parámetro principal es:

-   `axis` → Define el eje de unión.

------------------------------------------------------------------------

## Tipos de Apilado con `concat()`

### A. Apilado Vertical (`axis=0`) -- El Más Común

**¿Qué hace?**\
Coloca una tabla debajo de la otra.

**Aplicación en el mundo real:**\
Si recibes archivos separados con:

-   Ventas de Enero.
-   Ventas de Febrero.

Y ambas tienen exactamente las mismas columnas, puedes unirlas en una
sola tabla consolidada.

------------------------------------------------------------------------

### B. Apilado Horizontal (`axis=1`)

**¿Qué hace?**\
Coloca una tabla al lado de la otra.

**Condición clave:**\
El índice debe coincidir correctamente entre ambas estructuras.

**Aplicación en el mundo real:**\
Si generas una columna de predicciones con un modelo y deseas añadirla
al DataFrame original.

------------------------------------------------------------------------

# 🧠 Resumen Estratégico: Reglas de Oro

### Usa `pd.concat()` cuando:

-   Tienes archivos de diferentes meses o años.
-   Las columnas son iguales.
-   Necesitas unirlos en una sola tabla larga.

→ Concepto clave: **Apilar**

------------------------------------------------------------------------

### Usa `pd.merge(how='left')` cuando:

-   Tienes códigos (ej. id_vendedor).
-   Necesitas traer información descriptiva desde otra tabla.

→ Concepto clave: **Buscar y enriquecer sin perder datos**

------------------------------------------------------------------------

### Usa `pd.merge(how='inner')` cuando:

-   Quieres ver únicamente registros que existan en ambas bases
    simultáneamente.

→ Concepto clave: **Intersección**

------------------------------------------------------------------------

# 🎯 Conclusión Académica

El cruce de datos es una de las habilidades más importantes en análisis
profesional.

Comprender la diferencia entre:

-   Cruce por llave (`merge`)
-   Apilado estructural (`concat`)

Permite construir reportes confiables, enriquecer información y evitar
errores de interpretación.

Dominar estas funciones es esencial para cualquier analista de datos que
trabaje con Pandas.
