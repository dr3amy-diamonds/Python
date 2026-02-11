# 🧠 ¿QUÉ ES INDEXADO?

**Indexado** es la forma de acceder a un elemento específico dentro de un array.

En **NumPy**, cada valor:

- tiene una **posición**
- esa posición se identifica con un **índice**

👉 El indexado responde a la pregunta:

> **“¿Dónde está este dato dentro del conjunto?”**

---

# 🧠 ¿QUÉ ES SLICING?

**Slicing (rebanado)** es la forma de seleccionar **una parte del array**, no un solo valor.

👉 Responde a preguntas como:

- “Quiero los primeros 5 datos”
- “Quiero una columna”
- “Quiero un rango”

📌 En análisis de datos, casi nunca usas un solo valor:  
usas **subconjuntos**.

---

# 🎯 ¿PARA QUÉ SIRVE INDEXADO Y SLICING?

Sirve para:

- ✔ Extraer datos relevantes  
- ✔ Preparar datos para análisis  
- ✔ Limpiar datasets  
- ✔ Seleccionar filas o columnas  
- ✔ Aplicar operaciones solo a una parte  

👉 Es la base de:

- Pandas  
- Machine Learning  
- Visualización  

---

# ❌ ¿POR QUÉ NO BASTA CON LISTAS?

### Con listas:
- necesitas bucles
- código largo
- errores frecuentes

### Con NumPy:
- selección directa
- operaciones rápidas
- código claro

👉 **Indexado y slicing eliminan bucles.**

---

# 🧩 INDEXADO EN NUMPY (CONCEPTUAL)

### 🔹 Indexado positivo
Empieza desde el inicio del array.

### 🔹 Indexado negativo
Empieza desde el final del array.

👉 Es útil cuando:
- no sabes el tamaño exacto
- trabajas con datos dinámicos

---

# 🧠 ARRAYS MULTIDIMENSIONALES

En arrays 2D o más:

- cada dimensión representa algo distinto
- normalmente:
  - **filas** = observaciones
  - **columnas** = variables

📌 Indexar correctamente significa:  
> **“Saber qué representa cada eje”.**

---

# 📐 ¿QUÉ ES UN EJE (axis)?

Un **eje** es una dimensión del array.

Ejemplo conceptual:

- `axis 0` → filas  
- `axis 1` → columnas  

👉 Se usa constantemente en:
- estadísticas
- agregaciones
- filtrado

---

# 🔍 SLICING (REBANADO) — CONCEPTO CLAVE

Slicing te permite:

- tomar rangos
- saltar elementos
- copiar partes

Tiene tres partes conceptuales:

```
[inicio : fin : paso]
```

👉 Es **selectivo**, no destructivo.

---

# ⚠️ DIFERENCIA IMPORTANTE: COPIA vs VISTA

Cuando haces slicing:

- a veces obtienes una **vista**
- no una copia independiente

Esto significa:
- modificar el resultado puede modificar el original

👉 Es crítico entenderlo para no cometer errores.

---

# 🧠 INDEXADO BOOLEANO (IDEA AVANZADA)

NumPy permite seleccionar datos usando **condiciones**.

Ejemplos mentales:

- “Dame los valores mayores que 10”
- “Dame filas que cumplan una condición”

👉 Esto es **pensamiento de analista**, no de programador básico.

---

# 📊 ¿POR QUÉ ES FUNDAMENTAL EN ANÁLISIS DE DATOS?

Porque:

- los datasets reales son grandes
- no analizas todo a la vez
- seleccionas subconjuntos

Indexado y slicing permiten:

- filtrar
- segmentar
- preparar datos

📌 Sin esto, **Pandas se vuelve incomprensible**.

---

# 🧭 ERRORES COMUNES

- ❌ Confundir filas con columnas  
- ❌ No revisar `shape` antes de indexar  
- ❌ Modificar datos sin querer (vista vs copia)  
- ❌ Usar bucles en lugar de slicing  

---

# 🟢 CÓMO SABES QUE LO DOMINAS

Cuando:

- ✔ Piensas en filas y columnas  
- ✔ Sabes qué eje estás usando  
- ✔ Extraes subconjuntos sin bucles  
- ✔ No te pierdes con dimensiones  

---

# 🧠 RESUMEN FINAL

**Indexado y slicing no son sintaxis,  
son una forma de pensar los datos.**

Si entiendes esto:

- NumPy tiene sentido  
- Pandas será natural  
- El análisis de datos fluye 🚀
