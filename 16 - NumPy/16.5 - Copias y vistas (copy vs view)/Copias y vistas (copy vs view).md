# 🟩 16.5 — Copias y vistas (copy vs view) — NumPy

## Teoría avanzada y fundamentos internos

## 🧠 La idea central (a nivel profundo)

NumPy no trabaja con “valores”, trabaja con:

👉 **bloques de memoria + metadatos**

Un array NumPy es conceptualmente:

- Un bloque de memoria contigua (o no contigua)
- Un conjunto de metadatos que dicen:
  - cómo interpretar esa memoria  
  - qué forma tiene  
  - qué tipo de datos contiene  
  - cómo moverse por ella  

👉 **Copias y vistas no son más que decisiones sobre memoria.**

---

## 🔹 Qué significa “compartir memoria”

Cuando dos arrays:

- apuntan al mismo bloque de memoria  
- pero tienen metadatos distintos  

entonces:

- pueden verse diferentes  
- pero los datos físicos son los mismos  

Modificar uno:

- modifica la memoria  
- y el otro lo “ve” inmediatamente  

📌 Esto es lo que hace posibles las vistas.

---

## 🔹 Las vistas no son “subarrays”

Error conceptual común:

> “Una vista es un array más pequeño dentro de otro”

❌ Incorrecto.

Una vista es:

- el mismo array  
- con otra interpretación:
  - distinto inicio  
  - distinto paso  
  - distinta forma  

📌 No existe una “parte copiada”:  
solo existe una forma diferente de recorrer la misma memoria.

---

## 🔹 Strides (concepto clave)

Los **strides** indican:

- cuántos bytes hay que saltar en memoria  
- para pasar de un elemento al siguiente  

Una vista:

- cambia los strides  
- sin mover datos  

Por eso operaciones como:

- transponer  
- reordenar ejes  
- slicing  

pueden ser:

✔ inmediatas  
✔ sin coste  
✔ sin copia  

---

## 🔹 Memoria contigua vs no contigua

### Memoria contigua
- Datos uno tras otro  
- Ideal para CPU y caché  
- Más rápida  

### Memoria no contigua
- Datos “salteados”  
- Ocurre con algunas vistas  
- Puede ser más lenta  

📌 Algunas operaciones fuerzan copias solo para recuperar contigüidad.  
👉 No por seguridad, sino por rendimiento.

---

## 🔹 Por qué algunas operaciones devuelven copia “sin avisar”

NumPy crea una copia cuando:

- no puede representar la operación solo con metadatos  
- los datos deben reorganizarse físicamente  
- el nuevo tipo de datos requiere más o menos bytes  

📌 La regla no es “esta función copia”  
📌 La regla es “¿puede resolverse solo con metadatos?”

---

## 🔹 Propiedad de los datos (ownership)

Un array puede:

- poseer los datos  
- o solo referenciarlos  

Una vista:

- no es dueña de la memoria  
- depende del array original  

Si el original desaparece:

- la vista puede quedar inválida  

📌 Por eso NumPy gestiona referencias cuidadosamente.

---

## 🔹 Vistas en cadena (peligro silencioso)

Puedes tener:

- vista de una vista  
- vista de una vista de una vista  

Todas apuntando al mismo bloque de memoria original.

Modificar cualquiera:

👉 afecta a todos.

📌 Muy común en pipelines de datos.

---

## 🔹 Copias: seguridad a cambio de coste

Una copia:

- rompe toda relación con el origen  
- garantiza aislamiento  
- consume memoria  
- tarda más  

📌 En datasets grandes, copiar sin pensar puede:
- duplicar RAM  
- afectar rendimiento  
- provocar errores de memoria  

👉 Copiar solo cuando tiene sentido lógico, no por miedo.

---

## 🔹 Decisión clave: ¿quién es el dueño del dato?

Pregunta fundamental:

> “¿Este array representa el dataset original o un resultado derivado?”

- Dataset original → proteger (copiar antes de modificar)  
- Resultado temporal → vista  
- Resultado final → copia  

📌 Esta decisión define la arquitectura del análisis.

---

## 🔹 Relación con ciencia de datos real

En análisis reales:

- slicing para filtrar  
- transformaciones  
- normalización  
- eliminación de outliers  

Si trabajas sobre vistas sin saberlo:

- alteras el dataset base  
- contaminas experimentos  
- invalidas comparaciones  

📌 Muchos bugs en data science no son matemáticos,  
son errores de memoria compartida.

---

## 🔹 Error profesional común

> “No pasa nada, solo estoy modificando esta columna…”

Pero:
- esa columna es una vista  
- se reutiliza más adelante  
- el análisis posterior ya está sesgado  

📌 No hay excepciones  
📌 Solo “resultados raros”

---

## 🔹 Principio de oro

NumPy confía en ti.

No te protege:
- no pregunta  
- no avisa  
- no bloquea  

Porque:
- está diseñado para científicos e ingenieros  
- prioriza control y rendimiento  

👉 Con gran poder, gran responsabilidad.

---

## 🧭 Mapa mental final (avanzado)

✔ Un array = memoria + metadatos  
✔ Vista = mismos datos, otros metadatos  
✔ Copia = nueva memoria  
✔ NumPy evita copiar siempre que pueda  
✔ La seguridad depende del programador  
✔ Entender esto evita errores invisibles
