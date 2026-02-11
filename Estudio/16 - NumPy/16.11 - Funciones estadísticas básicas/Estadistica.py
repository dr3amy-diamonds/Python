import numpy as np

#Media(mean)

datos=np.array([10,20,30,40,100])

media=np.mean(datos)
print("Media:",mean)

"""
Qué observar

*   El valor 100 eleva la media

*   Sensible a outliers
"""

#Mediana(median)
mediana=np.median(datos)
print("Mediana:",mediana)

"""
*   Más representativa cuando hay valores extremos
"""

#Moda(valor más frecuente)

datos=np.array([1,2,2,3,4,4,4,5])

valores, conteos=np.unique(datos, return_counts=True)
moda=valores[np.argmax(conteos)]

print("Mods:",moda)

"""
*   NumPy no tiene mode directa
*   Se construye con herramientas básicas
"""

#Varianza(var)
datos = np.array([10, 12, 14, 16, 18])

varianza = np.var(datos)
print("Varianza:",varianza)

"""
*   Mide dispersión
*   Unidades al cuadrado
"""

#Desviación estándar(std)
std = np.std(datos)
print("Desviación Estandar:",std)

"""
*   Más intuitiva que la varianza
"""

#Rango(max-min)
rango = np.max(datos) - np.min(datos)
print("Rango:",rango)

"""
*   Muy sensible a outliers
"""

#Percentiles
datos = np.array([10, 20, 30, 40, 50, 60, 70])

p25 = np.percentile(datos, 25)
p50 = np.percentile(datos, 50)
p75 = np.percentile(datos, 75)

print("Percentil 1:",p25,"Percentil 2:", p50,"Percentil 3:", p75)

"""
*   Divide datos por posición
"""

#Cuartiles e IQR
q1 = np.percentile(datos, 25)
q3 = np.percentile(datos, 75)

iqr = q3 - q1

print("IQR:",iqr)

"""
*   Ideal para detectar outliers
"""

#Estadisticas por eje(axis)
matriz = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Columnas:",np.mean(matriz, axis=0)) 
print("Filas:",np.mean(matriz, axis=1)) 

"""
*   axis=0 → vertical
*   axis=1 → horizontal
"""

#Valores faltantes(NaN)
datos = np.array([10, 20, np.nan, 40])

print(np.mean(datos))        # da NaN
print(np.nanmean(datos))     # ignora NaN

"""
*   Usa funciones nan* en datos reales
"""

#Estadisticas combinadas
datos = np.array([5, 10, 15, 20, 25])

print("Dato Minimo:",np.min(datos))
print("Dato máximo",np.max(datos))
print("Media:",np.mean(datos))
print("Desviación Estandar:",np.std(datos))

"""
Error común (ejemplo)

❌ Usar solo la media:

np.mean(datos)


✔ Mejor:

np.mean(datos)
np.median(datos)
np.percentile(datos, [25, 75])

| Medida      | Función         |
| ----------- | --------------- |
| Media       | mean            |
| Mediana     | median          |
| Moda        | unique + counts |
| Varianza    | var             |
| Desviación  | std             |
| Rango       | max − min       |
| Percentiles | percentile      |
| Robusto     | IQR             |
| Ejes        | axis            |
| NaN         | nan*            |

"""
