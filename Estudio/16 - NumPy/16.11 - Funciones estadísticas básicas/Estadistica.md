# 🟩 16.11 — Funciones Estadísticas Básicas (NumPy)

## 🧠 ¿Por qué este tema es clave?

La estadística responde preguntas como:

- ¿Cuál es el valor típico?
- ¿Qué tan dispersos están los datos?
- ¿Hay valores extremos?
- ¿Cómo se distribuyen los datos?

📌 Todo análisis de datos comienza con **estadística descriptiva**.

Antes de trabajar con:
- modelos
- gráficas
- predicciones

primero debes **entender tus datos**.

---

## 🔹 ¿Qué son las funciones estadísticas?

Son operaciones que:

- resumen grandes conjuntos de datos
- convierten miles de valores en información
- permiten comparar y tomar decisiones

NumPy las implementa de forma:

- ✔ rápida
- ✔ vectorizada
- ✔ confiable

---

## 🔸 Medidas de Tendencia Central

### 🔹 Media (`mean`)

**Concepto**  
Promedio aritmético.

📌 Sensible a valores extremos.

**Uso real**
- promedios generales
- métricas globales

**Mala práctica**
- ❌ Usarla sin revisar *outliers*

---

### 🔹 Mediana (`median`)

**Concepto**  
Valor central cuando los datos están ordenados.

📌 Robusta ante valores extremos.

**Uso real**
- ingresos
- tiempos
- datos sesgados

---

### 🔹 Moda (`mode`)

**Concepto**  
Valor que más se repite.

📌 No siempre existe o es único.

**Uso real**
- categorías
- eventos frecuentes

---

## 🔸 Medidas de Dispersión

### 🔹 Varianza (`var`)

**Concepto**  
Mide qué tan alejados están los valores de la media.

- Varianza alta → datos dispersos
- Varianza baja → datos concentrados

---

### 🔹 Desviación estándar (`std`)

**Concepto**  
Raíz cuadrada de la varianza.

📌 Misma unidad que los datos.  
📌 Más intuitiva que la varianza.

**Uso real**
- análisis de riesgo
- control de calidad
- *Machine Learning*

---

### 🔹 Rango (`max - min`)

**Concepto**  
Diferencia entre el valor máximo y mínimo.

📌 Muy sensible a *outliers*.

---

## 🔸 Posición y Distribución

### 🔹 Percentiles

**Concepto**  
Indican la posición relativa de un valor dentro del conjunto.

**Ejemplo**
- Percentil 90 → el 90% de los datos está por debajo

**Uso real**
- notas
- salarios
- rendimiento

---

### 🔹 Cuartiles

**Concepto**  
Dividen los datos en 4 partes iguales.

- Q1 → 25%
- Q2 → 50% (mediana)
- Q3 → 75%

Base del análisis exploratorio.

---

### 🔹 IQR (Rango intercuartílico)

**Concepto**  
IQR = Q3 − Q1

📌 Medida robusta de dispersión  
📌 Ideal para detectar *outliers*

---

## 🔸 Estadísticas sobre Matrices

### 🔹 Estadística por eje (`axis`)

Permite calcular estadísticas:

- por filas
- por columnas

📌 Muy importante en datos tabulares.

**Error común**
- ❌ Confundir `axis=0` y `axis=1`

---

### 🔹 Valores faltantes (`NaN`)

**Concepto**  
Representan datos faltantes o inválidos.

NumPy tiene funciones que:

- ignoran `NaN`
- evitan errores

📌 Crítico en datos reales.

---

## 🚨 Errores comunes

- ❌ Confiar solo en la media
- ❌ Ignorar *outliers*
- ❌ No revisar la distribución
- ❌ Mezclar datos sin normalizar
- ❌ No tratar valores faltantes

---

## 🧠 Buenas prácticas

- ✔ Empieza con estadística descriptiva
- ✔ Usa mediana si hay *outliers*
- ✔ Usa desviación estándar para dispersión
- ✔ Usa percentiles para entender distribución
- ✔ Siempre revisa `NaN`

---

## 🧭 Resumen mental

| Tipo        | Medida              |
|------------|---------------------|
| Tendencia  | mean, median        |
| Frecuencia | mode                |
| Dispersión | var, std, range     |
| Posición   | percentiles         |
| Robusta    | IQR                 |
| Tablas     | axis                |

---

## 🎯 Idea clave final

**Antes de modelar, visualiza y resume.**  
La estadística no es opcional, es el **primer filtro de la verdad**.
