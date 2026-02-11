"""
Nivel 1: Básicos
"""

"""
Ejercicio 1
1. Declara una cadena con tu nombre y muéstrala en pantalla.
"""
#Declarar cadena
cadena="Layla"

#Mostrar
print(cadena)

"""
Ejercicio 2:
2. Crea una cadena con comillas dobles (") dentro usando secuencias de escape.
"""

#Crear Cadena
cadena = "Hola \"Mundo\""
print(cadena)

"""
Ejercicio 3:
3. Declara una cadena vacía y verifica con print(len(cadena)) cuántos caracteres tiene.
"""

#Crear cadena vacia
cadena=""
print(len(cadena)) #La saida será igual a 0

"""
Ejercicio 4:
4. Concatena dos cadenas: "Hola" y "Mundo", y muéstralo como "Hola Mundo".
"""

#Crear dos cadena
cadena="Hola"
cadena_2 ="Mundo"

#Imprimir cadena concatenada
print(cadena + " " +cadena_2)

"""
Ejercicio 5:
5. Repite la palabra "Python " 5 veces en una sola línea usando *.
"""

#Crear cadena
cadena="Python"

print(cadena*5)

#####################################################################################################################

"""
Nivel 2: Operaciones
"""

"""
Ejercicio 1:
1. Comprueba si la palabra "perro" está dentro de la cadena "El gato duerme en el sillón".
"""

#Comprobar
print("Perro" in "El gato duerme en el sillón")

#Donde sí esta el perro
print("Perro" in "El Perro duerme en el sillón") #Se tiene que tener precausión con las mayusculas porque es muy quisquilloso con estas y no puede tomarla

"""
Ejercicio 2:
2. Convierte el número 123.45 a string y muéstralo junto con un mensaje: "El número es: 123.45".
"""

#Crear variable del número

x=float(123.45)

#Conversión
cadena="El número es: " + str(x)
print(cadena)


"""
Ejercicio 3:
3. Declara la cadena "Programación" y muestra solo:

La primera letra

La última letra

Los primeros 5 caracteres
"""

#Crear cadena
cadena="Programación"

#Primera letra
print(cadena[0])

#Ultima letra
print(cadena[-1])

#Primeros 5 caracteres
print(cadena[0],cadena[1],cadena[2],cadena[3],cadena[4])

"""
Ejercicio 4:
4. Itera con un for sobre la cadena "banana" e imprime cada letra en una línea.
"""

#Crear Iteración
for x in "Banana":
    print(x)

"""
Ejercicio 5:
5. Busca la posición de "a" en "manzana" usando .find().
"""

#Crear cadena
cadena="manzana"

#Buscar
print(cadena.find("a"))

#####################################################################################################################

"""
Nivel 4
"""

"""
Ejercicio 1:
1. Declara variables: nombre = "Laura" y edad = 20, y crea el saludo:
"Hola Laura, tienes 20 años" de 3 formas:

Usando concatenación (+)

Usando %

Usando f-strings
"""

#Declarar variables

nombre = "Laura"
edad = 20

#Crear saludo
saludo = "Hola, %s.  Tienes %d años." % (nombre, edad)
print(saludo)

"""
Ejercicio 2:
2. Haz un f-string que calcule directamente 5 * 7 dentro del texto, mostrándolo como: "El resultado es 35".
"""

def multiplicacion():
    producto = 5*7
    return producto

cadena = f"El resultado de la función es {multiplicacion()}"
print(cadena)

#######################################################################################################################
"""
Nivel 4: Métodos de cadenas
"""

"""
Ejercicio 1:
1. Convierte "mi nombre es ana" en: "Mi nombre es ana" usando .capitalize().
"""

#Declarar cadena
cadena = "Mi nombre es ana"
#Conversión
print(cadena.capitalize())

"""
Ejercicio 2:
2. Convierte "HOY ES LUNES" a minúsculas usando .lower()
"""

#Declarar cadena
cadena="HOY ES LUNES"
#Conversión
print(cadena.lower())

"""
Ejercicio 3:
3. Convierte "Python Es Genial" a mayúsculas usando .upper()
"""

#Declarar cadena
cadena="Python Es Genial"
#Conversión
print(cadena.upper())

"""
Ejercicio 4:
4. Invierte el caso de "hOlA MuNdO" usando .swapcase().
"""

#Declarar cadena
cadena="hOlA MuNdO"
#Conversión
print(cadena.swapcase())

"""
Ejercicio 5:
5. Cuenta cuántas veces aparece "o" en "tomorrow".
"""

#Crear cadena
cadena="tomorrow"
#Buscar
print(cadena.count("o"))

"""
Ejercicio 6:
6. Comprueba si "Python3" es alfanumérica usando .isalnum().
"""

#Crear cadena
cadena="Python3"
#Comprobar
print(cadena.isalnum())

"""
Ejercicio 7:
7. Comprueba si "Python" es alfabética usando .isalpha().
"""

#Crear cadena
cadena="Python"
#Comprobar
print(cadena.isalpha())

"""
Ejercicio 8:
8. Une la lista ["Me", "gusta", "Python"] en una sola cadena separada por guiones (-).
"""

lista = ["Me", "gusta", "Python"]
separador = "-"
resultado = separador.join(lista)  
print(resultado)

#######################################################################################################

"""
Nivel 5: Retadores
"""

"""
Ejercicio 1:
1. Dada la cadena "abracadabra", reemplaza todas las "a" por "x".
"""

# Crear cadena
cadena="abracadabra"
#Reemplazo
print(cadena.replace("a", "x"))

"""
Ejercicio 2:
2. Divide la cadena "uno,dos,tres,cuatro" en una lista usando .split(",").
"""
#Crear cadena
cadena = "uno,dos,tres,cuatro"
#Reemplazo
lista=cadena.split(",")
print(lista)

"""
Ejercicio 3:
3. Pide al usuario que escriba una frase y muestra cuántos caracteres tiene (usa len()).
"""

#Crear cadena
cadena=input("Digita una frase: ")

#Mostrar caracteres
print(len(cadena)) #Toma como caractere los espacios

"""
Ejercicio 4:
4. Pide al usuario una palabra y dile si contiene la letra "z"
"""
#Crear cadena
cadena=input("Digita una palabra ")

#Confirmar por letra
print ("z" in cadena)

"""
Ejercicio 5:
5. Escribe un programa que pida al usuario su nombre y edad, y devuelva:
"Hola <nombre>, en 10 años tendrás <edad+10> años."
"""

#Crear Función
def programa():
    #Crear variables
    nombre = input("Digita tu nombre por favor: ")
    edad = int(input("Digita tu edad por favor: "))
    edad_sumada=10+edad
    saludo = "Hola, %s.  Tienes %d años." % (nombre, edad_sumada)
    return saludo

print(programa())



