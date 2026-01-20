import numpy as np

#Semilla(sedd) -- reproducibilidad

np.random.seed(42)

a=np.random.random(5)
b=np.random.random(5)

print("Primer Valor")
print(a)
print("\n")
print("Segundo Valor")
print(b)
print("\n")

"""
Qué demuestra

Cada ejecución con la misma semilla genera los mismos valores

Fundamental para experimentos reproducibles

*   Sin semilla: resultados distintos cada vez
*   Con semilla: control total
"""

# Números aleatorios uniformes (0 a 1)

valores = np.random.random(4)
print("Números aleatorios uniformes")
print(valores)
print("\n")

"""
*   Distribución uniforme
*   Todos los valores tienen la misma probabilidad
"""

#Uniforme en un rango específico

valores_2=np.random.uniform(low=10, high=20, size=50)
print("Valores en un rango especifico")
print(valores_2)
print("\n")

"""
✔ Útil para simulaciones
✔ Rango controlad
"""

#Enteros aleatorios

enteros = np.random.randint(1,7, size=10)
print("Enteros aleatorios")
print(enteros)
print("\n")

"""
*   Simula un dado
*   Muy usado en muestreo
"""

# Distribución normal(gaussiana)

normal = np.random.normal(loc=50, scale=10, size=10)
print("Distribución normal")
print(normal)
print("\n")

"""
Parámetros:

*   loc → media

*   scale → desviación estándar

*   Clave en análisis estadístico
"""

#Distribución binomial
binomial = np.random.binomial(n=10, p=0.3, size=10)
print("Distribución Binomial")
print(binomial)
print("\n")

"""
*   Número de éxitos en 10 intentos
*   Probabilidad 0.3 de éxito
"""

#Distribución Poisson
poisson = np.random.poisson(lam=3, size=10)
print("Distribución Poisson")
print(poisson)
print("\n")

"""
*   Eventos por intervalo
*   Análisis de conteos
"""

#Muestreo aleatorio(choice)

datos = np.array([10, 20, 30, 40, 50])

muestra = np.random.choice(datos, size=3, replace=False)
print("Muestreo Aleatorio")
print(muestra)
print("\n")

"""
*   Selección sin reemplazo
*   Muy usado en ML
"""

#Mezclar datos (shuffle vs permutation)

arr = np.array([1, 2, 3, 4, 5])

np.random.shuffle(arr)
print("Array Original")
print(arr)
print("\n")
#Modifica el original

mezclado = np.random.permutation(arr)
print("Array mezclado")
print(mezclado)
print("\n")
#No modifica el original

#Generador Moderno(default_rng)
rng = np.random.default_rng(seed=42)

valores = rng.random(5)
enteros = rng.integers(1, 10, size=5)

print("Valores")
print(valores)
print("\n")
print("Enteros")
print(enteros)
print("\n")

"""
✔ Recomendado por NumPy
✔ Código más limpio
✔ Mejor control
"""

#Comparació: Método Antiguo Vs Moderno
#Antiguo
np.random.random(3)

#Moderno
rng = np.random.default_rng()
rng.random(3)

#El moderno es el estándar actual

"""
Errores comunes (con ejemplo)

❌ No fijar semilla:

np.random.random(3)


✔ Mejor:

rng = np.random.default_rng(123)
rng.random(3)
"""