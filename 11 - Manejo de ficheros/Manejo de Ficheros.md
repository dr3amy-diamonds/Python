# Manejo de Ficheros en Python

## 📌 ¿Qué es un fichero?

Un **fichero** (archivo) es un espacio donde se guarda información de
forma permanente: texto, configuraciones, datos, etc. Estos archivos
pueden estar almacenados en tu sistema de archivos y tu programa puede
interactuar con ellos para **leer** o **escribir** datos.

Trabajar con ficheros permite a tu programa almacenar y recuperar
información de manera persistente, lo que significa que los datos no se
pierden cuando termina la ejecución del programa.

------------------------------------------------------------------------

## 📌 ¿Para qué sirve trabajar con ficheros?

El manejo de ficheros en Python es útil en una variedad de situaciones,
tales como:

-   **Guardar datos que deben persistir**
-   **Leer información externa**
-   **Crear registros o logs**
-   **Procesar archivos generados por otras aplicaciones**

------------------------------------------------------------------------

## 📌 Tipos de apertura de archivos

  Modo   Significado
  ------ ---------------------------------------------
  `r`    Leer archivo (error si no existe)
  `w`    Escribir (crea o **sobrescribe**)
  `a`    Agregar contenido al final
  `x`    Crear un archivo nuevo (error si ya existe)
  `r+`   Leer y escribir

### Codificación recomendada

``` python
open("archivo.txt", "r", encoding="utf-8")
```

------------------------------------------------------------------------

## 📌 Buenas prácticas

✔ Usar **with open()**\
✔ Manejar excepciones\
✔ Elegir correctamente el modo de apertura\
✔ Usar **utf-8** para evitar errores de codificación

Ejemplo:

``` python
with open("archivo.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
```

Ejemplo con excepciones:

``` python
try:
    with open("archivo.txt", "r") as f:
        contenido = f.read()
except FileNotFoundError:
    print("El archivo no se encuentra.")
except PermissionError:
    print("No tienes permisos para abrir el archivo.")
```

------------------------------------------------------------------------

## ❌ ¿Qué NO se debe hacer?

✗ Leer un archivo sin verificar su existencia\
✗ Usar `"w"` si no deseas sobrescribir el archivo\
✗ Asumir que siempre podrás abrir un archivo\
✗ Olvidar cerrar el archivo (si no usas `with open()`)

------------------------------------------------------------------------

## 📌 Operaciones Básicas

### ✔ Leer un archivo

``` python
with open("archivo.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
    print(contenido)
```

### ✔ Escribir (sobrescribir)

``` python
with open("archivo.txt", "w", encoding="utf-8") as f:
    f.write("Hola Mundo")
```

### ✔ Agregar contenido al final

``` python
with open("archivo.txt", "a", encoding="utf-8") as f:
    f.write("\nNueva línea agregada al final.")
```

### ✔ Leer línea por línea

``` python
with open("archivo.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea)
```

------------------------------------------------------------------------

## 📌 Manejo de errores

### Archivo que no existe

``` python
try:
    with open("nada.txt", "r") as f:
        contenido = f.read()
except FileNotFoundError:
    print("El archivo no existe.")
```

### Error de permisos

``` python
except PermissionError:
    print("No tienes permiso para abrir este archivo.")
```

------------------------------------------------------------------------

## 📌 Recomendaciones finales

-   Usa siempre `with open()`
-   Utiliza `utf-8`
-   Maneja excepciones
-   Prefiere rutas relativas
-   Verifica la existencia de archivos cuando sea necesario
