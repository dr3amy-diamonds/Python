#Nivel 1 — Módulos básicos

"""
1. Crear y usar tu primer módulo

*   Crea un archivo llamado saludos.py que tenga una función hola(nombre).
*   Después, desde otro archivo Python, importa el módulo y usa la función.
"""

"""
2) Módulo con varias funciones

*   Crea un módulo llamado operaciones.py con tres funciones:

*   sumar(a, b)

*   restar(a, b)

*   multiplicar(a, b)

Luego importa solo una de ellas usando from ... import ....
"""

"""
3) Variables dentro de un módulo

*Crea un módulo config.py que contenga:

una variable VERSION

una variable AUTOR

Desde otro archivo, imprime esos valores usando import config.
"""

#Nivel 2 — Paquetes

"""
4) Crear un paquete sencillo

Crea una carpeta llamada utilidades/ con:

*   __init__.py

*   cadenas.py (función cuenta_vocales(texto))

*   numeros.py (función es_par(n))

Desde un archivo principal, importa cada módulo del paquete y úsalo.
"""

"""
5) Subpaquetes

Crea este árbol:

herramientas/
    __init__.py
    texto/
        __init__.py
        limpiar.py


En limpiar.py, crea una función espacios(texto) que elimine espacios.
Luego importa el submódulo desde un archivo principal.
"""

#Nivel 3 — Librerías estándar
"""
6) Usar random

Escribe un programa que use random.randint() para simular:

tirar un dado 10 veces

mostrar cuántas veces salió cada número
"""

"""
7) Usar math

Crea un módulo propio que use funciones de math para:

calcular el área de un círculo

calcular la raíz cuadrada de un número

Exporta esas funciones desde tu módulo usando imports internos.
"""

"""
8) Usar datetime

Crea un programa que:

*   Imprima la fecha y hora actual

*   Extraiga el año, mes y día

Los muestre en formato: AAAA - MM - DD
"""

# Nivel 4 — Librerías externas (si quieres practicar con pip)
"""
9) Requests (si puedes instalar paquetes)

Crea un programa que:

Use requests.get() para obtener el contenido de “https://pokeapi.co/api/v2/pokemon/pikachu”

Muestre el nombre y el peso del Pokémon

(No necesitas entender APIs, solo practicar la librería).

"""

"""
10) NumPy básico

Crea un arreglo con NumPy de 10 números y calcula:

*   la suma

*   el máximo

*   el promedio

Todo usando funciones propias de NumPy (no de Python normal).
"""