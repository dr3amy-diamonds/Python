# Entornos Virtuales en Python

## 1. ¿Qué problema resuelve un entorno virtual?

Imagina esto:

-   **Proyecto A** usa `pandas 1.5`
-   **Proyecto B** usa `pandas 2.0`
-   Ambos están en la misma PC

❌ **Sin entorno virtual** → conflictos, errores, caos\
✅ **Con entorno virtual** → cada proyecto vive aislado

👉 Un entorno virtual es una caja donde: - Se instalan librerías - Solo
afectan a ese proyecto

------------------------------------------------------------------------

## 2. ¿Qué es venv?

`venv` es el módulo estándar de Python para crear entornos virtuales.

✔ Viene con Python\
✔ No se instala\
✔ Es el más usado

------------------------------------------------------------------------

## 3. Crear tu primer entorno virtual (PASO A PASO)

### 📁 Paso 1: Entra a tu carpeta de proyecto

``` bash
cd Proyecto_Analisis_Datos
```

### 📁 Paso 2: Crear el entorno

``` bash
python -m venv venv
```

### ▶ Paso 3: Activar el entorno

**Windows (PowerShell):**

``` bash
venv\Scripts\activate
```

**Linux / Mac:**

``` bash
source venv/bin/activate
```

Si salió bien, verás algo así:

``` text
(venv) C:\...
```

👉 Eso significa: el entorno está activo.

------------------------------------------------------------------------

## 4. pip: el instalador de librerías

Dentro del entorno activo:

``` bash
pip install pandas
pip install numpy
```

⚠️ **IMPORTANTE:** `pip` siempre instala en el entorno activo.

------------------------------------------------------------------------

## 5. ¿Cómo saber qué librerías tiene mi proyecto?

``` bash
pip list
```

O para guardarlo:

``` bash
pip freeze > requirements.txt
```

Ejemplo de `requirements.txt`:

``` text
numpy==1.26.4
pandas==2.2.1
```

👉 Esto permite recrear el proyecto exacto.

------------------------------------------------------------------------

## 6. Reconstruir un proyecto desde cero

``` bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

✨ Proyecto clonado perfectamente.

------------------------------------------------------------------------

## 7. Estructura profesional mínima de proyecto

``` text
Proyecto_Analisis_Datos/
│
├── venv/              (NO se sube a Git)
├── data/              (CSV, Excel)
├── src/
│   └── main.py
├── requirements.txt
└── README.md
```

Esto ya es nivel profesional real.

------------------------------------------------------------------------

## 8. Práctica guiada (OBLIGATORIA)

👉 Haz esto ahora mismo:

1️⃣ Crea una carpeta nueva: **14 - Entornos virtuales**\
2️⃣ Dentro, crea un entorno `venv`\
3️⃣ Actívalo\
4️⃣ Instala `numpy`\
5️⃣ Ejecuta:

``` bash
pip freeze > requirements.txt
```
