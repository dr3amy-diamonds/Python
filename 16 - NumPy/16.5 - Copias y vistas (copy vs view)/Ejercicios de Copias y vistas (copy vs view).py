import numpy as np
import random 

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 1 — Vista básica

#Creación de array de una dimensión
array_1dimension=np.arange(1, 11)
print("Primer Array: Primera Dimensión:")
print(array_1dimension)

#Obtener parte usando slicing
recorte_1dimension=array_1dimension[0:5]
print("Corte: Vista del primer Array:")
print(recorte_1dimension)

#Modificar valor
recorte_1dimension[0:5] = random.sample(range(20), 5)
print("Array con nuevos elementos: ")
print(array_1dimension)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 2 — Copia segura

#Obtener subparte
segundo_recorte=array_1dimension[2:6]
print("Segundo Corte: Vista del primer Array:")
print(segundo_recorte)

#Creación de la copia
primera_copia=array_1dimension.copy()
primera_copia[2:6] = random.sample(range(4), 4)
print("Array Orginal: ")
print(array_1dimension)
print("Copia:")
print(primera_copia)

#No cambia el array original

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 3 — reshape y memoria

#Creación de array de una dimensión
segundo_array1d=np.arange(1, 7)
print("Array Original:")
print(segundo_array1d)

#Cambiar forma a 2 filas, 3 columnas
nueva_estructura=segundo_array1d.reshape(2,3)
print("Nueva Estructura:")
print(nueva_estructura)
print("Array Original:")
print(segundo_array1d)


#No cambia la original

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 4 — flatten vs ravel

#Creación de array 2D
array_2d = np.arange(1, 11).reshape(2, 5)
print("Array Original 2D: ")
print(array_2d)

#Convertir a 1D con flatten()
print("\nArray aplanado (1D):")
array_aplanado=array_2d.flatten()
print(array_aplanado)

#Modificar resultado
resultado_modificado=array_aplanado
resultado_modificado[0]=15
print("\nResultado Modificado (1D):")
print(resultado_modificado)

#Usando Ravel()

#Convertir a 1D con Ravel()
print("\nArray aplanado (1D):")
array_aplanado=array_2d.ravel()
print(array_aplanado)

#Modificar resultado
resultado_modificado=array_aplanado
resultado_modificado[0]=10
print("\nResultado Modificado (1D):")
print(resultado_modificado)

#Mostrar array 2D
print("Array Original 2D: ")
print(array_2d)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 5 — Transposición

#Creación de nuevo array 2D
nuevo_2d = np.arange(21, 31).reshape(2, 5)
print("Array Original 2D: ")
print(nuevo_2d)

#Obtén la transpuesta usando `.T`
print("\nTranspuesta del array:")
transpuesta_2d=nuevo_2d.T
print(transpuesta_2d)

#Modificar el valor de la transpuesta
modificacion_2d=transpuesta_2d
modificacion_2d[3,1]=95
print("\nResultado Modificado (2D):")
print(modificacion_2d)

#Mostrar array 2D
print("Array Original 2D: ")
print(nuevo_2d)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 6 — Referencias en Python

nuevo_array2d = np.arange(20, 35).reshape(3, 5)
print("Array Original 2D: ")
print(nuevo_array2d)

#Asignarlo a otra variable
variable_array2d=nuevo_array2d
variable_array2d[2,3]=1
print("\nResultado Modificado (2D):")
print(variable_array2d)

#Mostrar de nuevo el array
print("Array Original 2D: ")
print(nuevo_array2d)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 7 — Referencias en Python
"""
-   `arr[2:5]`  #Copia
-   `arr.copy()`    #Copia
-   `arr.flatten()` #Copia
-   `arr.ravel()`   #Vista
-   `arr.T` #Vista
-   `b = arr`   #Vista
"""

