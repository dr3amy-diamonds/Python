# Ejemplos prácticos para librerías estándar

print("---- Ejemplo con os ----")
import os #

# Listar archivos y carpetas en el directorio actual
print("Archivos y carpetas en el directorio actual:")
print(os.listdir('.'))

# Obtener la ruta actual
print("Ruta actual:", os.getcwd())

# Crear una carpeta temporal (si no existe)
carpeta = 'temp_carpeta'
if not os.path.exists(carpeta):
    os.mkdir(carpeta) #Creación del directorio
    print(f"Carpeta '{carpeta}' creada.")
else:
    print(f"Carpeta '{carpeta}' ya existía.")

print("\n---- Ejemplo con sys ----")
import sys

# Mostrar versión de Python
print("Versión de Python:", sys.version)

# Mostrar argumentos pasados al script (lista)
print("Argumentos del script:", sys.argv)

print("\n---- Ejemplo con datetime ----")
from datetime import datetime, timedelta

# Fecha y hora actuales
ahora = datetime.now()
print("Fecha y hora actuales:", ahora)

# Formatear fecha como string
print("Fecha formateada:", ahora.strftime("%Y-%m-%d %H:%M:%S"))

# Calcular fecha futura: hoy + 7 días
futuro = ahora + timedelta(days=7)
print("Fecha dentro de 7 días:", futuro.strftime("%Y-%m-%d"))

print("\n---- Ejemplo con json ----")
import json

# Diccionario Python
persona = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}

# Convertir diccionario a JSON (string)
persona_json = json.dumps(persona)
print("JSON generado:", persona_json)

# Convertir JSON a diccionario
persona_dict = json.loads(persona_json)
print("Diccionario desde JSON:", persona_dict)

print("\n---- Ejemplo con re (expresiones regulares) ----")
import re

texto = "Mi correo es ejemplo@mail.com y mi teléfono es 123-456-7890."

# Buscar correo electrónico
correo = re.search(r'\S+@\S+\.\S+', texto)
if correo:
    print("Correo encontrado:", correo.group())

# Buscar todos los números en el texto
numeros = re.findall(r'\d+', texto)
print("Números encontrados:", numeros)

print("\n---- Ejemplo con random ----")
import random

# Número aleatorio entre 1 y 10
num = random.randint(1, 10)
print("Número aleatorio entre 1 y 10:", num)

# Elegir un elemento aleatorio de una lista
colores = ['rojo', 'verde', 'azul', 'amarillo']
color = random.choice(colores)
print("Color aleatorio:", color)

# Barajar lista
random.shuffle(colores)
print("Lista barajada:", colores)
