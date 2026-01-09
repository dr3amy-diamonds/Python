import numpy as np

# ===============================
# 1. Crear arrays a partir de listas
# ===============================

lista = [10, 20, 30, 40]

array_1d = np.array(lista)

print("Array 1D:")
print(array_1d)
print()


# ===============================
# 2. Crear un array 2D (matriz)
# ===============================

lista_2d = [
    [1, 2, 3],
    [4, 5, 6]
]

array_2d = np.array(lista_2d)

print("Array 2D:")
print(array_2d)
print()


# ===============================
# 3. Propiedades importantes
# ===============================

print("Propiedades del array 1D:")
print("Dimensiones:", array_1d.ndim)
print("Forma (shape):", array_1d.shape)
print("Total de elementos:", array_1d.size)
print("Tipo de dato:", array_1d.dtype)
print()

print("Propiedades del array 2D:")
print("Dimensiones:", array_2d.ndim)
print("Forma (shape):", array_2d.shape)
print("Total de elementos:", array_2d.size)
print("Tipo de dato:", array_2d.dtype)
print()


# ===============================
# 4. Acceso a elementos
# ===============================

print("Primer elemento del array 1D:", array_1d[0])
print("Elemento en fila 2, columna 3 del array 2D:", array_2d[1][2])
print()


# ===============================
# 5. Demostración de homogeneidad
# ===============================

mezcla = np.array([1, 2, 3.5])

print("Array con mezcla de enteros y flotantes:")
print(mezcla)
print("Tipo de dato resultante:", mezcla.dtype)
