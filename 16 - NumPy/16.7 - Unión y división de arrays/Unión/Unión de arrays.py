import numpy as np


# Unión base: np.concatenate()
# Unión correcta por filas (axis=0)

Matriz_A= np.arange(1, 7).reshape(2, 3)
print("Matriz A")
print(Matriz_A)
print("\n")

Matriz_B= np.arange(7, 13).reshape(2, 3)
print("Matriz B")
print(Matriz_B)
print("\n")

resultado=np.concatenate((Matriz_A,Matriz_B), axis=0)
print("Resultado de la concatenación ")
print(resultado)
print("\n")
print(resultado.shape)
print("\n")

"""
Qué pasa:

*   se eliminan las filas (axis=0)

*   se apilan filas

*   columnas deben coincidir
"""


# Error Común: Columnas Incompatibles

#Se implemente un try/Except para no perjudicar la ejecución del código
Matriz_C= np.arange(1,5).reshape(2,2)
print("Matriz C")
print(Matriz_C)
print("\n")
try:
    np.concatenate((A, C), axis=0)
except:
    print("ValueError: all the input array dimensions except for the concatenation axis must match exactly\n")
"""
Lección:
*   Al unir por filas, las columnas deben ser iguales
"""

#Unión por columnas (axis=1)

Matriz_D= np.arange(7,11).reshape(2,2)
print("Matriz D" )
print(Matriz_D)
print("\n")

resultado = np.concatenate((Matriz_A,Matriz_D ), axis=1)
print(resultado)
print("\n")
print(resultado.shape)

"""
Qué pasa:

*   se eliminan columnas (axis=1)

*   se apilan columnas

*   filas deben coincidir
"""

#Error Común: Filas incompatibles

Matriz_E=np.arange(1,7).reshape(3,2)
print("Matriz E")
print(Matriz_E)
print("\n")

try:
    np.concatenate((A, E), axis=1)
except:
    print("ValueError: all the input array dimensions except for the concatenation axis must match exactly\n")

"""
Lección:
*   Al unir por columnas, las filas deben ser iguales
"""

#vstack() — unión por filas (más claro)

resultado = np.vstack((Matriz_A, Matriz_B))
print(resultado)
print("\n")

"""
✔ Más legible
✔ Menos errores
✔ Recomendado para observaciones
"""

#Error: shapes incompatibles
try:
    np.vstack((Matriz_A, Matriz_D))
except:
    print("All the input array dimensions except for the concatenation axis must match exactly, but along dimension 1, the array at index 0 has size 3 and the array at index 1 has size 2")

"""
Error lógico:

*   columnas distintas
"""

#hstack() — unión por columnas
resultado = np.hstack((Matriz_A, Matriz_D))
print(resultado)

#Ideal para agregar variables

"""
Error Conceptual común

np.hstack((Matriz_A, Matriz_B))

No funciona porque:

*   columnas iguales

*   pero filas se duplicarían incorrectamente

Lección:

*   hstack ≠ “juntar cualquier cosa”

"""

#stack() — NUEVA dimensión (NO unión)

resultado = np.stack((Matriz_A, Matriz_A), axis=0)
print(resultado)
print(resultado.shape)

"""
Qué pasa:

*   no se mezclan datos

*   se crea un eje nuevo

*   estructura más profunda
"""

"""
ERROR muy común

“Uso stack para unir arrays”

* Conceptualmente incorrecto
✔ stack empaqueta, no une
"""


#Verificar shape (BUENA PRÁCTICA)
print("Matriz A:", Matriz_A.shape)
print("Matriz B:", Matriz_B.shape)

#Nunca unas arrays sin mirar shape

"""
ERRORES CLAVE QUE YA NO DEBES COMETER

*   Confundir axis con orientación
*   No revisar shape
*   Usar stack cuando quieres unir
*   Forzar concatenaciones
*   Asumir que NumPy “arregla” shapes
"""

"""
| Objetivo              | Función                          |
| --------------------- | -------------------------------- |
| Agregar filas         | `vstack` / `concatenate(axis=0)` |
| Agregar columnas      | `hstack` / `concatenate(axis=1)` |
| Crear nueva dimensión | `stack`                          |
| Control total         | `concatenate`                    |

"""