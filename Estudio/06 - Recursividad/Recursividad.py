"""
Recursividad

Es una técnica de programación donde una función se llama a sí misma para resolver un problema, dividiéndolo en subproblemas más pequeños hasta llegar a un caso base (condición de parada)
"""

"""
ADVERTENCIA
La recursividad a menudo se usa para problemas que pueden dividirse en subproblemas más pequeños que son similares al problema original. Sin embargo, puede ser menos eficiente que las soluciones iterativas (usando bucles como for o while) debido al consumo de memoria y tiempo que conlleva el manejo de múltiples llamadas a la función.
"""


#Ejemplo
def cuenta_atras(numero):
    if numero >=0:
        print(numero)
        cuenta_atras(numero-1)

cuenta_atras(100)