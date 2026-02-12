import random

contador = 1
datos = []

while contador <= 100:
    datos.append(contador)
    contador += 1

numero = random.choice(datos)
#print(numero) 

while True:
    print(" Elige un número del 1 al 100:")
    numero_random=int(input(""))

    if numero_random!=numero:
        print("Número equivocado, sigue intentando")
    else:
        print("¡Diste en el clavo")
        break
