import numpy as np

#Iteración básica en Array 1D
array_1d=np.array([10,20,30,40])

for elemento in array_1d:
    print("Elemento:", elemento)

"""
Qué pasa:

*   Se recorre elemento por elemento

*   Similar a una lista

Útil para inspección
No óptimo para cálculos
"""

#Iteración en array 2D(Por filas)
array_2d=np.array([[1,2,3,4], [5,6,7,8]])

for fila in array_2d:
    print("Fila: ", fila)

"""
Qué pasa:

*   Cada iteración devuelve una fila completa

*   Filas = observaciones

✔ Muy común
✔ Fácil de entender
"""

#Iteración elemento por elemento en 2D
for fila in array_2d:
    for elemento  in fila:
        print("Elemento por Fila:", elemento)

"""
Qué pasa:

*   bucle anidado

*   lento para grandes datos

 Evitar si puedes
"""

#Iteración con indices(range)
for i in range(array_2d.shape[0]):
    for j in range(array_2d.shape[1]):
        print(f"Elemento ({i},{j}) =", array_2d[i, j])

"""
Útil cuando:

*   Necesitas posición

*   Lógica dependiente del índice

Más propenso a errores
"""

#enumerate() (índice + valor)

nuevo_array1d=np.array([1,2,3,4,5,6])

for i, valor in enumerate(nuevo_array1d):
    print(f"Índice {i} → {valor}")

"""
✔ Limpio
✔ Recomendado frente a range
"""

#Iterar por columnas (transpose)
for columna in array_2d.T:
    print("Columna: ", columna)

"""
.T intercambia filas ↔ columnas
✔ Útil para análisis por variable
"""

#Iteración con nditer (básica)
for x in np.nditer(array_2d):
    print("Elemento:", x)

"""
Qué hace:

recorre todos los elementos

sin importar dimensiones

✔ General
Poco usado en análisis simple
"""

#nditer con escritura
arr_nditer = np.array([1, 2, 3])

for x in np.nditer(arr_nditer, op_flags=['readwrite']):
    x[...] = x * 10

print(arr_nditer)

"""
Modifica el array en el lugar

Avanzado
"""

#Orden de iteración (memoria)
arr = np.array([[1, 2], [3, 4]])

print("Orden C (por filas):")
for x in np.nditer(arr, order='C'):
    print(x)

print("Orden F (por columnas):")
for x in np.nditer(arr, order='F'):
    print(x)

"""
El orden afecta rendimiento
✔ NumPy usa C-order por defecto
"""

#Comparación: iterar vs vectorizar
arr = np.arange(1_000_000)
resultado = []

for x in arr:
    resultado.append(x * 2)

#Vectorizar
resultado = arr * 2

"""
Vectorizado:

*   más rápido

*   más limpio

*   más NumPy
"""

#terar solo cuando NO hay alternativa
arr = np.array([5, 12, 7, 20])

resultado = []

for x in arr:
    if x > 10 and x % 2 == 0:
        resultado.append(x)

print("Resultado:", resultado)

"""
✔ Justificado
✔ Claro
"""