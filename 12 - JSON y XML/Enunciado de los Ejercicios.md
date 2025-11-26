# Enunciados de Ejercicios de JSON & XML en Python

## 🟩 Nivel 1 — Muy Básico (JSON)

### Ejercicio 1 — Crear un JSON desde un diccionario
- Enunciado:
  - Crea un diccionario con tu nombre, edad y ciudad. Convierte ese diccionario a un texto JSON y muéstralo en pantalla.
- Variantes:
  - Usa `indent=2` y `ensure_ascii=False` para conservar tildes.

### Ejercicio 2 — Guardar un JSON en un archivo
- Enunciado:
  - Usa el diccionario anterior y guárdalo en un archivo llamado `perfil.json`, sobrescribiéndolo cada vez.
- Variantes:
  - Comprobar si el archivo existe y mostrar un aviso antes de sobrescribir.

## 🟩 Nivel 2 — Leer JSON (Control básico)

### Ejercicio 3 — Leer y mostrar un JSON completo
- Enunciado:
  - Abre `perfil.json` y muestra su contenido en pantalla. Si no existe, muestra el mensaje: "El archivo JSON no fue encontrado."
- Variantes:
  - Maneja errores de formato (JSON inválido) con `try/except`.

### Ejercicio 4 — Extraer datos del JSON
- Enunciado:
  - Lee `perfil.json` e imprime solo nombre y edad.
- Variantes:
  - Si falta algún campo, imprime un mensaje amigable en lugar de fallar.

## 🟩 Nivel 3 — Actualización y manipulación

### Ejercicio 5 — Agregar un nuevo campo
- Enunciado:
  - Carga `perfil.json`, añade un nuevo dato llamado `"hobby"` con el valor que quieras y vuelve a guardar el archivo.

### Ejercicio 6 — Lista dentro de un JSON
- Enunciado:
  - Añade al diccionario una lista llamada `"idiomas"` con 2 o más idiomas. Guarda el resultado en `perfil.json`.
- Variantes:
  - Evita duplicados si el idioma ya existe.

## 🟦 Nivel 4 — XML Muy Básico

### Ejercicio 7 — Crear un XML simple
- Enunciado:
  - Crea un archivo llamado `usuario.xml` con esta estructura:

```xml
<usuario>
    <nombre>...</nombre>
    <edad>...</edad>
</usuario>
```

- Los valores deben ser inventados por ti.

### Ejercicio 8 — Leer un XML
- Enunciado:
  - Carga `usuario.xml` y muestra solo el contenido de `<nombre>`.

## 🟦 Nivel 5 — Lectura y modificación

### Ejercicio 9 — Agregar un nuevo nodo
- Enunciado:
  - Carga `usuario.xml`, añade un nodo `<pais>` y vuelve a guardar el archivo.
- Variantes:
### Ejercicio 10 — Mostrar todos los nodos
- Enunciado:
  - Crea un XML con esta forma:

```xml
<usuarios>
    <usuario>...</usuario>
    <usuario>...</usuario>
</usuarios>
```

- Cada usuario debe tener `nombre` y `edad`. Cárgalo y muestra todos los nombres en pantalla.


