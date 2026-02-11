import numpy as np

#------------------------------------------------------------------------------------------------------------------------------------------------
#INDEXADO BÁSICO EN ARRAY 1D

"""
*   Los índices empiezan en 0

*   Los índices negativos cuentan desde el final

*   Es acceso directo, no hay bucles

"""

array = np.array([10, 20, 30, 40, 50])

print("Array completo:", array)

# Acceder por índice
print("Primer elemento:", array[0])
print("Tercer elemento:", array[2])

# Indexado negativo
print("Último elemento:", array[-1])
print("Penúltimo elemento:", array[-2])

#------------------------------------------------------------------------------------------------------------------------------------------------

#SLICING EN ARRAY 1D (REBANADO)

"""
[inicio : fin : paso]

*   inicio → desde dónde

*   fin → hasta dónde (NO incluido)

*   paso → saltos
"""

print("Primeros tres elementos:", array[0:3])
print("Desde el segundo hasta el final:", array[1:])
print("Desde el inicio hasta el cuarto:", array[:4])
print("Cada dos elementos:", array[::2])

#------------------------------------------------------------------------------------------------------------------------------------------------

#ARRAY 2D (FILAS Y COLUMNAS)

matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Matriz completa:")
print(matriz)

#INDEXADO EN ARRAY 2D

print("Elemento fila 0, columna 1:", matriz[0, 1])
print("Elemento fila 2, columna 2:", matriz[2, 2])      #Regla mental: array[fila, columna]


#SELECCIONAR FILAS COMPLETAS
print("Primera fila:", matriz[0])
print("Última fila:", matriz[-1])

#SELECCIONAR COLUMNAS COMPLETAS
print("Primera columna:", matriz[:, 0])
print("Segunda columna:", matriz[:, 1])

#SLICING EN ARRAY 2D
print("Primeras dos filas:")
print(matriz[0:2, :])

print("Últimas dos columnas:")
print(matriz[:, 1:3])

print("Submatriz central:")
print(matriz[1:3, 1:3])

#------------------------------------------------------------------------------------------------------------------------------------------------

#DIFERENCIA IMPORTANTE: VISTA

sub = matriz[0:2, 0:2]
sub[0, 0] = 999

print("Submatriz modificada:")
print(sub)

print("Matriz original (también cambió):")
print(matriz)

"""
Concepto crítico:

*   slicing suele devolver una vista

*   modificarla afecta al array original

"""

#------------------------------------------------------------------------------------------------------------------------------------------------

#INDEXADO BOOLEANO (INTRODUCTORIO)

datos = np.array([5, 10, 15, 20, 25])

print("Datos mayores que 10:", datos[datos > 10])


