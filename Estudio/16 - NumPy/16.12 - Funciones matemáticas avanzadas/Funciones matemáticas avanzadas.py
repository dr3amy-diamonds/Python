import numpy as np

"""
16.12 — FUNCIONES MATEMÁTICAS AVANZADAS
Ejemplos integrados (nivel intermedio)
"""

#EXPONENCIALES + ESTADÍSTICA + SHAPE : Simular crecimiento de usuarios y analizarlo.

#dias
dias=np.arange(1,11)

#crecimiento exponencial
usuarios=np.exp(dias/3)

print("Usuarios:",usuarios)

print("Shape:",usuarios.shape)
print("Media:",np.mean(usuarios))
print("Máximo:",np.max(usuarios))

"""
Qué se refuerza aquí:

*   exp() (matemática avanzada)

*   arrays 1D

*   funciones estadísticas

*   interpretación de crecimiento no lineal
"""

#LOGARITMOS + LIMPIEZA DE DATOS: Ingresos con valores muy grandes (sesgados).

ingresos = np.array([100, 200, 500, 5000, 20000, 100000])

log_ingresos=np.log(ingresos)

print("Original:",ingresos)
print("Log Transformado:",log_ingresos)

print("Media Antes:",np.mean(ingresos))
print("Media Después:",np.mean(log_ingresos))

"""
Concepto clave:

*   log reduce escalas

*   prepara datos para análisis y ML

*   transformación sin perder orden relativo
"""

#POTENCIAS + OPERACIONES VECTORIALES: Calcular error cuadrático (base de ML).
real = np.array([10, 12, 15, 18])
predicho = np.array([11, 11, 14, 20])

error=real-predicho
error_cuadrado=error**2

print("Errores:", error)
print("Errores al cuadrado:", error_cuadrado)
print("Error medio:", np.mean(error_cuadrado))

"""
Aquí usas:

*   potencias

*   broadcasting

*   estadística

*   operaciones matemáticas reales
"""

#RAÍCES + DISTANCIA (MUY IMPORTANTE): Distancia euclidiana entre dos puntos (ML / clustering).

punto_a = np.array([2, 3])
punto_b = np.array([6, 7])

distancia=np.sqrt(np.sum((punto_a-punto_b)**2))

print("Distancia:",distancia)

"""
Esto es:

*   raíz cuadrada

*   potencias

*   suma

*   fórmula matemática aplicada a datos
"""

#TRIGONOMETRÍA + SHAPE + TRANSPOSE: Simulación de ondas.

x=np.linspace(0,2*np.pi,5)

seno=np.sin(x)
coseno=np.cos(x)

ondas=np.vstack([seno,coseno])

print("Ondas:",ondas)
print("shape:",ondas.shape)
print("Transpuesta:",ondas.T)

"""
Refuerza:

*   trigonometría

*   unión de arrays

*   shape

*   .T
"""

#REDONDEO + PRESENTACIÓN DE DATOS: Resultados listos para reporte

valores=np.random.rand(5)*100

print("Original:", valores)
print("Redondeado:", np.round(valores, 2))
print("Ceil:", np.ceil(valores))
print("Floor:", np.floor(valores))

"""
Diferencia:

*   cálculo ≠ presentación

*   redondear al final
"""

#NORMALIZACIÓN (CLAVE PARA ML)

datos = np.array([50, 80, 120, 200])

min_val=np.min(datos)
max_val=np.max(datos)

normalizado=(datos-min_val)-(max_val-min_val)

print("Datos:", datos)
print("Normalizado:", normalizado)

"""
Aquí usas:

*   estadística

*   operaciones matemáticas

*   transformación de escala
"""

#ESTANDARIZACIÓN + ESTADÍSTICA

datos = np.array([10, 12, 15, 20, 30])

media=np.mean(datos)
std=np.std(datos)

z_scores=(datos-media)/std

print("Datos:", datos)
print("Z-scores:", z_scores)
print("Media Z:", np.mean(z_scores))
print("STD Z:", np.std(z_scores))

"""
Esto es obligatorio antes de:

*   regresión

*   clustering

*   PCA
"""

#ESTABILIDAD NUMÉRICA

valores = np.array([1e-10, 1e-5, 1, 10])
print("Log Normal:",np.log(valores))
print("Log Sefuro:",np.log1p(valores))

"""
*   log1p evita errores con valores pequeños.
"""

#PIPELINE REALISTA (TODO JUNTO)

datos = np.random.randint(1, 1000, size=10)

#Transformar
log_data=np.log(datos)

#Normalizar

norm=(log_data-np.min(log_data))/(np.max(log_data)-np.min(log_data))

# estadística
print("Datos originales:", datos)
print("Log:", log_data)
print("Normalizados:", norm)
print("Media:", np.mean(norm))
print("STD:", np.std(norm))