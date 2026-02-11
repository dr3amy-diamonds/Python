"""
Ejercicio 1: Inmutables (números)
1. ver que el número original no cambia afuera.
"""

#Ejemplo
def doblar(numero):
    numero = numero * 2
    print("Dentro de la función:", numero)

x = 7
doblar(x)
print("Fuera de la función:", x)

"""
Ejercicio 2: Mutables (listas)
2. ver que la lista sí se modificó afuera.
"""

#Ejemplo
def agregar_cuadrado(lista):
    lista.append(lista[-1] ** 2)
    print("Dentro de la función:", lista)

valores = [2, 3]
agregar_cuadrado(valores)
print("Fuera de la función:", valores) 

"""
Ejercicio 3: Reasignación en mutables
3. Comprobar que reasignar una lista no borra la original.
"""
#Ejemplo
def vaciar_lista(lista):
    lista = []   # reasignación local
    print("Dentro de la función:", lista)

datos = [1, 2, 3]
vaciar_lista(datos)
print("Fuera de la función:", datos)

"""
Ejercicio 4: Mutar y reasignar

4. Ver la diferencia entre mutar (afecta afuera) y reasignar (solo local). 
Qué cambio sí se refleja afuera?
¿Qué cambio solo existe dentro de la función?
"""

#Ejemplo
def modificar(lista):
    lista.append("nuevo")
    lista = ["otro", "elemento"]
    print("Dentro de la función:", lista)

x = [10]
modificar(x)
print("Fuera de la función:", x)

"""
Ejercicio 5: Strings (inmutables)
5. Entender que los strings son inmutables, igual que los números.
"""

#Ejemplo
def cambiar_texto(s):
    s = "nuevo texto"
    print("Dentro de la función:", s)

mensaje = "hola"
cambiar_texto(mensaje)
print("Fuera de la función:", mensaje)

"""
Ejercicio 6: Diccionarios (mutables)
6. Comprobar que los diccionarios, al ser mutables, se modifican afuera.
"""

#Ejemplo
def actualizar_diccionario(dic):
    dic["edad"] = 25
    print("Dentro de la función:", dic)

persona = {"nombre": "Ana"}
actualizar_diccionario(persona)
print("Fuera de la función:", persona)

"""
Ejercicio 7:
7. Crea una función que reciba un texto y dentro de la función lo convierta a mayúsculas.
Imprime el valor dentro de la función y luego el valor original fuera de la función.
"""
#Ejemplo
def texto(texto_en_mayusculas):
    texto_en_mayusculas = texto_en_mayusculas.upper()
    print("Dentro de la función:", texto_en_mayusculas)

s = "nuevo texto"
texto(s)
print("Fuera de la función:", s)

"""
Ejercicio 8:
8. Crea una función que reciba una lista y le agregue un elemento al final (puede ser el número 100).
Imprime la lista dentro de la función y luego afuera.
"""

#Ejemplo
def lista_nueva(lista_numero):
    lista_numero.append(100)
    print("Dentro de la función:", lista_numero)


valores = [2, 3]
lista_nueva(valores)
print("Fuera de la función:", valores) 

"""
Ejercicio 9:
9. Crea una función que reciba una tupla y dentro de la función le intente “agregar” un nuevo valor.
Imprime la tupla dentro de la función y luego afuera.
"""
#Ejemplo
def tupla(tupla_nueva):
    lista_temporal = list(tupla_nueva)   
    lista_temporal.append(4)            
    nueva_tupla = tuple(lista_temporal) 
    print("Dentro de la función:", nueva_tupla)

tupla_afuera = (1, 2, 3)
tupla(tupla_afuera)
print("Fuera de la función:", tupla_afuera)

