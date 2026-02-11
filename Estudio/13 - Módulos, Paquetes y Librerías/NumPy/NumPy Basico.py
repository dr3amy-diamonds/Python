import random
import numpy as num


#Crar lista con números aletarios, por eso se importa la librería random
numeros_random=10

lista=random.sample(range(1,100),numeros_random)

print(lista)

#Calcular la suma usando la librería Numpy
suma_total=num.sum(lista)
print(f'La suma de la lista es: ', suma_total)

#Calcular el número máximo en la lista
numero_maximo=num.max(lista)
print(f'El número máximo de lalista es: ', numero_maximo)

#Calcular el promedio usando la libreria Numpy
promedio_lista=num.mean(lista)
print(f'El promedio de la lista es: ',promedio_lista)