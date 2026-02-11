import xml.etree.ElementTree as xml
import json

persona = {
    "nombre": "Sandra",
    "apellido": "Upton",
    "edad": 24,
    "altura": 1.60,
    "es_estudiante": True,
    "ciudad": "Montería",
    "pais": "Colombia",
    "idiomas": ["Español", "Inglés"],
    "materias_favoritas": ["Matemáticas", "Ciencias", "Arte"]
}




#Convertir a JSON (string)
json_texto = json.dumps(persona, indent=4, ensure_ascii=False)
print(json_texto)

#Guardar en archivo JSON

with open("persona.json", "w", encoding="utf-8") as archivo:
    json.dump(persona, archivo, indent=4, ensure_ascii=False)

#Leer el archivo JSON

with open("persona.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

print("Nombre:", datos["nombre"])               
print("Primer idioma:", datos["idiomas"][0])     
print("Materias favoritas:", datos["materias_favoritas"]) 

#Convertir tus datos a XML

root = xml.Element("persona")

xml.SubElement(root, "nombre").text = "Sandra"
xml.SubElement(root, "apellido").text = "Upton"
xml.SubElement(root, "edad").text = str(24)
xml.SubElement(root, "altura").text = str(1.60)
xml.SubElement(root, "es_estudiante").text = str(True)
xml.SubElement(root, "ciudad").text = "Montería"
xml.SubElement(root, "pais").text = "Colombia"

# idiomas
idiomas_el = xml.SubElement(root, "idiomas")
for idioma in ["Español", "Inglés"]:
    xml.SubElement(idiomas_el, "idioma").text = idioma

# materias
materias_el = xml.SubElement(root, "materias_favoritas")
for m in ["Matemáticas", "Ciencias", "Arte"]:
    xml.SubElement(materias_el, "materia").text = m

tree = xml.ElementTree(root)
escribir_xml_pretty(root, "persona.xml")

#Leer el XML desde archivo


tree = xml.parse("persona.xml")
root = tree.getroot()

print("Nombre:", root.find("nombre").text)
print("País:", root.find("pais").text)

# imprimir todos los idiomas
for idioma in root.find("idiomas"):
    print("Idioma:", idioma.text)

#Modificar el XML
tree = xml.parse("persona.xml")
root = tree.getroot()

materias = root.find("materias_favoritas")
xml.SubElement(materias, "materia").text = "Historia"

escribir_xml_pretty(root, "persona.xml")

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



