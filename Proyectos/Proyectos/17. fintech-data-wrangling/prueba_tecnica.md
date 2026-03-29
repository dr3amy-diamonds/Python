# 📩 Prueba Técnica — Auditoría de Transacciones 2023

**De:** Sofía Reyes, Directora de Riesgos (Chief Risk Officer)
**Para:** Valentina, Candidata a Data Analyst
**Asunto:** Prueba Técnica - Auditoría de Transacciones 2023

---

## Contexto

Gracias por avanzar a la etapa final de nuestro proceso de selección. Para evaluar tus habilidades técnicas y tu criterio de negocio, te hemos compartido una extracción cruda de nuestra base de datos de transacciones del año 2023 (`transacciones_fintech_2023.csv`).

> ⚠️ El sistema anterior tenía fallos graves, por lo que los datos están **sumamente sucios**. Necesito que prepares un **Jupyter Notebook** que limpie esta información y entregue respuestas concretas a las siguientes problemáticas de negocio.

---

## 🧹 1. Estandarización y Calidad de Datos (Data Wrangling)

Nuestra base de datos es un desastre. Necesito que consolides la información bajo un único estándar para poder analizarla:

### 1.1 Unificación de Fechas
- Unifica la columna de fechas a un **formato estándar de Pandas**.
- ⚠️ Ten cuidado: el sistema guardó fechas **europeas**, **americanas** y **formatos de tiempo Unix** mezclados.

### 1.2 Consolidación de Nombres de Comercios
- No sirve tener `"AMAZON.COM"`, `"amzn"` y `"Amazon"` como cosas separadas.
- Identifica las **5 marcas principales** y unifica su escritura.

### 1.3 Estandarización del Estado de Transacción
- Estandariza los valores de la columna `status`.

### 1.4 Eliminación de Duplicados
- Elimina cualquier transacción cobrada dos veces (**duplicados exactos**).

---

## 💱 2. Normalización Financiera

Tenemos clientes pagando en **USD, EUR, COP y GBP**. Para el reporte financiero global, todas las transacciones deben estar convertidas a **USD (Dólares)** en una nueva columna.

**Tasas de cambio estándar aproximadas a utilizar:**

| Moneda | Tasa |
|--------|------|
| 1 EUR  | = 1.10 USD |
| 1 GBP  | = 1.25 USD |
| 4000 COP | = 1 USD |
| 1 USD  | = 1 USD |

---

## 🔍 3. Detección de Anomalías y Fraude

El equipo de prevención de fraude necesita aislar comportamientos extraños:

### 3.1 Filtrado de Transacciones
- **Excluye del análisis principal** las transacciones fallidas (`Failed`) y los reembolsos (valores negativos).

### 3.2 Identificación de Outliers
- Identifica las transacciones sospechosamente altas.
- Entrega una **tabla** que muestre únicamente las transacciones que superen los **$10,000 USD**.
- Responde: ¿A qué comercio se le está inyectando ese dinero anómalo?

---

## 📊 4. Inteligencia de Cliente y Cierre

> Usando **solo** las transacciones exitosas, estandarizadas y convertidas a USD (excluyendo el fraude mayor a $10,000):

### 4.1 Análisis de Amazon
- ¿Cuál es el **mes** en el que los usuarios gastan más dinero en **"Amazon"**?

### 4.2 Visualización de Volumen Mensual
- Genera un **gráfico** que muestre el volumen total gastado **mes a mes** en toda la plataforma.

---

## 🗺️ Criterios de Evaluación

Se evaluará:
- La **eficiencia** del código
- La **limpieza** (pipelines)
- Tus **conclusiones**

---

## 🛠️ Herramientas y Funciones Sugeridas

El proyecto requerirá que busques en la documentación de Pandas cosas que quizás no hemos visto tan a fondo:

| Tarea | Herramienta sugerida |
|-------|---------------------|
| Arreglar fechas | `pd.to_datetime(..., errors='coerce')` o funciones personalizadas |
| Limpiar nombres de comercios | `.str.replace()` o diccionarios con `.map()` |
| Eliminar duplicados | `.drop_duplicates()` |
| Conversión de moneda según columna | Lógica condicional con `np.where` o cruces |

---

*Atentamente,*
**Sofía Reyes**
*Chief Risk Officer*
