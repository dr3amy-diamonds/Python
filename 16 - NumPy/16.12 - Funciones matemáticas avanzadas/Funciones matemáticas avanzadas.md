# 🟩 16.12 --- Funciones Matemáticas Avanzadas (NumPy)

## 🧠 ¿Por qué este tema es importante?

Las funciones matemáticas avanzadas sirven para:

-   Transformar datos\
-   Normalizar escalas\
-   Corregir distribuciones\
-   Preparar datos para modelos\
-   Trabajar con fenómenos no lineales

📌 Aquí **NumPy** deja de ser solo números y se vuelve una **herramienta
analítica**.

Sin este tema:

-   Los modelos fallan\
-   Las estadísticas engañan\
-   Los datos no son comparables

------------------------------------------------------------------------

## 🔹 ¿Qué se considera "matemática avanzada" en NumPy?

No es cálculo abstracto complejo.\
Es **matemática aplicada a datos reales**.

Incluye:

-   Exponenciales y logaritmos\
-   Potencias y raíces\
-   Trigonometría\
-   Redondeo inteligente\
-   Normalización\
-   Transformación de escalas\
-   Manejo numérico estable

------------------------------------------------------------------------

## 🔸 Exponenciales y logaritmos

### 🔹 Exponencial

**Concepto:**\
Modela crecimiento, decaimiento y procesos multiplicativos.

**Usos reales:**

-   Crecimiento poblacional\
-   Interés compuesto\
-   Funciones de activación en ML

📌 Crece muy rápido.

### 🔹 Logaritmos

**Concepto:**\
Operación inversa del exponencial.

**Usos reales:**

-   Reducir escalas\
-   Corregir asimetrías\
-   Análisis financiero\
-   Datos muy dispersos

📌 Transforman multiplicación en suma.

------------------------------------------------------------------------

## 🔸 Potencias y raíces

### 🔹 Potencias

**Concepto:**\
Elevar valores a una potencia.

**Usos reales:**

-   Penalizaciones\
-   Escalamiento\
-   Métricas de error

### 🔹 Raíces

**Concepto:**\
Inverso de las potencias.

**Usos reales:**

-   Normalización\
-   Distancias\
-   Desviación estándar

------------------------------------------------------------------------

## 🔸 Trigonometría

### 🔹 Funciones trigonométricas

Incluyen:

-   Seno\
-   Coseno\
-   Tangente

**Usos reales:**

-   Señales\
-   Ondas\
-   Rotaciones\
-   Simulaciones físicas

📌 NumPy trabaja en **radianes**, no en grados.

------------------------------------------------------------------------

## 🔸 Redondeo y aproximación

### 🔹 Redondeo clásico

Permite:

-   Limitar decimales\
-   Limpiar resultados\
-   Mostrar datos

📌 No cambia el significado matemático, solo la representación.

### 🔹 Redondeo hacia arriba / abajo

**Usos reales:**

-   Límites\
-   Intervalos\
-   Discretización

------------------------------------------------------------------------

## 🔸 Normalización y escalado

### 🔹 Normalización

**Concepto:**\
Llevar los datos a un rango común.

**Usos reales:**

-   Machine Learning\
-   Comparación de variables\
-   Distancias entre observaciones

### 🔹 Estandarización

**Concepto:**

-   Media = 0\
-   Desviación estándar = 1

**Usos reales:**

-   Regresión\
-   Clustering\
-   PCA

📌 Muy usada antes de entrenar modelos.

------------------------------------------------------------------------

## 🔸 Estabilidad numérica

### 🔹 Problemas numéricos comunes

En datos reales aparecen:

-   Números muy grandes\
-   Números muy pequeños\
-   Errores de precisión

NumPy incluye funciones que:

-   Evitan *overflow*\
-   Evitan *underflow*\
-   Mantienen la precisión

📌 Fundamental en ciencia de datos.

------------------------------------------------------------------------

## 🔸 Operaciones combinadas

### 🔹 Composición de funciones

**Concepto:**\
Aplicar varias transformaciones en cadena.

**Usos reales:**

-   Pipelines de datos\
-   Limpieza\
-   Preparación de modelos

📌 NumPy permite hacerlo de forma **vectorizada**.

------------------------------------------------------------------------

## 🚨 Errores comunes

-   ❌ Usar logaritmos sin revisar ceros\
-   ❌ Mezclar grados con radianes\
-   ❌ Redondear demasiado pronto\
-   ❌ No escalar datos antes de modelos\
-   ❌ Ignorar estabilidad numérica

------------------------------------------------------------------------

## 🧠 Buenas prácticas

-   ✔ Revisa rangos antes de aplicar funciones\
-   ✔ Usa log para datos sesgados\
-   ✔ Normaliza antes de comparar\
-   ✔ Documenta transformaciones\
-   ✔ Piensa en estabilidad numérica

------------------------------------------------------------------------

## 🧭 Resumen mental

  Necesidad          Tipo de función
  ------------------ -----------------
  Crecimiento        Exponencial
  Reducir escala     Logaritmo
  Escalar            Potencias
  Distancias         Raíces
  Ondas              Trigonometría
  Limpieza           Redondeo
  Comparar           Normalización
  Machine Learning   Estandarización

------------------------------------------------------------------------

## 🎯 Idea clave final

Las funciones matemáticas avanzadas **no son opcionales**.\
Son lo que convierte **datos crudos** en **datos analizables**.
