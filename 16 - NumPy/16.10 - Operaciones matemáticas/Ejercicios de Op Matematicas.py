import numpy as np

#------------------------------------------------------------------------------------------------------------------------------------------------

np.random.seed(42)
#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 1 — Operaciones básicas elemento a elemento

array_1=np.arange(1,7)
array_2=np.arange(7,13)
np.random.shuffle(array_1)
np.random.shuffle(array_2)

suma_total = array_1 + array_2
print("Suma de ambos arrays:", suma_total)
print(suma_total.shape)

resta_total = array_1 - array_2
print("Resta de los dos arrays:", resta_total)
print(resta_total.shape)

multiplicacion = array_1 * array_2
print("Multiplicación de los dos arrays:", multiplicacion)
print(multiplicacion.shape)

division = array_1 / array_2
print("División de los dos arrays:", division)
print(division.shape)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 2 — Broadcasting con escalar


array_1=np.arange(1,7)

# Sumar un escalar
arr_suma = array_1 + 10

# Multiplicar por otro escalar
arr_multiplica =array_1 * 3

print("Array original:", array_1)
print("Array después de sumar 10:", arr_suma)
print("Array después de multiplicar por 3:", arr_multiplica)

"""
Broadcasting es una característica de NumPy, permite realizar operaciones entre arrays de distintos tamaños
"""

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 3 — Broadcasting 2D con vector

coordenadas=np.arange(1,13).reshape(3,4)
array=np.arange(1,5)

suma_vecma=coordenadas+array
print("Suma de Vector y matriz:",suma_vecma)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 4 — Funciones universales (ufuncs)

elementos = np.array([-3,12,-55,14,-7,-9,-8,-65,45])

print("Valor Absoluto:",np.abs(elementos))
numeros_positivos = elementos[elementos > 0]
print("Raíz Cuadrada:", np.sqrt(numeros_positivos))
print("Potencia al cuadrado:",np.square(elementos))

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 5 — Estadísticas globales

items=np.arange(1,11)
np.random.shuffle(items)
print(items)

print("Suma Total:",np.sum(items))
print("Media:",np.mean(items))
print("Máxima:",np.max(items))
print("Mínimo:",np.min(items))
print("Desviación Estandar:",np.std(items))

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 6 — Estadísticas por eje

matriz_2=np.arange(1,13).reshape(4,3)
np.random.shuffle(matriz_2)
print(matriz_2)

suma_columna=np.sum(matriz_2,axis=0)
print("Suma por columnas:",suma_columna)
print(suma_columna.shape)
media=np.mean(matriz_2,axis=1)
print("Media por filas:",media)
print(media.shape)


#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 7 — Operaciones acumulativas

valores_diarios = np.random.randint(15, 31, size=7)

sum_acumulada=np.cumsum(valores_diarios)
print("Suma Acumulada:",sum_acumulada)
print(sum_acumulada.shape)
prod_acumulada=np.cumprod(valores_diarios)
print("Producto Acumulado",np.cumprod(valores_diarios))
print(prod_acumulada.shape)

"""
Este tipo de análisis se puede usar en:

Suma acumulada:

    Seguimiento de ventas o ingresos a lo largo del tiempo.

    Control de calorías consumidas o pasos diarios.

    Cualquier métrica donde importe el total acumulado.

Producto acumulado:

    Cálculo de crecimiento porcentual diario (por ejemplo, inversión compuesta).

    Modelos de multiplicación de probabilidades.

    Situaciones donde los efectos diarios se multiplican en vez de sumarse.
"""

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 8 — Comparaciones y filtrado

datos=np.arange(2,15)
np.random.shuffle(datos)
print(datos)

umbral = 5
mayores_que_umbral = datos[datos > umbral]
print("Valores mayores que 5:", mayores_que_umbral)

rango_min = 3
rango_max = 7
valores_en_rango = datos[(datos >= rango_min) & (datos <= rango_max)]
print("Valores entre 3 y 7:", valores_en_rango)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 9 — np.where()` con lógica

datos=np.arange(1,16)

resultado=np.where(datos > 5, datos*2,datos)
print("Resultado:",resultado)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 10 — Operaciones *in-place* vs copia

informacion=np.arange(1,16)
copia=informacion.copy()

copia += 10
print("Suma:",copia)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 11 — Control de valores extremos

valores_random = [25, 30, -5, 200, 150, 40]

print("Valores Limitados:",np.clip(valores_random,0,80))

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 12 — Integrador (nivel análisis real)
array2D = np.random.rand(5, 5)


array_escalado = array2D * 100
print("\nArray escalado (0-100):\n", array_escalado)


media_filas = np.mean(array_escalado, axis=1)
print("\nMedia por fila:", media_filas)


media_columnas = np.mean(array_escalado, axis=0)
print("Media por columna:", media_columnas)


std_filas = np.std(array_escalado, axis=1)
print("Desviación estándar por fila:", std_filas)


valores_filtrados = np.where((array_escalado > 90) | (array_escalado < 10), 0, array_escalado)
print("\nArray con valores extremos filtrados (reemplazados por 0):\n", valores_filtrados)


acumulativo_filas = np.cumsum(array_escalado, axis=1)
print("\nSuma acumulativa por filas:\n", acumulativo_filas)


acumulativo_columnas = np.cumsum(array_escalado, axis=0)
print("\nSuma acumulativa por columnas:\n", acumulativo_columnas)