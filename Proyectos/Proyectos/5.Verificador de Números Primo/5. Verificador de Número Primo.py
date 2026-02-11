import math

def es_primo(numero):
    if numero <= 1:
        return False #No es primo
    if numero == 2:
        return True #Es primo
    if numero % 2 == 0:
        return False #No es primo

    
    for i in range(3, int(math.sqrt(numero)) + 1, 2):
        if numero % i == 0:
            return False 
    return True 


num = int(input("Introduce un número: "))
if es_primo(num):
    print(f"{num} es un número primo.")
else:
    print(f"{num} no es un número primo.")