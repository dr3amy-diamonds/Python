# Excepciones en Python 🐍

## 📘 Concepto

Las **excepciones** en Python son eventos que interrumpen el flujo
normal de ejecución de un programa cuando ocurre un **error**.\
En lugar de que el programa se detenga abruptamente, Python permite
**capturar** y **manejar** esas situaciones usando un bloque
`try-except`.

El objetivo principal de las excepciones es **mantener el control** del
programa y permitir que se tomen decisiones cuando algo inesperado
ocurre.

------------------------------------------------------------------------

## ⚙️ Estructura básica

``` python
try:
    # Código que puede generar un error
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que se ejecuta si ocurre una excepción
    print("No se puede dividir entre cero.")
```

**Salida:**

    No se puede dividir entre cero.

------------------------------------------------------------------------

## 🧩 Bloques adicionales

### `else`

Se ejecuta **solo si no ocurre ninguna excepción**.

``` python
try:
    numero = int(input("Ingresa un número: "))
except ValueError:
    print("Debes ingresar un número válido.")
else:
    print("Número correcto:", numero)
```

------------------------------------------------------------------------

### `finally`

Se ejecuta **siempre**, haya o no ocurrido una excepción (útil para
liberar recursos o cerrar conexiones).

``` python
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("Archivo no encontrado.")
finally:
    archivo.close()
    print("Archivo cerrado.")
```

------------------------------------------------------------------------

## 🔎 Tipos comunes de excepciones

  -------------------------------------------------------------------------
  Excepción             Descripción
  --------------------- ---------------------------------------------------
  `ValueError`          Valor incorrecto o tipo inapropiado.

  `ZeroDivisionError`   División entre cero.

  `TypeError`           Operación o función aplicada a un tipo inapropiado.

  `FileNotFoundError`   No se encuentra el archivo especificado.

  `IndexError`          Índice fuera de rango en una lista.

  `KeyError`            Clave no encontrada en un diccionario.
  -------------------------------------------------------------------------

------------------------------------------------------------------------

## 🧠 Qué **sí** se puede hacer

✅ Capturar errores específicos para tratarlos de forma adecuada.\
✅ Usar `finally` para liberar recursos (archivos, conexiones, etc.).\
✅ Crear tus **propias excepciones personalizadas** heredando de
`Exception`.\
✅ Encadenar excepciones para depurar mejor.

``` python
class ErrorPersonalizado(Exception):
    pass

try:
    raise ErrorPersonalizado("Ocurrió un error personalizado.")
except ErrorPersonalizado as e:
    print(e)
```

------------------------------------------------------------------------

## 🚫 Qué **no** se debe hacer

❌ Usar `except:` sin especificar el tipo de error --- esto captura
**todo**, incluso errores del sistema.\
❌ Abusar de las excepciones para controlar el flujo lógico normal del
programa.\
❌ Ignorar excepciones sin manejarlas (por ejemplo, `pass` dentro de un
`except`).\
❌ No liberar recursos (usar `finally` o contexto `with` cuando sea
necesario).

------------------------------------------------------------------------

## 🕐 Cuándo usar excepciones

**Usa excepciones cuando:**

-   Hay una posibilidad real de error que **no puedes evitar** (e.g.,
    abrir un archivo que podría no existir).
-   Quieres dar **información útil** al usuario o al desarrollador.
-   Trabajas con **operaciones externas** (archivos, redes, bases de
    datos, etc.).

**No las uses cuando:**

-   El error puede prevenirse con una simple validación previa.
-   Estás controlando la lógica normal del programa (mejor usar `if` o
    `while`).

------------------------------------------------------------------------

## 💡 Buenas prácticas

-   Captura solo las excepciones que necesites.
-   Escribe mensajes claros para depurar.
-   Usa `raise` para propagar errores si no puedes manejarlos
    localmente.
-   Mantén el bloque `try` lo más pequeño posible.

``` python
try:
    resultado = 10 / divisor
except ZeroDivisionError as e:
    raise ValueError("El divisor no puede ser cero.") from e
```

------------------------------------------------------------------------

## 📚 Conclusión

Las excepciones en Python son una herramienta poderosa para **manejar
errores de forma controlada**, mejorar la **robustez** del código y
mantener una **buena experiencia de usuario**.\
Usadas correctamente, permiten escribir programas más seguros, claros y
mantenibles.
