import numpy as np

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución 1
array1 =np.array([2, 4, 6, 8, 10, 12])

#Imprimir primer elemento
print(array1[0])

#Imprimir último elemento
print(array1[-1])

#Imprimir tercer elemento
print(array1[2])

#------------------------------------------------------------------------------------------------------------------------------------------------
#Solución 2

#Accede al penúltimo valor
print(array1[-2])

#Acceder al antepenultimo valor
print(array1[-3])

#------------------------------------------------------------------------------------------------------------------------------------------------
#Solución 3

#Extraer los tres primeros elementos
primeros_3=array1[:3]
print("'Primeros tres elementos':", primeros_3)

#Extrae los últimos 3 elementos
ultimos_3=array1[3:]
print("'Últimos tres elementos':", ultimos_3)

#Extrae todos los elementos excepto el primero y el último
first_last=array1[1:-1]
print("'Todos los elementos, excepto el primero y el último':", first_last)

#------------------------------------------------------------------------------------------------------------------------------------------------
#Solución 4

#Extrae los elementos en posiciones pares
pares = array1[::2]  # Desde el índice 0, saltando de 2 en 2

print("Array original:", array1)
print("Elementos en posiciones pares:", pares)

#Extrae los elementos en posiciones impares
impares = array1[1::2]  # Desde el índice 0, saltando de 2 en 2

print("Array original:", array1)
print("Elementos en posiciones impares:", impares)

#------------------------------------------------------------------------------------------------------------------------------------------------
#Solución 5

array_d2 = np.array([[1, 2, 3], 
                    [4, 5, 6], 
                    [7, 8, 9]])
print(array_d2)

#Imprimir el elemento central
filas, columnas = array_d2.shape 
centro = array_d2[filas//2, columnas//2] 
print("El centro del elemento es: ", centro)

#Imprimir la primera fila del array
print("Primera Fila: ", array_d2[0])

#Imprimir la última columna
ultima_columna = array_d2[:, -1]
print("Última Columna: ", ultima_columna)

#------------------------------------------------------------------------------------------------------------------------------------------------
#Solución 6

#Accede al valor en la fila 2, columna 1
elemento = array_d2[1, 0]
print("\nElemento en fila 2, columna 1:", elemento)

#Accede al valor en la fila 0, columna 2
elemento = array_d2[0, 1]
print("\nElemento en fila 0, columna 2:", elemento)

#------------------------------------------------------------------------------------------------------------------------------------------------
#Solución 7

#Extrae una submatriz 2×2 de la esquina superior izquierda
submatriz = array_d2[0:2, 0:2]

print("Array original:")
print(array_d2)

print("\nSubmatriz 2x2 (esquina superior izquierda):")
print(submatriz)

#Extrae una submatriz 2×2 de la esquina inferior derecha
submatriz2 = array_d2[-2:, -2:]

print("Array original:")
print(array_d2)

print("\nSubmatriz 2x2 (esquina inferior derecha):")
print(submatriz2)

#------------------------------------------------------------------------------------------------------------------------------------------------
#Solución 8

#Extraer las dos primeras filas y las dos primeras columnas
submatriz = array_d2[:2, :2]

print("Matriz original:")
print(array_d2)

print("\nSubmatriz (2 primeras filas y columnas):")
print(submatriz)

#Extrae solo la fila central
fila_central = array_d2[1, :]  
print("La fila central es: ", fila_central)

#Extrae solo la columna central
columna_central=array_d2[ :, 1]
print("La columna central es: ", columna_central)

#------------------------------------------------------------------------------------------------------------------------------------------------
#Solución 9

#Crear Array 1D
array_d1=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

#Extraer valores mayores de 5
umbral=5
indices = np.where(array_d1 > umbral)
print("Valores correspondientes:", array_d1[indices])

#Extraer solo los valores pares
indices_pares = np.where(array_d1 % 2 == 0)
pares = array_d1[indices_pares]
print(pares)
