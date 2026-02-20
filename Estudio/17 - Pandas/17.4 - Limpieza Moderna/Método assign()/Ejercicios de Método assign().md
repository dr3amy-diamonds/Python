# 📊 Taller Académico: Transformaciones y Lógica Condicional en Pandas

------------------------------------------------------------------------

## 🎯 Objetivo General

Desarrollar la capacidad de transformar, limpiar y enriquecer datos
utilizando un enfoque funcional y encadenado, aplicando herramientas
clave como:

-   Creación de columnas derivadas
-   Transformación de datos tipo texto a numérico
-   Lógica condicional simple y múltiple
-   Clasificación basada en patrones de texto

Este taller está diseñado para fortalecer la comprensión conceptual y
estratégica del análisis de datos en entornos profesionales.

------------------------------------------------------------------------

# 🟢 Ejercicio 1: Limpieza y Matemáticas en un Solo Paso

### 🔎 Enfoque Conceptual

Aplicar una transformación funcional que permita:

1.  Limpiar un dato textual.
2.  Convertirlo a un tipo numérico adecuado.
3.  Realizar inmediatamente una operación matemática con ese dato
    transformado.

### 🎯 Tu Misión

-   Crear un nuevo DataFrame llamado **df_calculado**.
-   Sobrescribir la columna **precio_venta** eliminando el símbolo
    monetario y convirtiendo el resultado en número decimal.
-   En el mismo proceso, crear una nueva columna llamada
    **ganancia_unitaria**.
-   Esta nueva columna debe representar la diferencia entre el precio de
    venta y el precio de costo.

### 🧠 Propósito del Ejercicio

Comprender cómo encadenar transformaciones sin modificar el DataFrame
original y cómo calcular métricas derivadas en el mismo flujo lógico.

------------------------------------------------------------------------

# 🟡 Ejercicio 2: El Semáforo del Inventario

### 🔎 Enfoque Conceptual

Aprender a generar etiquetas categóricas a partir de condiciones
numéricas utilizando lógica condicional vectorizada.

### 🎯 Tu Misión

-   Trabajando sobre el DataFrame resultante del ejercicio anterior,
    crear una nueva columna llamada **alerta_stock**.
-   Aplicar una condición:
    -   Si el **stock_actual** es menor a 10 → asignar el texto
        **"Comprar urgente"**.
    -   En caso contrario → asignar **"Stock suficiente"**.

### 🧠 Propósito del Ejercicio

Entender cómo traducir reglas de negocio en condiciones lógicas
aplicadas de manera masiva sobre los datos.

------------------------------------------------------------------------

# 🟠 Ejercicio 3: Condiciones Múltiples (El Combo Estratégico)

### 🔎 Enfoque Conceptual

Aplicar múltiples condiciones simultáneamente utilizando operadores
lógicos.

### 🎯 Tu Misión

-   Crear una nueva columna llamada **promocion_dia**.

-   Establecer la siguiente regla:

    -   Si la **categoría** es *"Comida"*\
        Y\
        el **stock_actual** es mayor a 10\
        → asignar **"Aplicar 2x1"**.

    -   En cualquier otro caso → asignar **"Precio Normal"**.

### 🧠 Propósito del Ejercicio

Aprender a combinar condiciones y comprender cómo se evalúan expresiones
lógicas compuestas en análisis de datos.

------------------------------------------------------------------------

# 🔴 Ejercicio 4: Clasificación por Categorías de Texto

### 🔎 Enfoque Conceptual

Clasificar registros utilizando patrones dentro de texto.

### 🎯 Tu Misión

-   Crear una nueva columna llamada **tipo_preparacion**.

-   Definir la siguiente regla:

    -   Si el nombre del producto contiene la palabra **"Café"** o
        **"Té"** → asignar **"Barista"**.
    -   En caso contrario → asignar **"Cocina"**.

### 🧠 Propósito del Ejercicio

Desarrollar la capacidad de detectar patrones dentro de columnas de
texto y convertirlos en categorías analíticas.

------------------------------------------------------------------------

# 📚 Recomendaciones Académicas

-   Piensa cada transformación como una etapa de un flujo de datos.
-   Evita modificar datos originales innecesariamente.
-   Mantén claridad entre limpieza, transformación y lógica de negocio.
-   Reflexiona sobre cómo estas operaciones escalan en datasets grandes.

------------------------------------------------------------------------

## 🏁 Resultado Esperado

Al finalizar este taller deberás:

-   Comprender cómo transformar columnas de texto en valores numéricos
    utilizables.
-   Crear métricas derivadas con lógica clara.
-   Implementar clasificación condicional simple y múltiple.
-   Aplicar reglas de negocio basadas en texto.

------------------------------------------------------------------------

**Nivel:** Intermedio\
**Enfoque:** Profesional y orientado a análisis real de datos
