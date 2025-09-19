"""
Cadena de Caracteres

Las cadenas en Python o strings son un tipo inmutable que permite almacenar secuencias de caracteres. Para crear una, es necesario incluir el texto entre comillas dobles ". 
"""
cadena = "Esto es una cadena"
print(cadena)

#Valido tambien para declarar variables en comillas simples ''
cadena ='Esto tambien es una candena'
print(cadena)

#cadena vacía
cadena=''
print(cadena)

#Error de cadena de caracteres
#cadena = "Esto es una comilla doble " de ejemplo" # Error!

#Secuencias de escape "\"
cadena = "Esto es una comilla doble \" de ejemplo"
print(cadena)

#Salto de linea
cadena = "Esto es una comilla doble \n de ejemplo"
print(cadena)

#Concatenar cadena
x=5
cadena="El número es: " + str(x)
print(cadena)

"""
Otra forma de concatenar es usando % en diferentes formas. Una lista de sus usos:
%s: Para cadenas de caracteres
%d: Para enteros

Advertencia: in embargo, se considera un método desactualizado y no recomendado, siendo preferibles las f-strings o el método `format()` por su mayor legibilidad y funcionalidad
"""

#Ejemplo
nombre = "Juan" #Toma la cadena de caracteres
edad = 30 #Toma el número
saludo = "Hola, %s.  Tienes %d años." % (nombre, edad)
print(saludo)

"""
Alternativas
F-strings (Formatted String Literals): Introducidas en Python 3.6, son la forma recomendada para formatear cadenas, colocando las variables o expresiones entre llaves {} dentro de la cadena, precedida por la letra f.

Método format(): Otro método moderno que utiliza llaves {} como marcadores de posición y los reemplaza con los valores pasados como argumentos a la función format()
"""

#Ejemplo usando F-strings
nombre = "Ana"
edad = 25
saludo = f"Hola, {nombre}. Tienes {edad} años." # esto tambien es interpolación de Cadenas
print(saludo) 

#Puedes incluso hacer operaciones dentro de la creación del string.
a = 5 
b = 10
cadena = f"a + b = {a+b}"
print(cadena)

#Puedes incluso llamar a una función dentro.
def funcion():
    return 20
cadena = f"El resultado de la función es {funcion()}"
print(cadena)

#Ejemplo usando format()
nombre = "Carlos"
edad = 40
saludo = "Hola, {}. Tienes {} años.".format(nombre, edad)
print(saludo) 

"""
Ejemplos String:
1. Para entender mejor la clase string, vamos a ver unos ejemplos de como se comportan. Podemos sumar dos strings con el operador +.
"""
#Ejemplo
cadena_uno = "Parte 1"
cadena_Dos = "Parte 2"

print(cadena_uno + " " +cadena_Dos)

"""
2. Se puede multiplicar un string por un int. Su resultado es replicarlo tantas veces como el valor del entero.
"""
#Ejemplo 2
cadena= "Hola "
print(cadena * 3)

#Podemos ver si una cadena esta contenida en otra con in.
print("Donde" in "Donde está el policia")
print ("Chicos" in "Chicas Malas")

#Longitud de la cadena
print(len("Esta es mi cadena"))

#Converson de int a String
cadena_numerica = str(10.4)
print(cadena_numerica)

#También se pueden indexar las cadenas, como si de una lista se tratase.
abecedario = "abcde"
print(abecedario[0])  
print(abecedario[-1]) 

"""
Las cadenas son matrices

Como muchos otros lenguajes de programación populares, las cadenas en Python son matrices de caracteres Unicode.
Sin embargo, Python no tiene un tipo de datos de carácter, un solo carácter es simplemente una cadena con una longitud de 1.
Se pueden utilizar corchetes para acceder a los elementos de la cadena.
"""

#Ejemplo
cadena = "Hola Mundo"
print(cadena[0])
print(cadena[1])
print(cadena[2])
print(cadena[3])

"""
Iteración de una cadena de caracteres
"""
#Ejemplo
for x in "banana":
    print(x)

"""
Reemplazo de palabras
"""
cadena= "Hola"
print(cadena.replace("o", "x"))

"""
División de Caracteres
"""
print(cadena.split("o"))
"""


Métodos String

Algunos métodos Strings son:
"""

"""
capitalize()
El método capitalize() se aplica sobre una cadena y la devuelve con su primera letra en mayúscula.
"""

#Ejemplo
cadena = "mi cadena de caracteres"
print(cadena.capitalize())

"""
lower()
El método lower() convierte todos los caracteres alfabéticos en minúscula.
"""

#Ejemplo
cadena = "MI CADENA DE CARACTERES"
print(cadena.lower())

"""
wapcase()
El método swapcase() convierte los caracteres alfabéticos con mayúsculas en minúsculas y viceversa.
"""

#Ejemplo
cadena = "mI cAdEnA dE cArActErEs"
print(cadena.swapcase())

"""
upper()
El método upper() convierte todos los caracteres alfabéticos en mayúsculas.
"""

#Ejemplo
cadena = "Mi cadena de Caracteres"
print(cadena.upper())

"""
count(<sub>[, <start>[, <end>]])
El método count() permite contar las veces que otra cadena se encuentra dentro de la primera. Permite también dos parámetros opcionales que indican donde empezar y acabar de buscar.
"""
#Ejemplo
cadena = "Pretty Little"
print(cadena.count("tt"))

"""
isalnum()
El método isalnum() devuelve True si la cadena esta formada únicamente por caracteres alfanuméricos, False de lo contrario. Caracteres como @ o & no son alfanumericos.
"""

#Ejemplo
cadena = "correo@dominio.com"
print(cadena.isalnum())

#Ejemplo 2
cadena = "elton96"
print(cadena.isalnum())

"""
isalpha()
El método isalpha() devuelve True si todos los caracteres son alfabéticos, False de lo contrario.
"""

#Ejemplo de salida True
cadena = "abcdefg"
print(cadena.isalpha())

#Ejemplo de salida False
cadena = "Hola Mundo" #Su salida será False si contiene un caracter no alfabetico, en este caso, un espacio 
print(cadena.isalpha())


"""
join()
Unir elementos de un iterable (como una lista) en una sola cadena, usando la cadena donde se llama el método como separador
"""

#Ejemplo
palabras = ["Esto", "es", "una", "prueba"]
separador = " "
resultado = separador.join(palabras)  
print(resultado)


"""
Para más información visitar esta página: https://ellibrodepython.com/cadenas-python, https://www.w3schools.com/python/python_strings.asp
"""

