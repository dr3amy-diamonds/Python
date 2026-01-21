import numpy as np


#Operaciones aritméticas directas
array_a=np.array([1,2,3])
array_b=np.array([4,5,6])

print("Suma:", array_a+array_b)
print("Resta:", array_a-array_b)
print("Multiplicación:",array_a*array_b)
print("División:",array_a/array_b)

"""
*   Elemento a elemento
*   Sin bucles
*   Ultra rápido
"""

#Operaciones con escalares(broadcasting)
matriz=np.arange(1,7).reshape(2,3)

vector=np.arange(1,4)*10

print("Suma de Matriz y Vector:", matriz+vector)

"""
*   El vector se aplica a cada fila
*   No hay copias internas
"""

#Ufuncs matemáticas básicas
x=np.array([1,4,9,16])

print("Raíz Cuadrada:",np.sqrt(x))
print("Elevar un número al cuadrado:",np.square(x))
print("Valor Absoluto:",np.abs([-3, -1, 0, 2]))

"""
*   Funciones universales
*   Vectorizadas
"""

#Logaritmos y exponenciales
x=np.array([1,10,100])

print("Log Natural:", np.log(x))
print("Log base 10:", np.log10(x))
print("Exponencial:",np.exp([1,2,3]))

"""
*   Usadas en ML y estadística
"""

#Reducciones Globales

datos=np.arange(1,5)*10

print("Suma:",np.sum(datos))
print("Media:",np.mean(datos))
print("Valor máximo:",np.max(datos))
print("Valor Minimo:",np.min(datos))
print("Desvación Estandar:",np.std(datos))

"""
*   Devuelven un solo valor
"""

#Reducciones por eje (axis)
matriz=np.arange(1,7).reshape(2,3)*10

print("Suma de columnas:",np.sum(matriz,axis=0))
print("Suma de filas:",np.sum(matriz,axis=1))

"""
*   Control total de agregación
"""

#Operaciones acumulativas
datos=np.arange(1,5)

print("Suma Acumulativa:",np.cumsum(datos))
print("Producto Acumulativo:",np.cumprod(datos))

"""
*   Evolución del cálculo
*   Series temporales
"""

#Comparaciones Vectorizadas

datos=np.array([10, 50, 80 , 30])

print("Datos mayores a 40:",datos>40)
print("Datos iguales a 30:",datos==30)

"""
*   Devuelve booleanos
*   Base del filtrado
"""

#Lógica booleana combinada

datos=np.arange(1,6)*10

condicion=(datos>=20) & (datos<=40)
print("Condición:",datos[condicion])

"""
*   AND → &
*   OR → |
*   NOT → ~
"""

#Operaciones in-place(memoria eficiente)

datos=np.array([1,2,3])

datos += 10
print("Suma:",datos)

"""
*   Modifica el original
*   Cuidado en análisis
"""

#Funciones matemáticas avanzadas

x=np.array([1.2,2.7,3.5])

print("Redondear de abajo:",np.floor(x))
print("Redondear de arriba:",np.ceil(x))
print("Redondear Números:",np.round(x))

"""
*   Limpieza y normalización
"""

#np.clip()--limitar valores

datos=np.array([5,15,25,35])

print("Valores Limitados:",np.clip(datos,10,30))

"""
*   Control de outliers
"""

#np.where() como operador matemático

datos=np.arange(1,5)*10

resultado=np.where(datos > 25, datos*2,datos)
print("Resultado:",resultado)

"""
*   Lógica + matemática
*   Muy potente
"""