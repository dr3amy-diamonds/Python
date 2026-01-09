import numpy as np

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución ejercicio 1
array1 = np.array([5, 10, 15, 20, 25])

#Imprimir Array
print("Array 1:")
print(array1)
print()

#Tipo de dato
print("Tipo de dato de Array 1:")
print(type(array1))
print()

#Tipo de dato interno
print("Tipo de dato interno de Array 1:")
print(array1.dtype)
print()

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución ejercicio 2

#Imprimir número de dimensiones
print("Número de dimensiones del Array 1:")
print(array1.ndim)
print()

#Imprimir forma shape
print("Forma del Array 1:")
print(array1.shape) #5 → cantidad de elementos. #La coma indica que es una tupla de una sola dimensión
print()

#Imprimir número total de elementos que contiene el array
print("Número de total de elementos que contiene el Array 1:")
print(array1.size)
print()

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución Ejercicio 3

#Crear Array 2D

array2 = np.array([[1, 2, 3],
                [4,5,6]])

#Mostrar Array por terminal
print("Array 2:")
print(array2)
print()

#Imprimir número de dimensiones
print("Número de dimensiones del Array 2:")
print(array2.ndim)
print()

#Imprimir forma shape
print("Forma del Array 2:")
print(array2.shape) 
print()

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución 4

#Imprimir el primer elemento del Array 2D

# Validar que el array no esté vacío
if array2.size > 0:
    # Imprimir el primer elemento (fila 0, columna 0)
    primer_elemento = array2[0, 0]
    print("Primer elemento:\n ", primer_elemento)
else:
    print("El array está vacío.")

#Imprime el último elemento del array 2D
try:
    # Validar que el array no esté vacío
    if array2.size == 0:
        raise ValueError("El array está vacío.")
    # Obtener el último elemento usando índices negativos
    ultimo_elemento = array2[-1, -1]
    print(f"Último elemento:\n  {ultimo_elemento}")
except Exception as e:
    print(f"Error: {e}")

#Imprime un elemento específico usando índices de fila y columna.
elemento = array2[0, 2]
print("Elemento:\n ")
print(elemento)


#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución 5

#Creación del Array 1D

array_1dimension = np.array([1, 2, 3.7, 4])

#Imprimir Array
print("Array:\n ")
print(array_1dimension)
print()

#Tipo de Array
print("Tipo de dato interno de Array:\n")
print(array1.dtype)
print()

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución 6

array_modificaciones = np.array([100, 200, 300])

#Imprimir Array Original
print("Array Original:\n ")
print(array_modificaciones)
print()

#Cambiar valor
indice = 1
nuevo_valor = 99

if 0 <= indice < array_modificaciones.size:
    array_modificaciones[indice] = nuevo_valor
    #Imprimir el array modificado
    print(f"Array modificado (índice {indice} cambiado a {nuevo_valor}):\n", array_modificaciones )
else:
    print("Error: índice fuera de rango.")


#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución 7

#Creación de la lista
mi_lista = [5,4,8,1,3,2,10,6,9]

#Crear array=
array_lista= np.array([5,4,8,1,3,2,10,6,9])

#Imprimir ambas matrices
print("Lista:\n ")
print(mi_lista)
print()

print("Array:\n ")
print(array_lista)
print()

#------------------------------------------------------------------------------------------------------------------------------------------------
