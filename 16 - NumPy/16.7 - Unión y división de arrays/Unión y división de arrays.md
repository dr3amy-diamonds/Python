# 16.7 — UNIÓN Y DIVISIÓN DE ARRAYS (NumPy)
👉 **TEORÍA COMPLETA Y BIEN FUNDAMENTADA**

## 🧠 ¿POR QUÉ ESTE TEMA ES CRÍTICO?

En análisis de datos, los datos **no vienen perfectos**:

- vienen separados  
- vienen en bloques  
- vienen incompletos  
- hay que reorganizarlos  

👉 Unir y dividir arrays es una habilidad esencial para:

- limpieza de datos  
- preparación de datasets  
- machine learning  
- visualización  

---

## 🧠 IDEA CLAVE DEL TEMA

**Unir arrays = controlar shapes + elegir eje correcto**

📌 El **90% de los errores** vienen de:
- shape incompatible  
- eje (`axis`) mal entendido  

---

## 🔹 CONCEPTO FUNDAMENTAL: `axis`

En un array 2D:

```python
shape = (filas, columnas)
```

- `axis=0` → trabaja **verticalmente** (filas)
- `axis=1` → trabaja **horizontalmente** (columnas)

👉 No es intuitivo al principio, pero es **crucial**.

---

## 🟢 UNIÓN DE ARRAYS

### 🔹 `np.concatenate()`

Función base para unir arrays.

**Concepto:**
- une arrays existentes  
- no crea dimensiones nuevas  
- requiere compatibilidad de `shape`  

```python
np.concatenate((a, b), axis=0)
```

✔ Flexible  
❌ Verbosa  
✔ Base de todo lo demás  

---

### 🔹 `np.vstack()`

Apila arrays **verticalmente**.

- aumenta filas  
- mantiene columnas  

**Usos típicos:**
- agregar observaciones  

---

### 🔹 `np.hstack()`

Apila arrays **horizontalmente**.

- aumenta columnas  
- mantiene filas  

**Usos típicos:**
- agregar variables  

---

### 🔹 `np.stack()`

Crea una **nueva dimensión**.

👉 No une, **empaqueta**.

**Usos:**
- crear tensores  
- series temporales  
- imágenes  

---

## 🟢 DIVISIÓN DE ARRAYS

### 🔹 `np.split()`

Divide un array en partes **iguales**.

⚠️ Si no se puede dividir exacto → **error**.

---

### 🔹 `np.array_split()`

Versión **flexible** de `split`.

✔ Permite partes desiguales  
✔ Muy usada en práctica  

---

### 🔹 `np.vsplit()` y `np.hsplit()`

Especializadas para:
- dividir por filas  
- dividir por columnas  

---

### 🔹 CASO CLAVE: ENTRENAMIENTO / PRUEBA

Dividir datos en:
- entrenamiento  
- validación  
- prueba  

👉 Este tema conecta directamente con **Machine Learning**.

---

## 🔴 ERRORES COMUNES

❌ Shapes incompatibles  
❌ Eje incorrecto  
❌ Confundir `stack` con `concatenate`  
❌ No verificar dimensiones  

---

## 🟢 BUENAS PRÁCTICAS

✔ Siempre imprime `shape`  
✔ Dibuja mentalmente el array  
✔ Usa nombres claros  
✔ Verifica antes de unir  
✔ Prefiere funciones específicas (`vstack`, `hstack`)  

---

## 🧠 CONEXIÓN CON PANDAS

Muchas operaciones aquí:
- existen en Pandas  
- funcionan de forma similar  
- pero con más comodidad  

👉 Dominar NumPy hace **Pandas fácil**.

---

## 🧭 RESUMEN MENTAL

✔ `concatenate` → unión base  
✔ `vstack` → filas  
✔ `hstack` → columnas  
✔ `stack` → nueva dimensión  
✔ `split` → división estricta  
✔ `array_split` → flexible  
