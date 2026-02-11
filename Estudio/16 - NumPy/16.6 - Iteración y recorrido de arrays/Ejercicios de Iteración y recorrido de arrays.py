import numpy as np

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 1 — Recorrido básico (1D)

#Creación del array 1D
array_1dimension=np.arange(1, 11)
print("Array 1D")
print(array_1dimension)

contador=0

#Recorrer e imprimir elementos
for elementos in array_1dimension:
    print("Elemento:")
    print(elementos)
    contador += 1

#Número de elementos
print("Número total de elementos en el array 1D:")
print(contador)


#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 2 — Iterar y filtrar

# Creación del array 1D
array_1dimension = np.arange(10, 61)
print("Array 1D")
print(array_1dimension)

nueva_lista = []

# Recorrer array
for elemento in array_1dimension:
    if elemento > 50:
        # Guardarlo en una lista
        nueva_lista.append(int(elemento))

# Array final
print("Nueva Lista")
print(nueva_lista)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 3 — Iteración con índices

#Creación de nuevo array
nuevo_1dimension= np.arange(1, 6)

#Recorrer usando range
for indice in range(len(nuevo_1dimension)):
    print(f'Índice {indice} -> Valor {nuevo_1dimension[indice]}')

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 4 — `enumerate()`

#Creación de un nuevo array
nuevo_1dimension= np.arange(1, 11)
contador=0

#Imprimir indice y valor
for indice, valor in enumerate(nuevo_1dimension):
    contador+=1
    print(f'Recorrido N°{contador}')
    print(f'Índice {indice} -> Valor {valor}')

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 5 — Iteración en array 2D (filas)

#Crear una matriz de tamaño `(3, 4)`
array_2d = np.arange(1, 13).reshape(3, 4)
print("Array 2D")
print(array_2d)

#Recorrer Matriz por fila 
print("Iteración por filas")
for fila in array_2d:
    print(fila)

#Recorrer Matriz por columna
print("Iteración por columnas")
for columna in array_2d.T:
    print("Columna: ", columna)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 6 — Iteración elemento a elemento (2D)

#Recorrer valor elemento por elemento e imprimir su valor
for fila in array_2d:
    for elemento  in fila:
        print("Elementos:", elemento)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 7 — Iterar por columnas

#Recorrer Matriz por columna usado .T
print("Iterar por columnas con .T")
for columna in array_2d.T:
    print("Columna: ", columna)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 8 — `nditer` básico

#Recorrido del array 1D
print("Iteración del array usando nditer")
for x in np.nditer(nuevo_1dimension):
    print("Elemento:", x)

#Recorrido de la matriz
print("Iteración de la Matriz usando nditer")
for x in np.nditer(array_2d):
    print("Elemento:", x)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 9 — Modificación con `nditer`

#Crear nuevo array
nuevo_1dimension= np.arange(1, 11)


for x in np.nditer(nuevo_1dimension, op_flags=['readwrite']):
    x[...] = x * 2

print(nuevo_1dimension)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 10 — Modificación con `nditer`

array_2dimension = np.arange(1, 7).reshape(2, 3)
print("Matriz")
print(array_2dimension)

#Recorrer Usando `order='C'
print("Orden C (por filas):")
for x in np.nditer(array_2dimension, order='C'):
    print(x)

#Recorrer Usando `order='F'
print("Orden F (por columnas):")
for x in np.nditer(array_2dimension, order='F'):
    print(x)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 11 — Pensamiento crítico

array_2dimension = np.arange(1, 101).reshape(2, 50)

#Recorrido de la matriz
print("Iteración de la Matriz usando nditer")
for x in np.nditer(array_2dimension):
    print("Elemento:", x)

#Usando Vectorización

nueva_2dimension=array_2dimension**2
print("Vectorizado")
print(nueva_2dimension)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 12 — Caso real (análisis)
temperaturas = np.array([28.5, 30.2, 29.8, 31.0, 27.4, 26.8, 29.1])

nueva_temperatura=[]
for x  in np.nditer(temperaturas):
    if x > 27.6:
        nueva_temperatura.append((x.item()))
    
# Array final
print("Nuevas temperaturas")
print(nueva_temperatura)
