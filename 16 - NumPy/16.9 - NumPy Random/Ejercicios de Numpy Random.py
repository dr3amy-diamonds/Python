import numpy as np

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 1 — Reproducibilidad

np.random.seed(42)

datos_1=np.random.random(3)
datos_2 = np.random.randint(0, 10, size=5)

print("Array 1:", datos_1)
print("Array 2:", datos_2)

"""
La semilla ayuda a que esos números se mantengan fijos sin importar cuantas veces se ejecute
"""
#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 2 — Uniforme básico

#Generar números aleatorios

valores = np.random.random(4)
print("Números aleatorios uniformes:",valores)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 3 — Uniforme con rango

valores_2=np.random.uniform(low=20, high=50, size=15)
print("Valores en un rango especifico:",valores_2)

#Mostrar minimo
valor_min=np.min(valores_2)
print("Valor Minimo:", valor_min)

#Mostrar Máximo
valor_max=np.max(valores_2)
print("Valor Máximo:", valor_max)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 4 — Enteros aleatorios

lanzamientos = np.random.randint(1,7, size=20)
print("Array de Lanzamientos")
print(lanzamientos)
print("\n")

#Contar cuantas veces aparece cada número
for i in range(1, 7):
    print(f"Número {i}: {np.sum(lanzamientos == i)} veces")

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 5 — Distribución normal

normal = np.random.normal(loc=100, scale=15, size=100)
print("\n")
print("Distribución normal")
print(normal)
print("\n")

#Calcular media
suma_total=np.sum(normal)
print(suma_total)

num_elementos = len(normal)
print("Cantidad de elementos:", num_elementos)

media_normal=suma_total/num_elementos
print("La media normal es:", media_normal)

print("Diferencia con la media esperada:", media_normal - 100)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 6 — Binomial

binomial = np.random.binomial(n=10, p=0.4, size=50)
print("Distribución Binomial")
print(binomial)
print("\n")

#Valor que más se repite
# Obtiene valores únicos y sus conteos
valores, conteos = np.unique(binomial, return_counts=True)

# Encuentra el índice del conteo máximo
indice_max_conteo = np.argmax(conteos)
valor_mas_frecuente = valores[indice_max_conteo]
print(f"El valor más frecuente es: {valor_mas_frecuente}")

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 7 — Poisson

poisson = np.random.poisson(lam=3, size=30)
print("Distribución Poisson")
print(poisson)
print("\n")

# Análisis de variabilidad
media = np.mean(poisson)
desviacion = np.std(poisson)

print(f"Media: {media:.2f}")
print(f"Desviación estándar: {desviacion:.2f}")

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 8 — Muestreo sin reemplazo

items=np.arange(1,21)
print("Items")
print(items)

muestra = np.random.choice(items, size=5, replace=False)
print("Muestreo Aleatorio")
print(muestra)
print("\n")

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 9 — Muestreo sin reemplazo

muestra_2 = np.random.choice(items, size=10, replace=True)
print("Muestreo Aleatorio")
print(muestra_2)
print("\n")

print("Compración")
print(muestra)
print(muestra_2)
print("\n")

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 10 — Shuffle vs Permutation

elementos=np.arange(1,11)

#Mezclarlo usando shuffle
np.random.shuffle(elementos)
print("Array Modificado")
print(elementos)
print("\n")

#Mezclarlo usando permutation
mezclado = np.random.permutation(elementos)
print("Array mezclado")
print(mezclado)
print("\n")

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 11 — Generador moderno

rng = np.random.default_rng(42)


uniformes = rng.random(5)  
print("Uniformes:", uniformes)


enteros = rng.integers(10, 20, size=5)
print("Enteros:", enteros)


normales = rng.normal(0, 1, size=5)
print("Normales:", normales)

"""
Este maneja mejor control en los números generados, creando así un código más limpio y optimizado
"""