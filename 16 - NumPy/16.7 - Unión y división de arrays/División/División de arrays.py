import numpy as np

#División estricta con np.split() (array 1D)
array_1d=np.arange(1,7)*10
print("Primer Array (1D)")
print(array_1d)
print("\n")

partes= np.split(array_1d, 3)
print("Dividido")
print(partes)
print("\n")
"""
Qué pasa:

Qué pasa:

*   el array tiene 6 elementos

*   se divide en 3 partes iguales

*   cada parte tiene 2 elementos

✔ División exacta
✔ Orden preservado
"""

#Error común con split()
try:
    array_1d = np.array([1, 2, 3, 4, 5])

    np.split(array_1d, 3)
except:
    print("ValueError: array split does not result in an equal division")
print("\n")
"""
Lección
*   split() exige divisiones exactas
"""

#División flexible con np.array_split()

array_1d = np.array([1, 2, 3, 4, 5])

partes = np.array_split(array_1d, 3)

for p in partes:
    print(p)
print("\n")

"""
Qué pasa:

*   no todos los bloques tienen el mismo tamaño

*   NumPy reparte los elementos de forma equilibrada

✔ No lanza error
✔ Muy usada en la práctica
"""

#División por filas(axis=0)
matriz_uno=np.arange(1,13).reshape(4,3)
print("Matriz N°1")
print(matriz_uno)
print("\n")

partes=np.split(matriz_uno,2,axis=0)

print("División por filas(axis=0)")
for p in partes:
    print(p)
print("\n")

"""
Qué pasa:

*   se divide la matriz por filas

*   cada sub-array conserva columnas

axis=0 divide filas
"""

#Diisión por columnas(axis=1)
partes=np.split(matriz_uno, 3, axis=1)

print("División por columnas (axis=1)")
for p in partes:
    print(p)
print("\n")

"""
Qué pasa:

*   se divide por columnas

*   cada bloque conserva filas

axis=1 divide columnas
"""

#vsplit() — división vertical (filas)

partes=np.vsplit(matriz_uno,2)

print("División por vsplit")
for p in partes:
    print(p)

print("\n")

"""
    Equivale a np.split(matriz, 2, axis=0)
    ✔ Más legible
    ✔ Menos errores conceptuales
"""

#hsplit() -  división horizontal (columnas)
partes = np.hsplit(matriz_uno, 3)

print("División por hsplit()")
for p in partes:
    print(p)
print("\n")

#Equivale a np.split(matriz, 3, axis=1)

#Error Común con hsplit
try:
    np.hsplit(matriz_uno, 4)
except:
    print("El número de columnas no permite esa división")

print("\n")
"""
Lección
*   Siempre revisa el shape antes de dividir
"""

#División usando índices(Avanzado)

arr = np.array([1, 2, 3, 4, 5, 6])

partes = np.split(arr, [2, 4])

print("División usando índices")
for p in partes:
    print(p)
print("\n")

"""
Qué pasa:

*   se divide en posiciones específicas

*   muy útil para separar bloques concretos
"""

#Caso real: entrenamiento y prueba
datos = np.arange(20)

train, test = np.array_split(datos, 2)

print("Train:", train)
print("Test:", test)

"""
Uso real:

*   preparación de datos

*   machine learning

*   validación
"""

"""
ERRORES QUE YA NO DEBES COMETER

*   Usar split cuando no es exacto
*   Dividir sin revisar shape
*   Confundir axis=0 y axis=1
*   Asumir que NumPy “adivina”
"""

"""
| Objetivo            | Función        |
| ------------------- | -------------- |
| División exacta     | `split`        |
| División flexible   | `array_split`  |
| Dividir filas       | `vsplit`       |
| Dividir columnas    | `hsplit`       |
| Dividir por índices | `split([...])` |

"""