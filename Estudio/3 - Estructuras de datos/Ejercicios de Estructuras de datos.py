"""
Ejercicio de Listas
"""

"""
Ejercicio 1:
1. Crea una lista con los nombres de 5 frutas y:
Muestra la primera y la última fruta.
Reemplaza la tercera fruta por otra.
Agrega una fruta al final.
Cuenta cuántas veces aparece una fruta específica.
"""

#Lista de las frutas
lista = ["Manzana", "Durazno", "Pera", "Mango", "Maracuya"]
print(lista)

#Mostrar primera fruta
print(lista[0])

#Mostrar última fruta
print(lista[-1])

#Agregar una fruta al final
lista.append("Banano")
print(lista)

#Cuantas veces aparece una fruta en Especifico. Se agregara una fruta adrede para demostrar el ejemplo
lista.append("Manzana")
print(lista.count( "Manzana"))

"""
Ejercicio 2:
2. Dada la lista [5, 8, 2, 9, 1]:
Ordénala en orden ascendente.
Encuentra el número más grande y el más pequeño sin usar min() ni max() (haz tu propio algoritmo con un for).
"""

lista=[5, 8, 2, 9, 1]
print(lista)

#Ordenar de forma ascenden
lista.sort()
print(lista)

#Encontrar número más grande y más pequeño
Valor_Minimo=lista[0]
Valor_maximo=lista[0]

for i in lista:
    if i < Valor_Minimo:
        Valor_Minimo = i
else:
    if i > Valor_maximo:
        Valor_maximo=i

#Sacar print fuera del bucle, de lo contrario, tendremos print innecesarios
#Valor más pequeño
print('Valor Minimo:', Valor_Minimo)

#Valor Más grande
print('Valor Máximo:', Valor_maximo)

"""
Ejercicio 3:
3. Pide al usuario que escriba 5 números, guárdalos en una lista y luego:
Calcula la suma total.
Calcula el promedio.
Imprime los números mayores que el promedio.
"""

#Se crea la lista vacia
lista=[]

for i in range(5):
    Elementos_lista=float(input(f'Agrega un elemento (Deben ser númericos): '))
    lista.append(Elementos_lista)

print(lista)

#Suma de la lista
suma_lista=sum(lista)
print(suma_lista)

#Promedio de la lista
promedio_lista=suma_lista/len(lista)
print(promedio_lista)

#Número mayor que el promedio
for x in lista:
    if x > promedio_lista:
        break
    else:
        break

#Print por fuera para que no se repita el bucle dentro del for
print(f'El número {x} es mayor que el promedio de la lista')
print(f'El número {x} NO es mayor al promedio de la lista')


"""
Ejercicios con Tuplas
"""

"""
Ejercicio 1:
1. Crea una tupla con los días de la semana.
Muestra el tercer día.
Verifica si "Domingo" está en la tupla.
Convierte la tupla a lista, agrega un nuevo día inventado y vuelve a convertirlo a tupla.
"""

#Creación de tupla
tupla = ("Lunes", "Martes", "Miercoles", "Jueves","Viernes","Sábado", "Domingo")
print(tupla)

#Mostrar el tercer día
print(tupla[2])

#Verificamos si "Domingo" esta en la tupla.
if "Domingo" in tupla:
    print (f'Domingo se encuentra en la tupla')
else:
    print (f'Domingono se encuentra en la tupla')

"""
Ejercicio 2:
2. Dada la tupla (10, 20, 30, 40, 50):
Recorre la tupla e imprime solo los números mayores que 25.
Calcula la suma de todos sus elementos.
"""

tupla = (10, 20, 30, 40, 50)
print(tupla)

#Imprimir números(s) mayor(res) que 25

print("Números mayores que 25:")
for x in tupla:
    if x > 25:
        print(x)
    else:
        print("No hay número mayor a 25")

#Calcular la suma de todos los elementos
suma_lista=sum(tupla)
print(f'La suma de todos los elementos da como resultado: ', suma_lista)

"""
Ejercicios con Conjuntos (set)
"""

"""
Ejercicio 1:
1. Crea un conjunto con los números del 1 al 5 y otro con los números del 4 al 8:
Imprime la unión.
Imprime la intersección.
Imprime la diferencia del primer conjunto menos el segundo.
"""

#Creación de los dos conjuntos
Conjunto_1 = set([1,2,3,4,5])
print(Conjunto_1)
Conjunto_2 = set([4,5,6,7,8])
print(Conjunto_2)

#Imprimir unión
print(Conjunto_1.union(Conjunto_2))

#Imprimir la intersección
print(Conjunto_1.intersection(Conjunto_2))

"""
Ejercicio 2:
2. Crea un conjunto con nombres de animales.
Agrega un nuevo animal.
Elimina uno existente.
Verifica si "Perro" está en el conjunto.
"""

#Crear conjunto de animales
conjunto_animales = set(["Pato", "Gallo", "Pollo","Vaca","Perro"])
print(conjunto_animales)

#Agregar un animal
conjunto_animales.add("Tucan")
print(conjunto_animales)

#Eliminar animal existente
conjunto_animales.pop()
print(conjunto_animales)

#Verificar si "Perro" esta en el conjunto
if "Perro" in conjunto_animales:
    print("Se encontró Perro en el conjunto")
else:
    print("No hay perro")

"""
Ejercicio 3:
3. Escribe un programa que elimine los elementos repetidos de la lista [1,2,2,3,4,4,5,6,6,7] usando un set.
"""

lista_eliminar = [1,2,2,3,4,4,5,6,6,7]
print(lista_eliminar)

#Programa para eliminar
conjunto_eliminar=set(lista_eliminar)
print(conjunto_eliminar)

"""
Ejercicios con Diccionarios
"""

"""
Ejercicio 1:
1. Crea un diccionario con información de una persona: nombre, edad y ciudad.
Muestra el nombre.
Cambia la ciudad.
Agrega una nueva clave llamada "profesión".
"""

#Creación dle Diccionario
diccionario={ "Nombre":"Valentina", "Edad":22, "Ciudad":"Montería"}
print(diccionario)

#Mostrar nombre
print(diccionario['Nombre'])

#Cambiar la ciudad
diccionario["Ciudad"]="Bogotá"
print(diccionario)

#Nueva clave: Profesion
diccionario["Profesion"]="Analista de Datos"
print(diccionario)

"""
Ejercicio 2:
2. Dado el diccionario: precios = {"pan": 500, "leche": 3000, "huevos": 12000}
Imprime solo las claves.
Imprime solo los valores.
Recorre el diccionario e imprime clave y valor.
"""

#Creación del diccionario
precios = {"pan": 500, "leche": 3000, "huevos": 12000}

#Imprimir solo claves

for x in precios:
    print(x)

#Imprime solo los valores
for x in precios:
    print(precios[x])

#Recorre el diccionario e imprime clave y valor.
for x,t in precio.items():
    print(x,t)

"""
Ejercicio 3:
3. Escribe un programa que pida al usuario 3 nombres de estudiantes y sus notas, guárdalos en un diccionario y luego:
Imprime todas las notas.
Calcula el promedio.
Encuentra el estudiante con la nota más alta.
"""

colegio={}

for x in range(3):
    nombre=input("Introduce tu nombre: ")
    nota=float(input("Introduce tu nota: "))
    colegio[nombre] = nota

print("Diccionario creado:")
print(colegio)

#Imprimir Notas
for x in colegio:
    print(colegio[x])

"""
Promedio
"""
#Sacamos los valores para guardarlos en una variable
valores=colegio.values()

#Sumamos
suma_total=sum(valores)

#Cantidad de valores
cantidad=len(valores)

#Calculamos el promedio
promedio = suma_total/cantidad
print(f"El promedio de los valores del diccionario es: {promedio}")

#Encontrar estudiante con la nota más alta
nota_alta =max(colegio.values())
print(f'La nota más alta es: {nota_alta} ')