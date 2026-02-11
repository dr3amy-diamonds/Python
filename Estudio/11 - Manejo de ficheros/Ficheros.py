
#Ejemplo 1: Leer un archivo completo (básico)
with open("mensaje.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

"""
Qué hace:

*   Abre mensaje.txt en modo lectura ("r").

*   read() devuelve todo el texto.

*   with cierra el archivo automáticamente.
"""

#Ejemplo 2: Escribir un archivo desde cero
with open("saludo.txt", "w") as archivo:
    archivo.write("Hola, este archivo fue creado por Python.")

"""
Qué hace:

*   "w" borra todo lo que había y escribe desde cero.

*   Buena opción para generar archivos nuevos.
"""

#Ejemplo 3: Agregar contenido sin borrar
with open("log.txt", "a") as archivo:
    archivo.write("Nueva ejecución del programa\n")

"""
Qué hace:

*   "a" significa append → agrega al final.

*   Ideal para registros o historial.
"""

#Ejemplo 4:Leer línea por línea
with open("nombres.txt", "r") as archivo:
    for linea in archivo:
        print("Línea:", linea.strip())

"""
Qué hace:

*   Recorre cada línea del archivo.

*   strip() quita saltos de línea.
"""

#Ejemplo 5: Manejar errores (try/except)
try:
    with open("datos.txt", "r") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print("El archivo no existe.")

"""
Qué hace:

*   Si el archivo no existe → el programa no se rompe.

*   Captura el error y muestra un mensaje amigable.
"""

#Ejemplo 6: Guardar una lista en un archivo
frutas = ["Manzana", "Pera", "Uva"]

with open("frutas.txt", "w") as archivo:
    for f in frutas:
        archivo.write(f + "\n")

"""
Qué hace:

*   Escribe cada elemento de la lista en una línea.

*   Muy común para guardar datos simples.
"""

#Ejemplo 7: Leer un archivo y convertirlo a lista
with open("frutas.txt", "r") as archivo:
    lista = archivo.read().splitlines()

print(lista)

"""
Qué hace:

*   Devuelve una lista así: ["Manzana", "Pera", "Uva"]
"""

#Ejemplo 8: Ficheros + POO
class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def guardar(self):
        with open("usuarios.txt", "a") as f:
            f.write(f"{self.nombre},{self.edad}\n")

u1 = Usuario("Ana", 22)
u1.guardar()

"""
Qué hace:

*   Un objeto guarda su información en un archivo.

*   Esto mezcla POO con ficheros, igual que harás en proyectos reales.
"""

#Ejemplo 9: Leer un archivo como si fuera una base de datos
usuarios = []

with open("usuarios.txt", "r") as f:
    for linea in f:
        nombre, edad = linea.strip().split(",")
        usuarios.append((nombre, int(edad)))

print(usuarios)

"""
Qué hace:

*   Convierte texto a datos.

*   Útil para catálogos, inventarios, etc.
"""

#Ejemplo 10: Escribir JSON sin usar librerías externas
persona = {"nombre": "Luis", "edad": 30}

with open("persona.txt", "w") as f:
    for clave, valor in persona.items():
        f.write(f"{clave}:{valor}\n")

"""
Qué hace:

*   Guarda un diccionario de forma estructurada en un archivo.
"""