import numpy as np

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 1 — Identificando la forma

#Creación del array
arr = np.arange(1, 9)

#Imprimir Array
print(arr)

#Imprimir shape del array
print("Shape del Array 1D: ")
print(arr.shape)

#Imprimir número de dimensiones
print("Número de Dimensiones: ")
print(arr.ndim)

#Imprimir número de elementos en el array
print("Número de elementos alojados en el array: ")
print(arr.size)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 2 — Cambiando la forma

print("Array original (1D):")
print(arr)

try:
    # Cambiar forma a (2, 4)
    arr_2x4 = arr.reshape(2, 4)
    print("\nArray con forma (2,4):\n", arr_2x4)

    # Cambiar forma a (4, 2)
    arr_4x2 = arr.reshape(4, 2)
    print("\nArray con forma (4,2):\n", arr_4x2)

except ValueError as e:
    print("Error al cambiar la forma del array:", e)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 3  — Uso de -1

print("Array original (1D):")
print(arr)

try:
    arr_2x1 = arr.reshape(2, -1)
    print("\nArray con forma 2 filas :\n", arr_2x1)

    arr_1x4 = arr.reshape(-1, 4)
    print("\nArray con forma de 4 columnas  :\n", arr_1x4)

except ValueError as e:
    print("Error al cambiar la forma del array:", e)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 4 — Comparando dimensiones


n = 5

#Creación de vector
vector = np.arange(n)
print("\nVector:")
print(vector)
#Crear array de (n,1)
array_n1 = vector.reshape(n, 1)
print("\nArray (n, 1):")
print(array_n1)
print("shape:", array_n1.shape)
print("Dimensiones: ", array_n1.ndim )

#Crear array de (1,n)
array_1n = vector.reshape(1, n)
print("\nArray (1, n):")
print(array_1n)
print("shape:", array_1n.shape)
print("Dimensiones:", array_1n.ndim)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 5 — Flatten vs Ravel

#Creación de Array 2D

array_2d = np.arange(1, 11).reshape(2, 5)
print("\nArray 2D:")
print(array_2d)

#Modificación
array_2d_modificado=array_2d.flatten()
print("\nArray 2D modificado a 1D:")
print(array_2d_modificado)

#Modificar primer elemento
array_2d_modificado[0]=15
print("\nCambio de elemento:")
print(array_2d_modificado)

#Modificación usando ravel
array_2d_modificado=array_2d.ravel()
print("\nArray 2D modificado a 1D:")
print(array_2d_modificado)

#Modificar primer elemento
array_2d_modificado[0]=10
print("\nCambio de elemento:")
print(array_2d)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 6 — Reshape inválido
"""
array_6=np.arange(1,7).reshape(4,4)
print("\n Array")
print(array_6)
"""

#El número de elementos debe ser el resultado de la multiplicación de las columnas y filas, si no es igual a ese resultado, dara error

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 7 — Transposición

array_7=np.arange(1,7).reshape(3,2)
print("\n Array 7")
print(array_7)

#Transposición 
arr_T = array_7.T
print("\n Array Transposicionado")
print(arr_T)
print("Shape: ", arr_T.shape)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 8 — Ejes (conceptual)
array_2d = np.arange(1, 11).reshape(2, 5)
print("\n Array 2D:")
print(array_2d)

"""
axis=0
Represante el eje Y, osea las columnas
"""

"""
axis=1
Representa el eje x, osea las filas
"""

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 9 — Preparando datos (mentalidad analista)

"""
¿Qué `shape` debería tener el array?
Ya que el array, en el ejercicio dice 10 observaciones y 3 variables, cada observación es una fila y las variables es una columna por ende seria (10,3)
"""
