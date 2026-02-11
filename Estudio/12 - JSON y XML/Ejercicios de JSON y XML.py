import xml.etree.ElementTree as xml
import json
import os 

#Solución Ejercicio 1
datos_personales = {
    "Nombre": "Missouri",
    "Apellido": "Denesik",
    "Edad": 27,
    "Documento": 1003882,
    "Ciudad": "Berlin"
}

json_datos = json.dumps(datos_personales, indent=2, ensure_ascii=False)
print(json_datos)

print("================================================================================================================================================")
#Solución Ejercicio 2

archivo = "perfil.json"

if os.path.exists (archivo):
    print(f"¡Advertencia! El archivo '{archivo}' ya existe. Se sobrescribirá.")
else:
    print(f"El archivo '{archivo}' no existe. Se creará uno nuevo.")

with open(archivo, "w", encoding="utf-8") as archivo_json:
    json.dump(datos_personales, archivo_json, indent=2, ensure_ascii=False)

print(f"Datos guardados en '{archivo}' correctamente.")

print("================================================================================================================================================")
#Solución Ejercicio 3

try:
    with open("perfil.json", "r", encoding="utf-8") as file:
        datos = json.load(file)
        print(datos)
except FileNotFoundError:
    print("El archivo JSON no fue encontrado")
except json.JSONDecodeError:
    print("El archivo no contiene un JSON válido")

print("================================================================================================================================================")
#Solución Ejercicio 4

try:
    with open('perfil.json', 'r', encoding="utf-8") as archivo:
        datos = json.load(archivo)
    nombre = datos.get("Nombre", "El campo 'Nombre' no está presente en el archivo.")
    edad = datos.get("Edad", "El campo 'Edad' no está presente en el archivo.")
    print(nombre)
    print(edad)
except FileNotFoundError:
    print("El archivo JSON no fue encontrado")
except json.JSONDecodeError:
    print("El archivo no tiene un formato JSON válido")

print("================================================================================================================================================")
#Solución Ejercicio 5

try:
    with open('perfil.json', 'r',encoding="utf-8" ) as archivo:
        datos = json.load(archivo)
    datos['hobby'] = ['Leer', 'Jugar Fútbol', 'Viajar']
    with open('perfil.json', 'w', encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)
    print("Datos agregados correctamente")
except FileNotFoundError:
    print("El archivo JSON no fue encontrado")
except json.JSONDecodeError:
    print("El archivo no tiene un formato JSON válido")

print("================================================================================================================================================")
#Solución Ejercicio 6

try:
    # Abrimos el archivo en modo lectura
    with open('perfil.json', 'r', encoding="utf-8") as archivo:
        datos = json.load(archivo)

    # Definimos la lista de nuevos idiomas que queremos agregar
    nuevos_idiomas = ['Alemán', 'Español', 'Portugues', 'Inglés']

    # Si la clave 'idiomas' ya existe, solo agregamos los idiomas nuevos sin duplicar
    if 'idiomas' in datos:
        # Usamos un set para evitar duplicados, combinamos las listas y los convertimos a un set
        datos['idiomas'] = list(set(datos['idiomas'] + nuevos_idiomas))
    else:
        # Si no existe la clave 'idiomas', la creamos con los nuevos idiomas
        datos['idiomas'] = nuevos_idiomas

    # Guardamos el archivo actualizado
    with open('perfil.json', 'w', encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)

except FileNotFoundError:
    print("El archivo perfil.json no se encuentra.")
except json.JSONDecodeError:
    print("El archivo perfil.json no es un archivo JSON válido.")

print("================================================================================================================================================")
#Solución Ejercicio 7

#Lo pongo en modo defecto ya que esto hace que se vea lindo y bien estructurado
def escribir_xml_pretty(root, archivo):
    tree = xml.ElementTree(root)
    try:
        xml.indent(tree, space="    ")
        tree.write(archivo, encoding="utf-8", xml_declaration=True)
    except AttributeError:
        from xml.dom import minidom
        rough = xml.tostring(root, encoding="utf-8")
        reparsed = minidom.parseString(rough)
        pretty = reparsed.toprettyxml(indent="    ", encoding="utf-8")
        with open(archivo, "wb") as f:
            f.write(pretty)


#Creación del elemento Usuario
try:
    root = xml.Element("usuario")

    #Creación de los subelementos
    xml.SubElement(root, "nombre").text = "Letitia"
    xml.SubElement(root, "edad").text = str(24)

    tree = xml.ElementTree(root)
    escribir_xml_pretty(root, "usuario.xml")

    print("Cargado correctamente")
except NameError:
    print("Los datos no fueron cargados correctamente")

print("================================================================================================================================================")
#Solución Ejercicio 8
try:
    tree = xml.parse('usuario.xml')
    root = tree.getroot()
    print("Contenido del archivo XML:")

    nombre = root.find('nombre').text
    print(f"Nombre: {nombre}")
except FileNotFoundError:
    print("Error: El archivo XML no fue encontrado.")
except xml.ParseError:
    print("Error: Hubo un problema al analizar el archivo XML.")

print("================================================================================================================================================")
#Solución Ejercicio 9
try:
    tree = xml.parse('usuario.xml')
    root = tree.getroot()

    #Creación del nuevo elemento
    nuevo_elemento = xml.Element('país')
    nuevo_elemento.text = 'Alemania'

    #Agregar nuevo elemento
    root.append(nuevo_elemento)

    #Escribir y modificar
    tree.write('usuario.xml', encoding='utf-8', xml_declaration=True)
    escribir_xml_pretty(root, "usuario.xml")
    print("Elementos agregados")
except FileNotFoundError:
    print("Error: El archivo XML no fue encontrado.")
except xml.ParseError:
    print("Error: Hubo un problema al analizar el archivo XML.")

print("================================================================================================================================================")
#Solución Ejercicio 10

def escribir_xml_pretty2(root, archivo):
    tree = xml.ElementTree(root)
    try:
        # Intentamos usar xml.indent si estamos en Python 3.9 o superior
        xml.indent(tree, space="    ")
        tree.write(archivo, encoding="utf-8", xml_declaration=True)
    except AttributeError:
        # En caso de que xml.indent no esté disponible, usamos minidom
        from xml.dom import minidom
        rough = xml.tostring(root, encoding="utf-8")
        reparsed = minidom.parseString(rough)
        pretty = reparsed.toprettyxml(indent="    ")

        # Escribir el XML formateado en el archivo (modo texto)
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(pretty)

usuarios = xml.Element("usuarios")

datos_usuarios = [
    {"nombre": "Juan", "apellido": "Teagan", "edad": "30", "país": "México"},
    {"nombre": "Ana", "apellido": "Mitchell", "edad": "25", "país": "Colombia"},
    {"nombre": "Carlos", "apellido": "Ruvalcaba", "edad": "40", "país": "Argentina"}
]

for usuario in datos_usuarios:
    usuario_elem = xml.SubElement(usuarios, "usuario")

    nombre = xml.SubElement(usuario_elem, "nombre")
    nombre.text = usuario["nombre"]

    edad = xml.SubElement(usuario_elem, "edad")
    edad.text = usuario["edad"]

    pais = xml.SubElement(usuario_elem, "país")
    pais.text = usuario["país"]

# Llamamos a la función para escribir el archivo XML bonito
escribir_xml_pretty(usuarios, "usuario2.xml")
