import numpy as np

"""
1. No revisar shape
"""

#Error común
array_a=np.array([1,2,3])
array_b=np.array([[1], [2], [3]])

print("Suma de arrays:",array_a+array_b)

#Resultado inesperdo por broadcasting

#Buena práctica
print("Shape de array a:",array_a.shape)
print("Shape de array b:",array_b.shape)

#Siempre revisa el shape

"""
Confundir vista con copia
"""

arr=np.array([10,20,30,40])
sub=arr[1:3]
sub[0]=999

print("Array:",arr)

#El original cambia sin querer

#Buena Práctica
sub = arr[1:3].copy()

#Usa copy() si vas a modificar

"""
No especificar el axis
"""

#Error común

mat = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Promedio:",np.mean(mat))

#No sabes si es or filas o columnas
print("Promedio por columnas;",np.mean(mat, axis=0))  
print("Promedio por filas:",np.mean(mat, axis=1))

#Siempre indica el eje

"""
Usar bucles en lugar de vectorización
"""

#Error común

arr = np.array([1, 2, 3, 4])
resultado = []

for x in arr:
    resultado.append(x ** 2)


#Buena práctica
resultado = arr ** 2

#Más corto, más rápido, más claro

"""
Ignorar valores NaN
"""

#Error común
arr = np.array([10, 20, np.nan, 30])
print("Promedio:",np.mean(arr))

#Resultado: nan.

#Buena práctica
print("Promedio:",np.nanmean(arr))

#Usa funciones nan*.

"""
No revisar dtype
"""

#Error común
arr = np.array([1, 2, 3])
arr = arr / 2
print("Resultado:",arr)

#Puede generar confusión si esperas enteros.

#Buena práctica
print("Tipo de dato:",arr.dtype)

#El tipo de dato importa.

"""
reshape() incorrecto
"""

#Error común
arr = np.array([1, 2, 3, 4, 5])
# arr.reshape(2, 3)

#Error: tamaños incompatibles

#Buena práctica
arr.reshape(1, -1)

#Verificar siempre size

"""
Comparaciones mal hechas con arrays
"""
#Error común
arr = np.array([5, 12, 7])

"""
if arr > 10:
    print("Mayor")
"""

#Error lógico


#Buena práctica

print(arr[arr > 10])
"""
O:
print(np.any(arr > 10))


Usa operaciones vectorizadas.

"""

"""
Nombres poco claros
"""

#Error común
x = np.array([1, 2, 3])

#Buena práctica
ventas_diarias = np.array([1, 2, 3])

#El nombre explica el dato

"""
No documentar transformaciones
"""

#Error común
arr = np.log(arr)
arr = arr / np.max(arr)

#Nadie sabe por qué

#Buena práctica

# Aplicamos log para reducir escala
arr = np.log(arr)

# Normalizamos entre 0 y 1
arr = arr / np.max(arr)


#Comentar el por qué, no solo el qué

"""
Optimizar demasiado pronto

 Error común

Código difícil de leer solo por “eficiencia”.

Buena práctica

✔ Primero claridad
✔ Luego optimización
"""

"""
No validar resultados
"""

#Error comun
print(resultado)

#Y confiar

#Buena práctica
print("Min:", np.min(resultado))
print("Max:", np.max(resultado))
print("Media:", np.mean(resultado))

#Verificar siempre



