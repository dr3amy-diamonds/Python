import numpy as np

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 1 — Filtrado básico

arrayDatos=np.arange(1,11)*10
print("Array de Datos")
print(arrayDatos)
print("\n")

#Filtrar todos los valores mayores a 50
try:
    condicion= arrayDatos> 50
    #Ahora usamos la máscara
    filtrados= arrayDatos[condicion]
    print("Números mayores a 50")
    print(filtrados)
    print("\n")
except:
    print("No hay valores en el array")


#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 2 — Búsqueda de posiciones

valores_enteros=np.array([10, -2, 41, -8, -7, -75, 15, 25])

#Encontrar valores donde las posiciones son negativas 
indices_negativos=np.where(valores_enteros < 0)[0]
valores_negativos = valores_enteros[indices_negativos]
print("Índices:", indices_negativos)
print("Valores:", valores_negativos)
print("\n")

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 3 — Máximo y mínimo con posición

elementos=np.array([5, 14, 2, 8, 19, 58, 84, 21, 45, 4])

#Obtener el valor máximo/minimo y su posición
pos_max=np.argmax(elementos)
pos_min=np.argmin(elementos)

print("Posición Máxima, Valor Máximo")
print(pos_max, elementos[pos_max])
print("\n")
print("Posición Minima, Valor Minimo")
print(pos_min, elementos[pos_min])
print("\n")

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 4 — Filtrado por pertenencia

items=np.arange(1,15)*2
print("Items Originales")
print(items)
print("\n")

permitidos=[14]

mask = np.isin(items, permitidos)
print("Valores Booleanos")
print(mask)
print("\n")
print("Valores")
print(items[mask])
print("\n")

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 5 — Ordenación simple

elementos = np.array([11,  8,  5, 13, 10,  9,  6,  7, 12])
print("Array")
print(elementos)
print("\n")

#Ordenar de menor a mayor
elementos_sorted=np.sort(elementos)
print("Array Ordenado de menor a mayor")
print(elementos_sorted)
print("\n")

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 6 — Ordenación con relación entre arrays

array_nombres=np.array(["Tina", "Cox", "Susie", "Bush", "Jennifer","Nicholson"])
array_estaturas=np.array([1.62, 1.78, 1.59, 1.68, 1.85, 1.84])

#Ordenar array según por estatyra(Mayor a menor)
orden=np.argsort(array_estaturas)[::-1]
print("Ordenado por estatura")
print(array_nombres[orden])
print(array_estaturas[orden])
print("\n")

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 7 — Ordenación por filas y columnas

datos_matriz=np.arange(1,13).reshape(3,4)
np.random.shuffle(datos_matriz)
print("Matriz")
print(datos_matriz)
print("\n")

print("Ordenar valores por filas")
matriz_ordenada=np.sort(datos_matriz,axis=1)
print(matriz_ordenada)
print("\n")

print("Ordenar valores por columnas")
matriz_ordenada=np.sort(datos_matriz,axis=0)
print(matriz_ordenada)
print("\n")

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 8 — Ordenación parcial (Top N)

#Creación de array usando np.radom para números random y desorden del array
datos_aleatorios = np.random.randint(1, 101, size=10)
print("Datos")
print(datos_aleatorios)
print("\n")

#Obtener los 3 valores más grande
top3 = np.partition(datos_aleatorios, -3)[-3:]
print("Top 3")
print(top3)
print("\n")

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 9 — Detección de valores válidos

valores_posibles = np.array([0, 0, 0, 5, 10, 15, 20, 25, 30, 35])
datos = np.random.permutation(valores_posibles)
print("Array")
print(datos)
print("\n")

#Detectar las posiciones donde los valores no son ceros
indices_no_cero = np.nonzero(datos)[0]
print("Posiciones donde los valores no son ceros")
print(indices_no_cero)
print("\n")

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 10 — Error común (reflexión)
datos_random=np.arange(1,20)

#Usando for
for x in datos_random:
    if x > 15:
        print("Dato: ", x)
print("\n")
#Usando Numpy Vectorizado
indices = np.where(datos_random>15)[0]  
print("Índices")
print(indices)
print("\n")

"""
1️. Cuál es más claro:

*   Para análisis de datos, la versión vectorizada con Numpy es más clara porque deja explícito que estoy trabajando con todo el conjunto de datos a la vez, en lugar de recorrerlos uno por uno.

*   El for es más legible para principiantes, pero en datasets grandes puede volverse confuso y tedioso.

2️. Cuál es más eficiente:

*   Sin duda, Numpy vectorizado. En análisis de datos normalmente manejo miles o millones de registros, y los loops explícitos son demasiado lentos.

*   El for se vuelve ineficiente rápidamente con datos grandes.

3️. Cuál deberías usar:

*   Siempre vectorización o funciones de Numpy/Pandas, porque son rápidas, concisas y escalables.

*   El for solo lo usaría para pruebas rápidas o cuando el dataset es pequeño y no importa la eficiencia.
"""