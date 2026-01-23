import numpy as np

np.random.seed(42)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 1 — Ajuste de valores grandes

datos_1d = np.random.randint(1, 100, size=8)
print(datos_1d)

print("Media:",np.mean(datos_1d))

log_datos=np.log(datos_1d)
print("Logaritmo Natural:",log_datos)
print("Media después de sacar el logaritmo natural:",np.mean(log_datos))

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 2 — Raíz cuadrada para suavizar datos

senales_1d = np.random.uniform(1, 100, size=15)
print(senales_1d)

#Valor mpaximo
print("Valor Máximo en el array:",np.max(senales_1d))

#Aplicar np.sqrt()
raiz_2=np.sqrt(senales_1d)
print("Raíz cuadrada:",raiz_2)

print("Valor Máximo en el array:",np.max(raiz_2))

# La raíz cuadrada reduce los valores grandes, suavizando la señal

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 3 — Valores negativos (errores de medición)

valores_norm = np.random.randint(-50, 50, size=15)
print(valores_norm)

#Media
print("Media:",np.mean(valores_norm))

#Calcular valor absoluto
valor_abs=np.abs(valores_norm)
print("Valor Absoluto:",valor_abs)
print("Media apartir del valor absoluto:",np.mean(valor_abs))

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 4 — Potencias y comparación

muestras = np.random.randint(1, 50, size=15)

#Media
print("Media Original:",np.mean(muestras))

valores_2=np.square(muestras)
print("Elevado al cuadrado:",valores_2)

#Media
print("Media al cuadrado:",np.mean(valores_2))

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 5 — Potencias y comparación

muestras_1d = np.random.uniform(1, 100, size=15)
print(muestras_1d)

rounded_data = np.round(muestras_1d, 2)
print("Redondeo de 2 cifras:",rounded_data)

rounded_down = np.floor(muestras_1d)
print("Redondeo hacia abajp:",rounded_down)

rounded_up = np.ceil(muestras_1d)
print("Redondeo hacia arriba:",rounded_up)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 6 — Operaciones matemáticas en matriz

# Parámetros
dias = 3
horas = 4

# Matriz de temperaturas en °C
temperaturas = np.round(
    np.random.uniform(15, 35, size=(dias, horas)),
    2
)

#Aplicar `np.sqrt()` a toda la matriz
raices = np.sqrt(temperaturas)
print("Raíz aplicada a las temperaturas:",raices)

#Calcular media por filas y columnas
media_columna=np.mean(temperaturas, axis=0)
print("Media por columnas:",media_columna)

media_filas=np.mean(temperaturas, axis=1)
print("Media por filas:",media_filas)


#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 7 — Comparar dos transformaciones

datos=np.random.randint(1, 100, size=15)
print("Original:", datos)

#Aplicar np.sqrt()
raiz_datos=np.sqrt(datos)
print("Raíz cuadrada:",raiz_datos)

#Aplicar np.log()

loga_datos=np.log(datos)
print("Logaritmo natural:",loga_datos)

"""
Interpretación:

*   La raíz cuadrada mantiene más las diferencias entre los valores.

*   El logaritmo comprime más los valores grandes, haciendo la escala más “uniforme” visualmente.
"""

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 8 — Mini flujo completo (Muy controlado)

# Crear array 1D positivo
dato_1 = np.random.randint(1, 100, size=10)
print("Datos originales:", dato_1)

# Logaritmo natural
loga_datos = np.log(dato_1)
print("Log natural:", loga_datos)

# Redondeo a 3 decimales
rounded_log = np.round(loga_datos, 3)
print("Log redondeado a 3 decimales:", rounded_log)

# Estadísticas del array original
print("Media:", np.mean(dato_1))
print("Dato mínimo:", np.min(dato_1))
print("Dato máximo:", np.max(dato_1))