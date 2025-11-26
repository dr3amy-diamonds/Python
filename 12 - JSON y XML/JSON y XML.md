
------------------------------------------------------------------------

# 🧩 **JSON y XML: ¿Qué son?**

### 🟦 JSON (*JavaScript Object Notation*)

-   Un **formato de intercambio de datos** basado en texto.
-   Muy usado en **APIs**, **web**, **configuración de aplicaciones**,
    etc.
-   Representa datos con **diccionarios y listas** (llave-valor).

Ejemplo JSON:

``` json
{
  "nombre": "Juan",
  "edad": 20,
  "lenguajes": ["Python", "C++"]
}
```

------------------------------------------------------------------------

### 🟧 XML (*eXtensible Markup Language*)

-   Formato basado en **etiquetas**, parecido a HTML.
-   Más **verboso**, más orientado a documentos.
-   Se usa aún en sistemas **bancarios**, **legacy**, **SOAP**,
    configuraciones complejas.

Ejemplo XML:

``` xml
<persona>
  <nombre>Juan</nombre>
  <edad>20</edad>
  <lenguajes>
    <lenguaje>Python</lenguaje>
    <lenguaje>C++</lenguaje>
  </lenguajes>
</persona>
```

------------------------------------------------------------------------

# 🐍 **JSON vs XML en Python**

## ✔ **Cómo usar JSON en Python**

Python trae un módulo integrado:

``` python
import json

# JSON a diccionario
data = json.loads('{"nombre": "Juan", "edad": 20}')

# Diccionario a JSON
json_string = json.dumps(data, indent=4)
```

------------------------------------------------------------------------

## ✔ **Cómo usar XML en Python**

Usando `xml.etree.ElementTree` (nativo):

``` python
import xml.etree.ElementTree as ET

tree = ET.parse("archivo.xml")
root = tree.getroot()

for hijo in root:
    print(hijo.tag, hijo.text)
```

Para crear XML:

``` python
import xml.etree.ElementTree as ET

root = ET.Element("persona")
nombre = ET.SubElement(root, "nombre")
nombre.text = "Juan"

tree = ET.ElementTree(root)
tree.write("persona.xml")
```

------------------------------------------------------------------------

# 🆚 **¿Cuándo usar JSON y cuándo usar XML?**

## ⭐ **Usa JSON cuando:**

-   Trabajas con **APIs REST**.
-   Necesitas **velocidad y ligereza**.
-   Formatos fáciles de leer y manipular.
-   Interactúas con JavaScript o web.
-   Guardas **configuraciones simples**.

👉 JSON es hoy el *estándar de facto*.

------------------------------------------------------------------------

## ⭐ **Usa XML cuando:**

-   Necesitas **estructura compleja** o metadatos.
-   Requieres **atributos y validaciones con XSD**.
-   Trabajas con **SOAP**, **sistemas antiguos**, **banca**,
    **gobierno**.
-   Guardas documentación con formato.

👉 XML es útil para **documentos estructurados**, no solo datos.

------------------------------------------------------------------------

# 🚫 **Cuándo NO usar JSON/XML**

## ❌ No uses JSON si:

-   Necesitas **comentarios** (no soporta).
-   Se requiere **validación estricta de formato**.
-   Debes almacenar datos muy complejos o jerarquías profundas.

------------------------------------------------------------------------

## ❌ No uses XML si:

-   El objetivo es **simple intercambio de datos**.
-   Necesitas **rapidez**, **bajo peso**, o facilidad de lectura.
-   No requieres formatos basados en etiquetas.

------------------------------------------------------------------------

# ⚠️ **Errores comunes que puedes encontrar**

## 🟦 En JSON:

### ❗ `json.JSONDecodeError`

Ocurre cuando el JSON está mal formado:

-   Comillas simples `'` en lugar de `"`.
-   Falta de coma.
-   Trailing commas: `,` al final.

Ejemplo incorrecto:

``` json
{"nombre": "Juan",}
```

------------------------------------------------------------------------

## 🟧 En XML:

### ❗ `xml.etree.ElementTree.ParseError`

Suele venir por:

-   Etiquetas no cerradas.
-   Estructura irregular.
-   Caracteres ilegales (`&`, `<`, etc.).

Ejemplo incorrecto:

``` xml
<persona>
  <nombre>Juan
</persona>
```

------------------------------------------------------------------------

# 🧠 **Conclusión rápida**

  -----------------------------------------------------------------------
  Aspecto                 JSON             XML
  ----------------------- ---------------- ------------------------------
  Facilidad de lectura    ⭐⭐⭐⭐⭐       ⭐⭐

  Peso del archivo        Ligero           Pesado

  Velocidad               Alta             Baja

  Jerarquías complejas    Normal           Excelente

  Meta-información        Limitado         Muy bueno
  (atributos)                              

  Uso típico              APIs, apps,      Sistemas antiguos, banca,
                          configs          documentos
  -----------------------------------------------------------------------

✔ **Si dudas → usa JSON**\
✔ **Si te lo piden explícitamente o hay XSD/DTD → usa XML**
