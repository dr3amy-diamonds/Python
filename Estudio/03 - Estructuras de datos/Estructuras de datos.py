"""
Listas (arrays, arreglos o vectores)
"""

"""
Creación de una lista
"""
#Lista vacia

lista=[]

# Lista con valores del mismo tipo
lista = [1, 2, 3, 4, 5]

#Lista con tipos de valores mixtos
lista =[1,2.1,-3,"Valentina","Ojeda"]
print(lista)

#Acceder mediante el index
print(lista[3])

#Cambiar/reemplazar elemento
lista[2]="Debussy"
print(lista)

#Dara error ya que las lista toman el primer valor como 0
#print(lista[5])

#Va es número de posiciones hacia atrás
print(lista[-2])

#Agregar un elemento al final
lista.append("Hola")
lista.append("Valentina")
print(lista)

#Nos devuelve el número de veces que un valor se repite
print(lista.count( "Valentina"))

"""
El método index() en las listas de Python sirve para encontrar la posición (el índice) de la primera ocurrencia de un elemento específico dentro de la lista. Si el elemento se encuentra, el método devuelve su índice numérico; de lo contrario, genera un error ValueError. Este método es útil para buscar la ubicación exacta de un elemento
"""
print(lista.index("Ojeda"))

"""
El método remove() en Python se usa para eliminar la primera ocurrencia de un elemento específico de una lista, utilizando el valor del elemento como argumento, en lugar de su posición. Si el elemento no existe en la lista, se genera un error ValueError.
"""
lista.remove(1)
print(lista)

#Ordenarlo de forma ascendente
lista2=[9, 12, 7, 4, 11]
lista2.sort() #Tiene que ser de caracter númerico, de lo contrario dará error
print(lista2)

#Invertir elementos de una lista
lista3=["Bang Bang","Go Go Go", True, False, 2.1, 3.14, -9, 5]
lista3.reverse()
print(lista3)

"""
Crear algoritmos
A veces queremos realizar acciones que no estén incorporadas a Python.
Entonces podemos crear nuestros propios algoritmos.
Por ejemplo, un algoritmo se puede utilizar para encontrar el valor más bajo de una lista, como en el ejemplo de abajo:
"""
mi_lista = [10,12,14,15,16,2,58,75,65]
Valor_Minimo=mi_lista[0]

for i in mi_lista:
    if i < Valor_Minimo:
        Valor_Minimo = i
print('Valor Minimo:', Valor_Minimo) 


"""
Tuplas
as tuplas en Python son un tipo o estructura de datos que permite almacenar datos de una manera muy parecida a las listas, con la salvedad de que son inmutables (No sé ´pueden cambiar).

Las tuplas en Python o tuples son muy similares a las listas, pero con dos diferencias. Son inmutables, lo que significa que no pueden ser modificadas una vez declaradas, y en vez de inicializarse con corchetes se hace con (). Dependiendo de lo que queramos hacer, las tuplas pueden ser más rápidas.
"""

# Crear tupla Python
tupla = (1, 2, 3, True, False, False, "Mentiras", "Tuyas", 3.14,-9)
print(tupla)

#También pueden declararse sin (), separando por , todos sus elementos.
tupla = 1, 2, 3, True, False, False, "Mentiras", "Tuyas", 3.14,-9
print(tupla) 

#Como hemos comentado, las tuplas son tipos inmutables, lo que significa que una vez asignado su valor, no puede ser modificado. Si se intenta, tendremos un TypeError.
tupla = (1, 2, 3, True, False, False, "Mentiras", "Tuyas", 3.14,-9)
print(tupla)
#tupla[3] = 5 # Error! TypeError

#Para que lo interprete como una tupla
print(1,2,)

#Tupla de un solo elemento
tupla=("Apple Pie",)
print("tupla")

#Esto no es una tupla
tupla=("Apple Pie")
print("tupla")

#Acepta valores duplicados
tupla=("Pie", "De", "Manzana","Manzana")
print(tupla)

#conversion de lista a tupla
lista = [1, 2, 3]
tupla = tuple(lista)
print(tupla)

#Iteración de una tupla
tupla = [1, 2, 3]
for t in tupla:
    print(t) 

"""
Conjuntos
Nota: Se pueden usar llaves pero tambien se usan condicionales, entonces se usará se usará set para evitar confusiones

Los set en Python son un tipo que permite almacenar varios elementos y acceder a ellos de una forma muy similar a las listas pero con ciertas diferencias:

    *Los elementos de un set son único, lo que significa que no puede haber elementos duplicados.

    *Los set son desordenados, lo que significa que no mantienen el orden de cuando son declarados.

    *Sus elementos deben ser inmutables.
"""

#Crear Set
#Conjunto Vacio
set()
#lista
print(set([1,2,3,5,5,65,1.1]))
#tupla
print(set((2,5,7.9,6)))
#String (Conjunto Char)
print(set("0.104"))

#Uno de sus usos es eliminar elementos repetidos de la secuencia
conjunto=set([1,2,3,3,2,4])
print (conjunto)
#Añadir un elemento
conjunto.add ("Hola")
print (conjunto)

#Eliminar un elemento
conjunto.remove("Hola")
print(conjunto)

#Elimina un elemento aleatorio
conjunto=set([1,2,3])
print(conjunto)
conjunto.pop()
print(conjunto)

#Elimina todos los elementos
conjunto=set([1,2,3])
conjunto.clear()
print(conjunto)

#Creación de varios conjuntos
conjunto_2= set(["Hola", "Valentina",1])
conjunto_3= set (["Como", "Estas",1])
#Visualizar los  conjuntos
print(conjunto, conjunto_2,conjunto_3)
#Intersección
print(conjunto.intersection(conjunto_3))

#Union de Elementos
print(conjunto.union(conjunto_2))
print(conjunto.union(conjunto_3))

"""
El issubset()método retorna True si está establecido A es el subconjunto de B, es decir, si todos los elementos del conjunto A están presentes en el conjunto B. De lo contrario, devuelve False.
"""
print(conjunto_2.issubset(conjunto))
print(conjunto_3.issubset(conjunto))

"""
Diccionario

Los diccionarios en Python son una estructura de datos que permite almacenar su contenido en forma de llave y valor.

Un diccionario en Python es una colección de elementos, donde cada uno tiene una llave key y un valor value. Los diccionarios se pueden crear con paréntesis {} separando con una coma cada par key: value.
"""

"""
LA KEY NO DEBE REPETIRSE. En caso que se repita, toma el valor de la última repetición
"""
#Crear diccionario. Método Uno
diccionario = {1: "uno", 2:"Dos"}
diccionario [3] = "Tres"

#Crear diccionario. Método Dos
"""
Otra forma equivalente de crear un diccionario en Python es usando dict() e introduciendo los pares key: value entre paréntesis. Se usa una lista de tuplas
"""
diccionario = dict([(1, 'Uno'), (2, 'Dos')])
print(diccionario)

#Lista tipo tuplas
dict_lista_tupas=dict([(1, "Uno"), (2,"Dos"),(3,"Tres")])
print(dict_lista_tupas)

#Lista tipo String
dict_lista_string =dict(Uno=1, Dos=2, Tres=3)
print(dict_lista_string)

#Lista con sus tipo de datos
dict_tipos={1:"Integer",2.2: "Float", "Texto":"String", (1,2):"Tupla"}
print(dict_tipos)

#Lista con Key repetida
dict_repetido={1:"Primero", 1:"Último"}
print(dict_repetido)

#Varios métodos     
#.key(): Devuelve una lista con las claves
#.values(): Devuelve una lista con los valores
#.items(): Devuelve una lista de tuplas con los pares datos kay-value
print(diccionario, diccionario.keys(),diccionario.values(),diccionario.items())

#Acceder a sus elemetos
print(diccionario[1])
print(diccionario.get(1))

#Modificar un elemento
diccionario[1]="Unos"
print(diccionario)

#Eliminar todo el contenido del diccionario
diccionario_prueba={"Nombre":"Valentina", "Edad": 22}
print(diccionario_prueba)
diccionario_prueba.clear()
print(diccionario_prueba)

#Eliminar de manera aleatoria
diccionario_prueba2={"Nombre":"Juan Diego", "Edad": 20}
print(diccionario_prueba2)
diccionario_prueba2.popitem()
print(diccionario_prueba2)

"""
El método update() se llama sobre un diccionario y tiene como entrada otro diccionario. Los value son actualizados y si alguna key del nuevo diccionario no esta, es añadida.
"""

diccionario_uno= {'a': 1, 'b': 2}
diccionario_dos={'a': 0, 'd': 400}
diccionario_uno.update(diccionario_dos)
print(diccionario_uno)

#Si el key al que accedemos no existe, se añade automáticamente.
diccionario[3]="Tres"
print(diccionario)

#Iterar diccionario
# Imprime los key del diccionario
for x in diccionario:
    print(x)

#Imprimir los values del diccionario
for x in diccionario:
    print(diccionario[x])

#imprimir el key y el value a la vez.
for x,t in diccionario.items():
    print(x,t)