
En Python:
- JSON se maneja con el módulo `json`.
- XML se maneja, en este ejemplo, con `xml.etree.ElementTree`, que importamos con el alias `xml` para mantener consistencia en todo el código.

## Importaciones
- Usamos: `import xml.etree.ElementTree as xml` (`JSON y XML.py:1`). Esta forma establece el alias `xml` y lo usamos en todo el archivo.
- También importamos `json`: `import json` (`JSON y XML.py:2`).

## Datos de ejemplo: diccionario `persona`
- Se define un diccionario de Python llamado `persona` (`JSON y XML.py:4–14`) con campos típicos:
  - `str`: `nombre`, `apellido`, `ciudad`, `pais`
  - `int`: `edad`
  - `float`: `altura`
  - `bool`: `es_estudiante`
  - `list[str]`: `idiomas`, `materias_favoritas`
- Este diccionario es la fuente de datos que convertiremos a JSON y a XML.

## Convertir a JSON (texto) y mostrarlo
- Línea clave: `json_texto = json.dumps(persona, indent=4, ensure_ascii=False)` (`JSON y XML.py:33`).
  - `json.dumps(...)` convierte el diccionario de Python en una cadena JSON.
  - `indent=4` hace que el JSON quede bonito y legible con sangría de 4 espacios.
  - `ensure_ascii=False` permite que se conserven caracteres como tildes y ñ en UTF-8 (muy importante para español). Si fuera `True`, se escaparían como `\u00f1`, etc.
- `print(json_texto)` (`JSON y XML.py:34`) muestra el JSON por pantalla.

## Guardar el JSON en un archivo
- Bloque:
  - `with open("persona.json", "w", encoding="utf-8") as archivo:` (`JSON y XML.py:38`)
  - `json.dump(persona, archivo, indent=4, ensure_ascii=False)` (`JSON y XML.py:39`)
- ¿Qué pasa aquí?
  - `with open(...)` abre el archivo `persona.json` en modo escritura (`"w"`). El `with` es un “context manager” que garantiza que el archivo se cierre automáticamente, incluso si hay errores.
  - `encoding="utf-8"` asegura que se escriban bien los caracteres especiales.
  - `json.dump(...)` escribe el diccionario directamente al archivo en formato JSON (a diferencia de `dumps`, que solo devuelve la cadena).
  - El uso de `indent` y `ensure_ascii` es el mismo que antes.

## Leer el archivo JSON
- Bloque:
  - `with open("persona.json", "r", encoding="utf-8") as archivo:` (`JSON y XML.py:43`)
  - `datos = json.load(archivo)` (`JSON y XML.py:44`)
- ¿Qué pasa aquí?
  - Abres el archivo en modo lectura (`"r"`).
  - `json.load(...)` lee el contenido del archivo y te devuelve un diccionario de Python.
- Acceso a datos:
  - `print(datos["nombre"])` (`JSON y XML.py:46`) muestra el nombre (tipo `str`).
  - `print(datos["idiomas"][0])` (`JSON y XML.py:47`) muestra el primer idioma de la lista.
  - `print(datos["materias_favoritas"])` (`JSON y XML.py:48`) muestra toda la lista de materias.

## Crear un XML desde cero
- Se empieza con `root = xml.Element("persona")` (`JSON y XML.py:52`). Esto crea el elemento raíz `<persona>`.
- Luego se añaden subelementos (`JSON y XML.py:54–61`). Ejemplos:
  - `xml.SubElement(root, "nombre").text = "Sandra"` crea `<nombre>Sandra</nombre>`.
  - Para números y booleanos, se convierten a texto: `str(24)`, `str(1.60)`, `str(True)` (`JSON y XML.py:56–58`). En XML todo lo que va entre etiquetas es texto.
- Listas (idiomas y materias):
  - `idiomas_el = xml.SubElement(root, "idiomas")` y luego un `for` que crea `<idioma>` por cada elemento (`JSON y XML.py:63–66`).
  - `materias_el = xml.SubElement(root, "materias_favoritas")` y otro `for` para `<materia>` (`JSON y XML.py:68–70`).
- Para guardar: `escribir_xml_pretty(root, "persona.xml")` (`JSON y XML.py:73`). Esto garantiza que el archivo quede con sangría e indentación legible.

## Leer un XML desde archivo
- `tree = xml.parse("persona.xml")` y `root = tree.getroot()` (`JSON y XML.py:78–79`).
  - `xml.parse(...)` abre y analiza el XML.
  - `getroot()` te da el elemento raíz.
- Búsqueda de elementos:
  - `root.find("nombre").text` obtiene el texto dentro de `<nombre>` (`JSON y XML.py:81`).
  - `root.find("pais").text` obtiene el texto dentro de `<pais>` (`JSON y XML.py:82`).
- Recorrer hijos:
  - `for idioma in root.find("idiomas"):` (`JSON y XML.py:85`) recorre los subelementos `<idioma>` dentro de `<idiomas>` y muestra su `.text`.

## Modificar el XML
- Se vuelve a cargar el XML (`JSON y XML.py:89–90`).
- Se busca el contenedor de materias: `materias = root.find("materias_favoritas")` (`JSON y XML.py:92`).
- Se añade una nueva materia: `xml.SubElement(materias, "materia").text = "Historia"` (`JSON y XML.py:93`).
- Se guarda de nuevo con formato: `escribir_xml_pretty(root, "persona.xml")` (`JSON y XML.py:95`).

## Estructura XML con sangría como la solicitada
- Para que el archivo XML quede con líneas separadas e indentadas (no todo en una sola línea), añadimos una función de ayuda: `escribir_xml_pretty` (`JSON y XML.py:17–28`).
- ¿Cómo funciona?
  - Crea un `ElementTree` y, si tu versión de Python es 3.9 o superior, usa `xml.indent(tree, space="    ")` (`JSON y XML.py:20`) para aplicar sangría automáticamente.
  - Si la función `xml.indent` no existe (versiones antiguas), usa `xml.dom.minidom` para “prettificar” el contenido (`JSON y XML.py:23–28`).
- Luego se llama a esta función al guardar el XML inicial (`JSON y XML.py:73`) y al modificarlo (`JSON y XML.py:95`). Así el archivo queda con la estructura:

```xml
<persona>
    <nombre>Sandra</nombre>
    <apellido>Upton</apellido>
    <edad>24</edad>
    <altura>1.6</altura>
    <es_estudiante>True</es_estudiante>
    <ciudad>Montería</ciudad>
    <pais>Colombia</pais>
    <idiomas>
        <idioma>Español</idioma>
        <idioma>Inglés</idioma>
    </idiomas>
    <materias_favoritas>
        <materia>Matemáticas</materia>
        <materia>Ciencias</materia>
        <materia>Arte</materia>
        <materia>Historia</materia>
    </materias_favoritas>
</persona>
```

## ¿Cuándo usar JSON y cuándo usar XML?
- Usa JSON cuando:
  - Necesitas intercambiar datos con servicios web y APIs (es el estándar de facto).
  - Buscas simplicidad, legibilidad y eficiencia.
  - Tus datos son estructuras típicas de diccionarios y listas.
- Usa XML cuando:
  - Requieres esquemas, validación, atributos o espacios de nombres.
  - Trabajas con sistemas legados que esperan XML.

## Buenas prácticas y errores comunes
- JSON:
  - `ensure_ascii=False` es clave para textos en español. Sin eso, los caracteres se convierten a secuencias `\uXXXX`.
  - Diferencia `dump` vs `dumps`: `dump` escribe al archivo, `dumps` devuelve una cadena.
  - Diferencia `load` vs `loads`: `load` lee desde archivo, `loads` lee desde una cadena.
- XML:
  - Convierte números y booleanos a `str(...)` antes de asignarlos a `.text`.
  - Mantén una estructura clara: contenedores (`<idiomas>`, `<materias_favoritas>`) con hijos (`<idioma>`, `<materia>`).
  - Usa un alias consistente: `import xml.etree.ElementTree as xml` y utilízalo en todo el archivo.
  - Para legibilidad, aplica indentación al guardar (con `xml.indent` o `minidom`).
- Archivos:
  - Usa `with open(...)` para garantizar cierre y manejo correcto de recursos.
  - Especifica `encoding="utf-8"` cuando trabajes con tildes/ñ.

## Resumen rápido
- Convierte dict de Python a JSON: `json.dumps` (cadena) o `json.dump` (archivo).
- Lee JSON: `json.load` (desde archivo) o `json.loads` (desde cadena).
- Construye XML: `xml.Element`, `xml.SubElement`, asigna `.text`.
- Guarda XML legible: `escribir_xml_pretty(root, "persona.xml")`.
- Lee XML: `xml.parse`, `getroot`, `find`, recorre hijos.
- JSON es más simple y común para APIs; XML es más expresivo pero más complejo.
