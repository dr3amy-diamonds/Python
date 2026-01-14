import numpy as np

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 1 — Unión básica por filas

#Creación de dos array 2D
Matriz_1=np.arange(1,9).reshape(2,4)
Matriz_2=np.arange(9,21).reshape(3,4)
print("Matriz Uno")
print(Matriz_1)
print("\n")
print("Matriz Dos")
print(Matriz_2)
print("\n")

#Unir filas
resultado=np.concatenate((Matriz_1,Matriz_2), axis=0)
print("Resultado de la concatenación ")
print(resultado)
print("\n")
#Imprimir shape
print(resultado.shape)
print("\n")

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 2 — Unión básica por columnas

#Creación de Matrices
Matriz_3=np.arange(1,9).reshape(2,4)
Matriz_4=np.arange(9,21).reshape(2,6)
print("Matriz Tres")
print(Matriz_3)
print("\n")
print("Matriz Cuatro")
print(Matriz_4)
print("\n")

#Unirlos por columnas
resultado=np.concatenate((Matriz_3,Matriz_4), axis=1)
print("Resultado de la concatenación ")
print(resultado)
print("\n")
#Imprimir shape
print("Shape")
print(resultado.shape)
print("\n")

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 3 — `concatenate` vs funciones especializadas

#Usando `concatenate`
resultado=np.concatenate((Matriz_1,Matriz_2), axis=0)
print("Resultado de la concatenación ")
print(resultado)
print("\n")

#Usando vstack
resultado=np.vstack((Matriz_1,Matriz_2))
print("Matriz  unida con Vstack \n")
print(resultado)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 4 — Error por incompatibilidad

Matriz_5=np.arange(2,6).reshape(4,1)
Matriz_6=np.arange(15,25).reshape(5,2)
print(Matriz_5.shape)
print(Matriz_6.shape)

try:
    resultado=np.vstack((Matriz_5,Matriz_6))
except:
    print("No se pueden unir, shapes incompatibles")

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 5 — Verificación previa

Matriz_7=np.arange(5,13).reshape(4,2)
Matriz_8=np.arange(11,19).reshape(2,4)

print("Shape de la Matriz 7")
print(Matriz_7.shape)
print("Shape de la Matriz 8")
print(Matriz_8.shape)

try:
    resultado=np.vstack((Matriz_7,Matriz_8))
except:
    print("No fue posible unirlas")

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 6 — Uso incorrecto de `stack`
#Crear arrays Iguales
Matriz_A=np.arange(1,11).reshape(2,5)
Matriz_B=np.arange(11,21).reshape(2,5)


resultado = np.vstack((Matriz_A, Matriz_B))
print("Nueva Matriz")
print(resultado)
print("\n")
print("Shape de la nueva Matriz")
print(resultado.shape)
print("\n")

#Stack crea un nuevo eje

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 7 — Pensamiento estructural

array_base=np.arange(1,5).reshape(2,2)
print("Array Base")
print(array_base)
print("\n")

#Nueva dimensión para trabajar de mejor forma los array 3D
F = np.stack((array_base, array_base))
print("Nuevo Array")
print(F)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 8 — Simulación de dataset

#Creación de array de datos
datos = np.array([10.5, 12.3, 9.8, 11.2, 10.9])

#Nuevas Observaciones
nuevas_observaciones = np.array([11.5, 12.1, 10.7])

#Se unen
datos_actualizados = np.concatenate((datos, nuevas_observaciones))
print("Datos Actualizados")
print(datos_actualizados)

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 9 — Detección de errores conceptuales

"""
Objetivo 1: Agregar variables
    np.column_stack()   # o np.concatenate(axis=1)

Por qué:
*   Las variables viven en las columnas.
*   Cada nueva variable se agrega como una columna adicional.
*   Mantiene la correspondencia correcta entre observaciones (filas).

Por qué no los otros:

np.append()
*   Aplana el array si no se especifica el parámetro axis.
*   Puede destruir la estructura bidimensional de los datos.

np.vstack()
*   Agrega filas, no columnas.
*   Se usa para agregar observaciones, no variables.

np.hstack()
*   Puede fallar si las dimensiones no son compatibles.
*   No distingue explícitamente entre variables y observaciones.
"""

"""
Objetivo 2: Agregar observaciones
    np.vstack()   # o np.concatenate(axis=0)

Por qué:
*   Las observaciones viven en las filas.
*   Cada nueva observación se agrega como una fila adicional.
*   Conserva la estructura tabular del array.

Por qué no los otros:

np.append()
*   Aplana el array si no se especifica el parámetro axis.
*   Puede perder la forma original del array.

np.column_stack()
*   Agrega columnas, no filas.
*   Se usa para agregar variables, no observaciones.

np.hstack()
*   Agrega columnas.
*   Mezcla observaciones como si fueran variables.
"""

"""
Objetivo 3: Crear un tensor
    np.array()

Por qué:
*   Un tensor es un array de más de dos dimensiones.
*   np.array() permite definir directamente la estructura n-dimensional.
*   Es la forma más clara y controlada de crear tensores.

Por qué no los otros:

np.vstack()
*   Combina arrays existentes.
*   No crea estructuras n-dimensionales desde cero.

np.hstack()
*   Solo concatena en una dimensión.
*   No permite definir tensores.

np.append()
*   Tiende a aplanar los datos.
*   Pierde la dimensionalidad del tensor.
"""

#------------------------------------------------------------------------------------------------------------------------------------------------

#Solución de Ejercicio 10 — Autodiagnóstico

"""
np.concatenate()

Qué hace:
*   Une arrays existentes a lo largo de un eje especificado (axis).
*   No crea nuevas dimensiones.

Cuándo usarla:
*   Cuando quieres control explícito del eje (filas o columnas).
*   Cuando trabajas con arrays ya compatibles en forma.

Qué error evita:
*   Evita unir arrays en el eje incorrecto.
*   Evita usar funciones más específicas sin entender el eje real.
"""

"""
np.vstack()

Qué hace:
*   Apila arrays verticalmente.
*   Agrega filas (observaciones).
*   Equivale a concatenate(axis=0).

Cuándo usarla:
*   Cuando quieres agregar nuevas observaciones.
*   Cuando los arrays tienen el mismo número de columnas.

Qué error evita:
*   Evita confundir filas con columnas.
*   Evita usar hstack por error conceptual.
"""

"""
np.hstack()

Qué hace:
*   Apila arrays horizontalmente.
*   Agrega columnas (variables).
*   Equivale a concatenate(axis=1) para arrays 2D.

Cuándo usarla:
*   Cuando quieres agregar variables.
*   Cuando los arrays tienen el mismo número de filas.

Qué error evita:
*   Evita usar vstack cuando en realidad necesitas columnas.
*   Evita escribir concatenate(axis=1) innecesariamente.
"""

"""
np.stack()

Qué hace:
*   Apila arrays creando una NUEVA dimensión.
*   Aumenta la dimensionalidad del array.

Cuándo usarla:
*   Cuando quieres crear un tensor.
*   Cuando necesitas conservar los arrays separados en una nueva dimensión.

Qué error evita:
*   Evita perder información al concatenar.
*   Evita usar concatenate cuando se necesita una dimensión extra.
"""

