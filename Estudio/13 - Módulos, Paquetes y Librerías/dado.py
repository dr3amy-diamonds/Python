import random

#Diccionario de lanzamientos y contadores
contador = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

n_lanzamiento=6
#Lanzamientos y contador
for _ in range(n_lanzamiento):
    numero = random.randint(1, 6)
    print(numero)
    contador[numero] += 1

#Resultado final
print("Número de apariciones de cada cara del dado:")
for numero, veces in contador.items():
    print(f"Número {numero}: {veces} veces")