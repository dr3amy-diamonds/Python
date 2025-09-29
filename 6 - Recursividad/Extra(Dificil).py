"""
DIFICULTAD EXTRA (opcional):
    Utiliza el concepto de recursividad para:
        Calcular el factorial de un número concreto (la función recibe ese número).
        Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci (la función recibe la posición).
"""

#Calcular Factorial
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

print(factorial(4)) 

#Calcular serie Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6)) 