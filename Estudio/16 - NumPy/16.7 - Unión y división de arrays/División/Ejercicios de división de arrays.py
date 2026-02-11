import numpy as np  

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 1 — División exacta en 1D

#Creación del Array 1D
array_1d=np.arange(1,13)
print("Array de una dimensión")
print(array_1d)
print("\n")

#Dividir array
dividir_array1d=np.split(array_1d,3)
print("División del Array 1D")
print(dividir_array1d)
print("\n")

for array in dividir_array1d:
    print(array)
    print(array.shape)

print("\n")

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 2 — División flexible en 1D

#Creación de nuevo array 1D
nuevo_array_1d=np.arange(1,11)
print("Nuevo Array 1D")
print(nuevo_array_1d)
print("\n")

#Dividir el array
partes = np.array_split(nuevo_array_1d, 3)
print("División del nuevo Array")
print(partes)
print("\n")

for array in partes:
    print(array)
    print(array.shape)
print("\n")

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 3 — División por filas (axis=0)

#Creación de Matriz
Matriz_uno=np.arange(1,13).reshape(4,3)
print("Matriz")
print(Matriz_uno)
print("\n")

#Dividir matriz en 2 filas
bloque1, bloque2 = np.split(Matriz_uno, 2, axis=0)
print("Bloque 1:")
print(bloque1)
print("Shape:", bloque1.shape)

print("\nBloque 2:")
print(bloque2)
print("Shape:", bloque2.shape)


#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 4 — División por columnas (axis=1)

#Dividir matriz en 2 filas
bloque1, bloque2, bloque3 = np.split(Matriz_uno, 3, axis=1)

#Imprimir Bloques
print("Bloque 1:")
print(bloque1)
print("Shape:", bloque1.shape)

print("\nBloque 2:")
print(bloque2)
print("Shape:", bloque2.shape)

print("\nBloque 3:")
print(bloque3)
print("Shape:", bloque3.shape)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 5 — Uso de funciones especializadas

#Creación de la matriz 2D
Matriz_2=np.arange(1,15).reshape(2,7)
print("Segunda Matriz")
print(Matriz_2)
print("\n")

#Dividir por filas usando svplit
filas_matrices = np.vsplit(Matriz_2, 2)
print("División de filas")
print(filas_matrices)
print("\n")

#Dividir por columnas usando hsplit
columnas_matrices=np.hsplit(Matriz_2, [2, 5])
print("División de columnas")
print(columnas_matrices)
print("\n")

"""
Reflexión:
    Las funciones especializadas (vsplit y hsplit) son más legibles que split,
    porque indican explícitamente si la división es por filas o por columnas,
    lo que hace el código más claro y fácil de entender.
"""

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 6 — División por índices

nuevo_array1d=np.arange(1,9)
print("Nuevo Array 1D")
print(nuevo_array1d)
print("\n")

#Dividir Array en Los primeros 3 elementos
primeros_tres=nuevo_array1d[:3]
print("Primeros tres elementos")
print(primeros_tres)
print("\n")

#Los siguientes tres elementos
siguiente_tres=nuevo_array1d[3:6]
print("Siguiente tres elementos")
print(siguiente_tres)
print("\n")

#Últimos dos elementos
ultimos_elementos=nuevo_array1d[-2:]
print("últimos dos elementos")
print(ultimos_elementos)
print("\n")

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 7 — Error controlado (muy importante)

nuevo_array1d=np.arange(1,8)
print("Nuevo Array 1D")
print(nuevo_array1d)
print("\n")

try:
    partes=np.split(nuevo_array1d,3)
except:
    print("ValueError: array split does not result in an equal division")

#Para dividir el arreglo en partes iguales, la longitud del array debe ser divisible por el número que quieres dividirlo

#Usando un método más flexible

try:
    partes=np.array_split(nuevo_array1d,3)
    print("Nuevo Array")
    print(partes)
except:
    print("ValueError: array split does not result in an equal division")
