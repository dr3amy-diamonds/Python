import numpy as np

"""
1. shape — la forma del array
"""

#Ejemplo 1: Array 1D

arr = np.array([10, 20, 30, 40, 50])

print(arr)
print("Shape:", arr.shape)

"""
Qué entender:

*   (5,) significa un solo eje con 5 elementos

*   No es fila ni columna, es un vector 1D
"""

#Ejemplo 2: Array 2D

matriz = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matriz)
print("Shape:", matriz.shape)


"""
Qué entender:

*   (2, 3) → 2 filas, 3 columnas

*   Esto ya se comporta como una tabla
"""

"""
2. Dimensiones (ndim)
"""

#Ejemplo 1: Comparar dimensiones
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3]])

print(a.ndim)
print(b.ndim)


"""
Qué entender:

Aunque visualmente parezcan similares:

*   a es 1D

*   b es 2D

Esto cambia cómo se operan
"""

"""
3. size — cantidad total de datos
"""

#Ejemplo:
arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr1.size)
print(arr2.size)

"""
Qué entender:

*   Ambos tienen 6 datos

*   La forma cambia, los datos no
"""

"""
4. reshape() — reorganizar datos
"""

#Ejemplo 1: reshape simple
arr = np.array([1, 2, 3, 4, 5, 6])

nuevo = arr.reshape(2, 3)

print(nuevo)
print("Shape:", nuevo.shape)

"""
Qué entender:

*   Los datos son los mismos

*   Solo cambió la organización
"""

#Ejemplo 2: usando -1
otro = arr.reshape(3, -1)
print(otro)

"""
Qué entender:

*   -1 le dice a NumPy:

*   “Calcula tú el tamaño que falta”
"""

"""
5. Ejes (axis) — idea visual
"""

#Ejemplo conceptual
matriz = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Shape:", matriz.shape)

"""
Qué entender:

*   axis=0 → vertical (columnas)

*   axis=1 → horizontal (filas)

(No operamos aún, solo ubicación mental).
"""

"""
6. (n,) vs (n,1) vs (1,n)
"""

#Ejemplo comparativo
a = np.array([1, 2, 3])
b = np.array([[1], [2], [3]])
c = np.array([[1, 2, 3]])

print(a.shape)
print(b.shape)
print(c.shape)

"""
Qué entender:

*   Mismos datos

*   Comportamientos distintos

* En machine learning esto es crítico
"""

"""
7. flatten() vs ravel()
"""

#Ejemplo 1: flatten (copia)
matriz = np.array([[1, 2], [3, 4]])

flat = matriz.flatten()
flat[0] = 999

print("Flatten:", flat)
print("Original:", matriz)

"""
Qué entender:

*   El original no cambia

*   flatten() crea copia
"""

#Ejemplo 2: ravel (vista)
rav = matriz.ravel()
rav[0] = 888

print("Ravel:", rav)
print("Original:", matriz)

"""
Qué entender:

*   El original sí cambia

*   ravel() es una vista
"""

"""
8. transpose() — cambiar ejes
"""

#Ejemplo:
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

transpuesta = matriz.T

print("Original:")
print(matriz)

print("Transpuesta:")
print(transpuesta)

"""
Qué entender:

*   Filas ↔ columnas

*   Fundamental en matemáticas y ML
"""