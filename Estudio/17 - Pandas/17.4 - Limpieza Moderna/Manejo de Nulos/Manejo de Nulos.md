# 📘 Teoría: Manejo de Datos Faltantes (Nulos)

------------------------------------------------------------------------

## 1. ¿Qué es un "Nulo"?

En Python y Pandas, un nulo **no es** el número cero (0) ni una cadena
vacía ("").\
Es la **ausencia total de información**. Es un vacío en el espacio de
datos.

Pandas utiliza principalmente dos representaciones:

-   **NaN (Not a Number)**: Estándar clásico basado en números
    flotantes.
-   **`<NA>`{=html} / None**: Estándar moderno que permite trabajar con
    enteros y texto sin convertirlos en flotantes.

------------------------------------------------------------------------

## 2. ¿Por qué existen los nulos? (El Mundo Real)

En el entorno laboral, los datos faltantes aparecen por razones
específicas que deben analizarse antes de eliminarlos.

### • Error de usuario

Alguien olvidó completar un campo en un formulario.

### • Fallo del sistema

Un sensor dejó de registrar datos durante cierto período.

### • Unión de datos (Merge)

Al cruzar tablas, pueden generarse vacíos cuando no existe coincidencia
entre registros.

### • Lógica de negocio (Muy importante)

A veces, un nulo tiene significado propio.

Ejemplo:\
Si en una columna `fecha_baja_servicio` el valor es nulo, puede
significar que el cliente sigue activo.\
Eliminar esos nulos podría eliminar información crítica.

------------------------------------------------------------------------

## 3. ¿Por qué son peligrosos? (El Efecto Viral)

Los nulos pueden propagarse y afectar cálculos y modelos.

### • En sumas

Un solo nulo puede anular el resultado completo.

### • En promedios

Puede generar resultados sesgados si no se manejan correctamente.

### • En Machine Learning

Muchos modelos no aceptan datos con valores faltantes y generarán
errores.

------------------------------------------------------------------------

# 🛠️ Estrategias de Solución

En el entorno profesional existen tres enfoques principales para tratar
datos faltantes.

------------------------------------------------------------------------

## Estrategia A: Eliminación (dropna)

Consiste en borrar filas o columnas que contienen nulos.

### Cuándo usarla:

-   Cuando el porcentaje de datos faltantes es muy bajo.
-   Cuando la fila pierde sentido sin ese dato.

### Riesgo:

-   Puede eliminar información valiosa en otras columnas.

------------------------------------------------------------------------

## Estrategia B: Imputación (fillna)

Consiste en rellenar el valor faltante con una estimación.

### Formas comunes:

-   Con un valor constante (0, "Desconocido", etc.)
-   Con el promedio o la mediana de la columna.

### Riesgo:

-   Se están generando datos artificiales.
-   Puede introducir sesgo si se usa sin análisis previo.

------------------------------------------------------------------------

## Estrategia C: Interpolación (interpolate)

Método usado principalmente en series de tiempo.

Se estiman valores faltantes basándose en puntos anteriores y
posteriores.

### Cuándo usarla:

-   En datos cronológicos donde los valores siguen una tendencia
    progresiva.

------------------------------------------------------------------------

# 🧰 Métodos y Funciones Clave

## 1. Detección

Antes de actuar, se debe diagnosticar.

-   `isna()` / `isnull()` → Detectan valores faltantes.
-   `notna()` → Detecta valores válidos.
-   `info()` → Muestra cantidad de datos no nulos por columna.

------------------------------------------------------------------------

## 2. Eliminación

-   `dropna()` → Elimina filas o columnas con valores faltantes.
-   Puede configurarse para eliminar solo si toda la fila está vacía.
-   Permite especificar columnas concretas para evaluar.

------------------------------------------------------------------------

## 3. Relleno

-   `fillna(valor)` → Rellena con un valor fijo.
-   Relleno con promedio o mediana.
-   `ffill()` → Copia el último valor válido hacia adelante.
-   `bfill()` → Copia el siguiente valor válido hacia atrás.

------------------------------------------------------------------------

# 💡 Consejo Profesional (Buenas Prácticas)

## 🎯 El Consejo de Oro (Nivel Profesional)

En el mundo laboral del análisis de datos, existe una regla que separa a
un analista junior de uno senior:

> **Nunca rellenes un valor nulo sin dejar evidencia de que lo
> hiciste.**

Cuando imputas datos (por ejemplo, reemplazar valores faltantes con el
promedio), estás modificando la realidad original del dataset.\
Si no dejas rastro, nadie podrá saber qué datos eran reales y cuáles
fueron creados artificialmente.

------------------------------------------------------------------------

## ❌ Enfoque Junior (Mala práctica)

``` python
df['edad'] = df['edad'].fillna(30)
```

### Problema:

-   Se pierden los valores originales nulos.
-   No hay forma de distinguir datos reales de datos imputados.
-   Se compromete la trazabilidad.
-   En auditorías futuras, no habrá evidencia de manipulación.

Este tipo de práctica puede generar errores graves en análisis
posteriores.

------------------------------------------------------------------------

## ✅ Enfoque Senior (Estilo Profesional)

``` python
(
    df
    .assign(edad_es_imputada=lambda x: x['edad'].isna())
    .assign(edad=lambda x: x['edad'].fillna(30))
)
```

### ¿Qué está ocurriendo aquí?

1.  **Primero se crea una columna bandera (`edad_es_imputada`)**
    -   Marca con `True` los valores que originalmente eran nulos.
    -   Marca con `False` los valores que ya existían.
2.  **Luego se realiza la imputación**
    -   Se rellenan los valores nulos con el promedio (30 en este
        ejemplo).
    -   Pero ahora existe evidencia de qué filas fueron modificadas.

------------------------------------------------------------------------

## 🧠 ¿Por qué esto es importante?

### 🔎 1. Trazabilidad

Permite saber meses después qué datos fueron alterados.

### 🧾 2. Auditoría

Si alguien cuestiona el análisis, puedes demostrar qué transformaciones
hiciste.

### 📊 3. Modelado

En Machine Learning, las variables bandera pueden incluso mejorar el
rendimiento del modelo.

### 🛡 4. Transparencia profesional

Un analista senior protege la integridad del dato original.

------------------------------------------------------------------------

## 📌 Regla Profesional

Si modificas datos:

-   Marca la modificación.
-   Documenta la transformación.
-   Mantén evidencia.

En análisis de datos, **la memoria humana falla, pero las columnas no.**


------------------------------------------------------------------------

# 🧠 Conclusión

Los valores nulos no son simples errores:\
son eventos que cuentan una historia.

Antes de eliminarlos o rellenarlos, es fundamental comprender:

-   Por qué existen.
-   Qué impacto tienen.
-   Qué estrategia es más adecuada según el contexto.

Un analista senior no elimina datos por reflejo.\
Primero investiga. Luego decide.
