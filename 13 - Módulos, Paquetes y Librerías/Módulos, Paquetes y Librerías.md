# 📘 Tema 13 -- Módulos, Paquetes y Librerías en Python

## 🔹 ¿Qué es un módulo en Python?

Un **módulo** es un archivo con extensión `.py` que contiene código
Python: - Funciones\
- Clases\
- Variables\
- Código ejecutable

Sirve para **organizar código** en partes reutilizables.

Ejemplos de módulos estándar: - `math` - `random` - `os`

``` python
import math
print(math.sqrt(16))  # 4.0
```

También se pueden importar elementos específicos:

``` python
from math import sqrt
print(sqrt(25))  # 5
```

------------------------------------------------------------------------

## 🔹 ¿Qué es un paquete?

Un paquete es una carpeta que contiene varios módulos y un archivo
especial `__init__.py`.

Ejemplo de estructura:

    mi_paquete/
    │── __init__.py
    │── modulo1.py
    │── modulo2.py

Permite organizar módulos en una **estructura jerárquica**.

------------------------------------------------------------------------

## 🔹 ¿Qué es una librería?

Una librería es un conjunto de módulos y/o paquetes que proporcionan
funcionalidades específicas.

Ejemplos:

-   requests → HTTP
-   numpy → operaciones matemáticas
-   pandas → análisis de datos
-   flask → desarrollo web

------------------------------------------------------------------------

## 🔹 Librerías estándar más comunes y útiles

### 📁 os --- Interacción con el sistema operativo

``` python
import os
print(os.listdir())
```

### 💻 sys --- Información del sistema

``` python
import sys
print(sys.version)
```

### 🕒 datetime --- Manejo de fechas y horas

``` python
from datetime import datetime
print(datetime.now())
```

### 📦 json --- Trabajar con JSON

### 🔍 re --- Expresiones regulares

### 🎲 random --- Números aleatorios

------------------------------------------------------------------------

## 🔹 Instalación y uso de librerías externas con pip

`pip` es el gestor oficial de paquetes de Python.

### ➤ Instalar un paquete

    pip install nombre_paquete

Ejemplo:

    pip install requests

Luego se usa:

``` python
import requests
```

### ➤ Actualizar

    pip install --upgrade nombre_paquete

### ➤ Desinstalar

    pip uninstall nombre_paquete

### ➤ Ver paquetes instalados

    pip list

------------------------------------------------------------------------

## 🔹 Entornos virtuales (venv)

Los entornos virtuales permiten aislar dependencias de cada proyecto.

### ➤ Crear entorno

    python -m venv env

### ➤ Activar en Windows

    .\env\Scriptsctivate

### ➤ Activar en Linux/Mac

    source env/bin/activate

### ➤ Desactivar

    deactivate

------------------------------------------------------------------------

## 🔹 ¿Por qué usar entornos virtuales?

✔ Evitan conflictos entre versiones\
✔ Mantienen limpio el sistema\
✔ Facilitan compartir proyectos

Crear archivo de dependencias:

    pip freeze > requirements.txt

Instalar dependencias desde él:

    pip install -r requirements.txt

------------------------------------------------------------------------

## 🔹 Resumen

En este tema aprendimos a:

-   Organizar código con módulos\
-   Agrupar módulos con paquetes\
-   Usar librerías estándar y externas\
-   Instalar paquetes con pip\
-   Manejar entornos virtuales\
-   Usar requirements.txt para proyectos profesionales
