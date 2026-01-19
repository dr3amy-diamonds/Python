import numpy as np

#Búsqueda lógica(Máscara Booleana)
# Buscar valores mayores a 50

datos=np.array([10, 45, 60, 80, 30])

condicion = datos > 50
print("Condición")
print(condicion)
print("\n")

"""
Qué pasa aquí

*   NumPy evalúa todos los valores a la vez

*   Devuelve un array booleano
"""

#Ahora usamos la máscara
filtrados= datos[condicion]
print("Filtracion")
print(filtrados)
print("\n")

"""
✔ Sin bucles
✔ Muy rápido
✔ Muy legible
"""

# np.where() --- búsqueda condicional
#Encontrar índices donde el valor es mayor a 50

indices = np.where(datos>50)
print("Índices")
print(indices)
print("\n")

#Ahora obtenemos los valores
print("Valores")
print(datos[indices])
print("\n")

"""
✔ where devuelve posiciones
✔ Útil para análisis estructural
"""

#argmax() y argmin()
#Posición del valor máximo y mínimo

valores=np.array([20, 90, 40, 70])

pos_max=np.argmax(valores)
pos_min=np.argmin(valores)

print("Posición Máxima, Valor Máximo")
print(pos_max, valores[pos_max])
print("\n")
print("Posición Minima, Valor Minimo")
print(pos_min, valores[pos_min])
print("\n")

"""
Clave

*   argmax NO devuelve el valor

*   Devuelve la posición
"""

#nonzero() -- posiciones verdaderas

datos_2= np.array([0, 5, 0, 3, 7])

print("Posiciones verdaderas")
indices=np.nonzero(datos_2)
print(indices)
print("\n")

"""
✔ Ignora ceros
✔ Útil para datos binarios
"""

#isin() -- pertenencia
# Ver qué valores estan en el conjunto permitido

datos_3=np.arange(1,6)
permitidos=[2, 4]

mask = np.isin(datos_3, permitidos)
print("Valores Booleanos")
print(mask)
print("\n")
print("Valores")
print(datos_3[mask])
print("\n")

"""
✔ Muy útil para filtros categóricos
"""

#Ordenación

#np.sort() -- Ordenar valores

valores_2 = np.array([40, 10 , 30, 20])

ordenador= np.sort(valores_2)
print("Valores Ordenados")
print(valores_2)
print("\n")

#sort devuelve una copia

#argsort() -- ordenar por índices

#Mantener relación entre arrays

nombres = np.array(["Ana",  "Luis", "Pedro"])
edades=np.array([30, 20, 25])

orden=np.argsort(edades)

print("Ordenado por edad")
print(nombres[orden])
print(edades[orden])
print("\n")

"""
✔ Relación preservada
✔ Herramienta profesional clave
"""

#Ordenación por eje(axis)
matriz = np.array([
    [3, 1, 2],
    [6, 5, 4]
])

print("Ordenar por filas")
print(np.sort(matriz, axis=1))
print("Ordenar por columna")
print(np.sort(matriz, axis=0))
print("\n")

"""
Recuerda:

*   axis=1 → cada fila

*   axis=0 → cada columna
"""

#Métodos de Ordenación
arr = np.array([5, 1, 4, 2, 3])

print("Ordenado Rápido")
print(np.sort(arr, kind="quicksort"))
print("Ordenado Estable")
print(np.sort(arr, kind="mergesort")) 
print("Ordenado Intermedio")
print(np.sort(arr, kind="heapsort"))
print("\n")

"""
✔ En análisis: quicksort es suficiente
✔ Usa mergesort si el orden previo importa
"""

#Ordenación parcial(Más eficiente)
#Top 3 Mayores

datos_4 = np.array([10, 80, 30, 50, 90, 40])

top3 = np.partition(datos_4, -3)[-3:]
print("Top 3")
print(top3)
print("\n")

"""
*   No ordena todo
*    Mucho más rápido para grandes datasets
"""

"""
Errores comunes (ejemplos reales)

*   Usar for para buscar:

# MALA PRÁCTICA
resultado = []
for x in datos:
    if x > 50:
        resultado.append(x)


✔ Mejor:

datos[datos > 50]

"""

"""
Resumen Final

| Necesidad         | Método             |
| ----------------- | ------------------ |
| Filtrar           | máscaras booleanas |
| Buscar índices    | `where`, `nonzero` |
| Máx / mín         | `argmax`, `argmin` |
| Cruzar datos      | `isin`             |
| Ordenar           | `sort`             |
| Mantener relación | `argsort`          |
| Optimizar         | `partition`        |

"""