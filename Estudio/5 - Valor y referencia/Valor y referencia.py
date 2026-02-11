"""
Valor y referencia
En Python, el paso de parámetros funciona de manera diferente a otros lenguajes. No es exactamente "paso por valor" ni "paso por referencia", sino "paso por asignación de objeto".
"""

"""
Ejemplo de paso por valor

Como ya sabemos los números se pasan por valor y crean una copia dentro de la función, por eso no les afecta externamente lo que hagamos con ellos:
"""

#Ejemplo
x = 10
def funcion(entrada):
    entrada = 0
funcion(x)

print(x)

"""
Ejemplo de paso por referencia

Sin embargo las listas u otras colecciones, al ser tipos compuestos se pasan por referencia, y si las modificamos dentro de la función estaremos modificándolas también fuera:
"""

#Ejemplo
x = [10, 20, 30]
def funcion(entrada):
    entrada.append(40)

funcion(x)
print(x)

"""
El ejemplo anterior nos podría llevar a pensar que si en vez de añadir un elemento a x, hacemos x=[], estaríamos destruyendo la lista original. Sin embargo esto no es cierto.
"""

x = [10, 20, 30]
def funcion(entrada):
    entrada = []

funcion(x)
print(x)



"""
Ejemplo con tipos mutables (como una lista):
"""

def modificar_lista(mi_lista):
    mi_lista.append(4) # Modifica el objeto lista original
    print("Dentro de la función:", mi_lista)

numeros = [1, 2, 3]
modificar_lista(numeros)
print("Fuera de la función:", numeros)


"""
Ejemplo con tipos inmutables (como un entero):
"""

def intentar_modificar_numero(mi_numero):
    mi_numero = mi_numero + 1 # Crea un nuevo objeto entero
    print("Dentro de la función:", mi_numero)

contador = 5
intentar_modificar_numero(contador)
print("Fuera de la función:", contador)



"""
Para más información visitar la pagina con su link: https://ellibrodepython.com/paso-por-valor-y-referencia
"""