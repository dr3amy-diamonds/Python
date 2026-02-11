"""
Ejercicio 1: Suma de una lista de números

1. Escribe una función recursiva que sume todos los elementos de una lista de números.
"""

def lista_numero(numeros):
    suma_total = sum(numeros)
    print(f'La suma total es: ', +suma_total)

lista_numero(numeros=[1, 2, 3, 4, 5])

"""
Ejercicio 2: Invertir una cadena de texto
2. Crea una función recursiva que invierta una cadena de texto. Por ejemplo, si la entrada es "hola", la salida debe ser "aloh".
"""

def reverso_texto(texto):
    texto_invertida = texto[::-1]
    print(texto_invertida)

reverso_texto("Hola")

"""
Ejercicio 3: Potencia de un número

3. Escribe una función recursiva para calcular la potencia de un número (baseexponente).
"""

def potencia(base,exponente):
    potencia_total=base**exponente
    print(potencia_total)

potencia(2,2)

"""
Ejercicio 4: Búsqueda binaria (opcional, un poco más avanzado)

La búsqueda binaria es un algoritmo que encuentra la posición de un valor en una lista ordenada. Este es un excelente ejemplo para ver cómo la recursividad puede dividir un problema grande en problemas más pequeños.
"""
def busqueda_binaria(lista, objetivo):
    if not lista:
        return False  # Caso base: lista vacía

    medio = len(lista) // 2

    if lista[medio] == objetivo:
        return True
    elif objetivo < lista[medio]:
        return busqueda_binaria(lista[:medio], objetivo)
    else:
        return busqueda_binaria(lista[medio+1:], objetivo)

# Prueba
numeros = [2, 4, 6, 8, 10, 12, 14]
print(busqueda_binaria(numeros, 10))  
print(busqueda_binaria(numeros, 5))

"""
Ejercicio 5: Sumar los dígitos de un número

5. Escribe una función recursiva que sume los dígitos de un número entero. Por ejemplo, sumar_digitos(123) debería devolver 1 + 2 + 3, que es 6.
"""

def suma_digitos(numero):
    if numero==0:
        return 0
    else:
        suma_digitos = sum(map(int, str(numero)))
        print(f"La suma de los dígitos es: {suma_digitos}")

suma_digitos(123456)

