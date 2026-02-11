# 🐼 Pandas – Optimización de Carga y Lectura de Datos

Este documento contiene una serie de ejercicios conceptuales diseñados para comprender **cómo cargar datos de forma eficiente en Pandas**, optimizando memoria, tipos de datos y formatos de almacenamiento.

> ⚠️ **Nota importante:**  
> Este archivo **NO contiene código resuelto**, únicamente las consignas, contextos y misiones de cada ejercicio.

---

## 🟢 Ejercicio 1: La Dieta de Columnas (`usecols`)

### Contexto
El departamento de IT envía un log de servidor gigantesco con decenas de columnas técnicas irrelevantes.  
Tu jefe solo necesita dos cosas:
- **Cuándo ocurrió el error**
- **Qué mensaje produjo**

### Datos de Entrada
Debes crear un archivo llamado **`log_servidor.csv`** con las siguientes columnas:

- **Fecha**:  
  - 2024-01-01  
  - 2024-01-02  
  - 2024-01-03  

- **IP** (dato irrelevante):  
  - 192.168.1.1  
  - 127.0.0.1  
  - 10.0.0.1  

- **Usuario** (dato irrelevante):  
  - Admin  
  - Guest  
  - Root  

- **Mensaje**:  
  - Error 404  
  - Login OK  
  - Timeout  

### Tu Misión
1. Cargar el archivo completo en un DataFrame llamado **`df_gordo`** y medir su uso de memoria.
2. Cargar nuevamente el archivo en **`df_flaco`**, usando `usecols` para traer **solo Fecha y Mensaje**.
3. Comparar el uso de memoria entre ambos.
4. Reflexionar:  
   > ¿Por qué cargarías la IP si nadie te la pidió?

---

## 🟡 Ejercicio 2: El Traductor Anticipado (`dtype` & `parse_dates`)

### Contexto
El sistema exporta datos con problemas comunes:
- Los códigos de sucursal pierden ceros a la izquierda.
- Las fechas llegan como texto.

Debes **corregir esto durante la carga**, no después.

### Datos de Entrada
Crea un archivo llamado **`sucursales.csv`** con:

- **fecha** (texto):
  - 01/01/2024  
  - 02/01/2024  

- **sucursal_id** (texto, conserva ceros):
  - 001  
  - 002  

- **tipo_tienda**:
  - A  
  - B  

### Tu Misión
1. Definir un diccionario de tipos (`tipos = {...}`):
   - `sucursal_id` como texto (`object`)
   - `tipo_tienda` como categoría
2. Usar ese diccionario en el parámetro `dtype` al cargar el CSV.
3. Usar `parse_dates` para convertir la columna fecha automáticamente.
4. Imprimir `.info()` para verificar:
   - `sucursal_id` **no es int**
   - `fecha` es `datetime64`

---

## 🟠 Ejercicio 3: El Desfile de Hormigas (`chunksize`)

### Contexto
Simulas un archivo gigantesco, pero tu memoria solo permite procesar **2 filas a la vez**.  
Debes calcular una suma total sin cargar todo el archivo en memoria.

### Datos de Entrada
Crea un archivo llamado **`mini_bigdata.csv`** con una sola columna:

- **valor**:  
  - Números del 1 al 10

### Tu Misión
1. Crear un iterador usando `pd.read_csv()` con `chunksize=2`.
2. Inicializar una variable `suma_total = 0`.
3. Recorrer los bloques con un bucle.
4. En cada iteración:
   - Imprimir: *Procesando lote…*
   - Sumar los valores del bloque.
5. Imprimir el resultado final.

📌 Resultado esperado: **55**

---

## 🔴 Ejercicio 4: La Carrera de Formatos (Pickle vs CSV)

### Contexto
Tu empresa guarda históricos diarios en CSV y la lectura tarda horas.  
Quieres demostrar que **Pickle es más rápido para Pandas**.

### Datos de Entrada
Usa:
- El DataFrame del Ejercicio 1  
  **o**
- Uno nuevo con datos simples

Guárdalo como:
- `datos.csv`
- `datos.pkl`

### Tu Misión
1. Importar la librería `time`.
2. Medir cuánto tarda en cargarse:
   - El archivo CSV
   - El archivo Pickle
3. Comparar los tiempos.
4. Imprimir una frase final:

> **"El formato Pickle fue X segundos más rápido que el CSV"**

---

## 🧠 Idea Clave Final
Estos ejercicios no tratan de escribir código más corto, sino de **pensar mejor antes de cargar datos**:
- Menos columnas → menos memoria
- Tipos correctos → menos errores
- Procesamiento por partes → escalabilidad
- Formatos adecuados → velocidad

Pandas no es lento.  
Leer mal los datos sí.
