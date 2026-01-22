import numpy as np
np.random.seed(42)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 1 — Tendencia central

datos=np.arange(41,55)
np.random.shuffle(datos)
print(datos)

print("Media:",np.mean(datos))
print("Mediana:",np.median(datos))

"""
### Reflexión

La **mediana** representa mejor los datos cuando existen valores extremos, ya que no se ve afectada por números muy altos o muy bajos. En cambio, la **media** puede distorsionarse si hay uno o más valores atípicos, alejándose del comportamiento general del conjunto de datos.
Por lo tanto, si los datos están distribuidos de forma irregular o contienen valores extremos, la mediana ofrece una representación más fiel de la tendencia central; si los datos son más homogéneos, la media resulta adecuada.

"""

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 2 — Moda

datos = np.random.randint(41, 50, size=10)
print(datos)

valores,conteos=np.unique(datos,return_counts=True)
indice_max=np.argmax(conteos)
moda=valores[indice_max]
print("Moda:",moda, ", Frecuencia:", int(conteos[indice_max])
)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 3 — Dispersión

elementos=np.arange(54,63)
np.random.shuffle(elementos)
print(elementos)


varianza = np.var(elementos)
print("Varianza:",varianza)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 4 — Percentiles y cuartiles

elementos=np.random.randint(40, 70, size=15)
np.random.shuffle(elementos)
print(elementos)


p25 = np.percentile(elementos, 25)
p50 = np.percentile(elementos, 50)
p75 = np.percentile(elementos, 75)
print("Percentil 1:",p25,"Percentil 2:", p50,"Percentil 3:", p75)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 5 — IQR y detección de outliers

q1 = np.percentile(elementos, 25)
q3 = np.percentile(elementos, 75)

iqr = q3 - q1
print("Rango Intercuartílico:",iqr)


#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 6 — Estadística por eje

items=np.arange(1,13).reshape(4,3)
np.random.shuffle(items)
print(items)

media_columnas=np.mean(items, axis=0)
print("Media por columnas:",media_columnas)
media_filas=np.mean(items, axis=1)
print("Media por filas:",media_filas)
desviacion_columna=np.std(items,axis=0)
print("Desviación estándar por columnas:",desviacion_columna)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 7 — Valores faltantes (NaN)

datos = np.array([85, np.nan, 12, 430, -25, 7.5, 300, 0, 1024, 3, -400, 58])

# Calcular la media
media = np.mean(datos)

print(f"La media es: {media}")

#Calcular ignorando NaN
media_sin_nan = np.nanmean(datos)
print("Media ignorando NaN:", media_sin_nan)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 8 — Integrador estadístico


# Crear array 2D de ejemplo (10 filas x 7 columnas)
items = np.arange(10, 80).reshape(10,7).astype(float)  # float para poder usar NaN
np.random.shuffle(items)
# Insertar un NaN en el array para el ejemplo
items[2, 3] = np.nan
print("Array 2D con NaN:\n", items)


# 1️. Estadísticas globales (ignorando NaN)
media_global = np.nanmean(items)
mediana_global = np.nanmedian(items)
min_global = np.nanmin(items)
max_global = np.nanmax(items)
std_global = np.nanstd(items)

print("\nEstadísticas globales (ignorando NaN):")
print("Media:", media_global)
print("Mediana:", mediana_global)
print("Mínimo:", min_global)
print("Máximo:", max_global)
print("Desviación estándar:", std_global)

# 2️. Estadísticas por eje
# Por filas (axis=1)
media_filas = np.nanmean(items, axis=1)
mediana_filas = np.nanmedian(items, axis=1)

# Por columnas (axis=0)
media_columnas = np.nanmean(items, axis=0)
mediana_columnas = np.nanmedian(items, axis=0)

print("\nMedia por filas:", media_filas)
print("Mediana por filas:", mediana_filas)
print("Media por columnas:", media_columnas)
print("Mediana por columnas:", mediana_columnas)

# 3️. Percentiles (ignorando NaN)
p25 = np.nanpercentile(items, 25)  # primer cuartil
p50 = np.nanpercentile(items, 50)  # mediana
p75 = np.nanpercentile(items, 75)  # tercer cuartil

print("\nPercentiles globales (ignorando NaN):")
print("25°:", p25)
print("50° (mediana):", p50)
print("75°:", p75)
