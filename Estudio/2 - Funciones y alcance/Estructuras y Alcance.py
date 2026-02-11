#Funciones
"""
Creando funciones
En Python, una función se define utilizando la defpalabra clave:
"""
def mi_funcion():
    print("Hola")

"""
Llamar una función
Para llamar a una función, utilice el nombre de la función seguido de paréntesis:
"""
def mi_funcion():
    print("Hola")

mi_funcion()

"""
Argumentos
La información se puede pasar a las funciones como argumentos.

Los argumentos se especifican después del nombre de la función, entre paréntesis. Puedes agregar tantos argumentos como quieras, simplemente separándolos con una coma.

El siguiente ejemplo tiene una función con un argumento (fname). Al llamar a la función, se pasa un nombre, que se usa dentro de la función para imprimir el nombre completo:
"""
def mis_hermanos(fname):
    print(fname + " Refsnes")

mis_hermanos("Emil")
mis_hermanos("Tobias")
mis_hermanos("Linus")

################################

def mi_funcion(fname, lname):
    print(fname + " " + lname)

mi_funcion("Emil", "Refsnes")

"""
Argumentos de palabras clave
También puedes enviar argumentos con la sintaxis clave = valor .
De esta manera el orden de los argumentos no importa
"""
def mis_hijos(nene3, nene2, nene1):
    print("The youngest child is " + nene3)

mis_hijos(nene1 = "Emil", child2 = "Tobias", nene3 = "Linus")

"""
Argumentos de palabras clave arbitrarias, **kwargs
Si no sabe cuántos argumentos de palabras clave se pasarán a su función, agregue dos asteriscos: **antes del nombre del parámetro en la definición de la función.
De esta manera, la función recibirá un diccionario de argumentos y podrá acceder a los elementos en consecuencia:
"""

#Si se desconoce el número de argumentos de palabras clave, agregue un doble **antes del nombre del parámetro:
def mi_funcion(**nene):
    print("His last name is " + nene["lname"])

mi_funcion(fname = "Tobias", lname = "Refsnes")


"""
Valor del parámetro predeterminado

El siguiente ejemplo muestra cómo utilizar un valor de parámetro predeterminado.
Si llamamos a la función sin argumentos, utiliza el valor predeterminado:
"""
def mi_Mundo(country = "Norway"):
    print("I am from " + country)

mi_Mundo("Sweden")
mi_Mundo("India")
mi_Mundo()
mi_Mundo("Brazil")

"""
Pasar una lista como argumento

Puede enviar cualquier tipo de datos de argumento a una función (cadena, número, lista, diccionario, etc.) y se tratará como el mismo tipo de datos dentro de la función.
Por ejemplo, si envías una lista como argumento, seguirá siendo una lista cuando llegue a la función:
"""

def Mi_nevera(comida):
    for x in comida:
        print(x)

Comida = ["Pollo", "Arroz", "Cerdo"]

Mi_nevera(Comida)

"""
Valores de retorno

Para permitir que una función devuelva un valor, utilice la returndeclaración:
"""
def mi_multiplacion(x):
    return 8 * x

print(mi_multiplacion(1))
print(mi_multiplacion(6))
print(mi_multiplacion(8))


"""
La Declaración de Pase

Las definiciones de funciones no pueden estar vacías, pero si por alguna razón tienes una definición de función sin contenido, ponla en la passdeclaración para evitar recibir un error.
"""
def mi_funcion():
    pass


"""
Ejemplos Aritmeticos
"""

#Suma
def suma(a,b):
    result= a+b
    print(result)

suma(1,1)

#Resta
def resta(a,b):
    result=a-b
    return result
print(resta(10,5))

#Multiplicación
def multiplicacion(a,b):
    result=a*b
    return result
print(multiplicacion(2,2))

#Division
def division(a,b):
    result=a/b
    print(result)

division(5,5)

#Potenciación
def potencia(a,b):
    result=a**b
    return result

print(potencia(2,2))

#Radicación
def radicacion (a,b):
    # Para calcular la raíz cuadrada (n=2)
    result_a= a** (1/2)
    #Para calcular la raíz cúbica (n=3)
    result_b= b** (1/3)
    return result_a, result_b

print(radicacion(4,8))



"""
Parte del contenido presentado en este archivo ha sido extraído y adaptado de W3Schools.com, una plataforma educativa propiedad de Refsnes Data. Todos los derechos sobre dicho material pertenecen exclusivamente a sus autores.

El uso de esta información se realiza con fines educativos y de referencia, respetando los términos de uso establecidos por W3Schools. No se pretende infringir derechos de propiedad intelectual ni atribuir autoría sobre el contenido original.
"""