# ============================================
# 16.5 — COPIAS Y VISTAS EN NUMPY
# Ejemplos prácticos explicados
# ============================================

import numpy as np

# --------------------------------------------
# 1. Ejemplo base: array original
# --------------------------------------------
print("\n--- 1. ARRAY ORIGINAL ---")
original = np.array([10, 20, 30, 40, 50])
print("Original:", original)

# --------------------------------------------
# 2. VISTA usando slicing
# --------------------------------------------
print("\n--- 2. VISTA CON SLICING ---")
vista = original[1:4]   # slicing → vista
vista[0] = 999

print("Vista modificada:", vista)
print("Original después:", original)

# Nota:
# vista comparte memoria con original
# modificar la vista modifica el original

# --------------------------------------------
# 3. COPIA explícita con copy()
# --------------------------------------------
print("\n--- 3. COPIA CON copy() ---")
original = np.array([10, 20, 30, 40, 50])

copia = original[1:4].copy()
copia[0] = 777

print("Copia modificada:", copia)
print("Original intacto:", original)

# --------------------------------------------
# 4. reshape() → vista o copia
# --------------------------------------------
print("\n--- 4. reshape() ---")
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)

reshaped[0, 0] = 100

print("Reshape:")
print(reshaped)
print("Original:")
print(arr)

# reshape() suele devolver una vista
# modificar reshaped puede afectar al original

# --------------------------------------------
# 5. flatten() → COPIA
# --------------------------------------------
print("\n--- 5. flatten() ---")
matriz = np.array([[1, 2], [3, 4]])

flat = matriz.flatten()
flat[0] = 999

print("Flatten:", flat)
print("Matriz original:", matriz)

# flatten() crea una copia
# el original NO cambia

# --------------------------------------------
# 6. ravel() → VISTA
# --------------------------------------------
print("\n--- 6. ravel() ---")
matriz = np.array([[1, 2], [3, 4]])

rav = matriz.ravel()
rav[0] = 888

print("Ravel:", rav)
print("Matriz original:", matriz)

# ravel() devuelve una vista
# el original SÍ cambia

# --------------------------------------------
# 7. Transposición (.T) → VISTA
# --------------------------------------------
print("\n--- 7. TRANSPOSICIÓN (.T) ---")
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

transpuesta = matriz.T
transpuesta[0, 0] = 999

print("Transpuesta:")
print(transpuesta)
print("Matriz original:")
print(matriz)

# .T no copia datos
# comparte memoria con el original

# --------------------------------------------
# 8. Asignación simple en Python
# --------------------------------------------
print("\n--- 8. ASIGNACIÓN SIMPLE ---")
a = np.array([1, 2, 3])
b = a
b[0] = 100

print("a:", a)
print("b:", b)

# b = a NO crea una copia
# ambos apuntan al mismo array

# --------------------------------------------
# 9. Regla de oro
# --------------------------------------------
print("\n--- 9. REGLA DE ORO ---")
original = np.array([1, 2, 3, 4, 5])

seguro = original.copy()   # Si vas a modificar
rapido = original[1:4]     # Si solo vas a leer

print("Seguro (copia):", seguro)
print("Rápido (vista):", rapido)

# ============================================
# IDEAS CLAVE
# slicing    → vista
# copy()     → copia
# flatten()  → copia
# ravel()    → vista
# reshape()  → normalmente vista
# .T         → vista
# si dudas   → usa .copy()
# ============================================
