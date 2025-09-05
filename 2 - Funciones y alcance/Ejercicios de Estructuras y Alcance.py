"""
Ejercicio 1: Saludo personalizado
1. Crea una función llamada saludo(nombre) que reciba un nombre como argumento y muestre en pantalla:
"""
def saludar(nombre):
    return "Hola, " + nombre
print(saludar("Valentina")) 

"""
Ejercicio 2: Edad con valor predeterminado
2. Crea una función mostrar_edad(nombre, edad=18) que muestre en pantalla:
"""
def informacion(nombre, edad=22):
    return "Hola " + nombre + "Tu edad es " + edad

print(informacion("Valentina"))

"""
Ejercicio 3: Pasando listas
3. Crea una función mostrar_lista(lista) que reciba una lista de frutas y las muestre una por una.
"""
def mostrar_lista(lista):
    for x in lista:
        print(x)

lista = ["Pollo", "Arroz", "Cerdo"]
mostrar_lista(lista)

"""
Ejercicio 4: Uso de kwargs
4. Crea una función informacion_persona(**Persona) que reciba nombre, edad y ciudad como argumentos
"""
def informacion_persona(**Persona):
    # kwargs llega como un diccionario
    # entonces podemos acceder a los datos con las "claves"
    print("Nombre:", Persona["nombre"])
    print("Edad:", Persona["edad"])
    print("Ciudad:", Persona["ciudad"])

# Llamamos a la función pasando los argumentos con clave=valor
informacion_persona(nombre="Nancy", edad=46, ciudad="Aldeavieja")

"""
Ejercicio 4.1: Uso de kwargs
4.1 . Crea una función informacion_mascota(**mascota) que reciba datos de una mascota (nombre, tipo, edad y dueño). La función debe imprimirlos uno por uno.
"""

def informacion_mascota(**mascota):
    return mascota

print(informacion_mascota(nombre="Luna", Tipo="Perro", Edad="9", Dueno="Valentina"))


"""
Ejercicio 5: Retorno múltiple
5. Crea una función calcular_potencia_y_raiz(x) que:
Devuelva x al cuadrado.
Devuelva la raíz cuadrada de x.
Llama a la función y guarda ambos valores en variables.
"""
import math  # para usar la función sqrt (raíz cuadrada)

def calcular_potencia_y_raiz(x):
    potencia = x ** 2          # x al cuadrado
    raiz = math.sqrt(x)        # raíz cuadrada
    return potencia, raiz      # devolvemos dos valores a la vez

# Llamamos la función y guardamos los resultados en variables
resultado_potencia, resultado_raiz = calcular_potencia_y_raiz(9)

print("Potencia:", resultado_potencia)
print("Raíz cuadrada:", resultado_raiz)

"""
Ejercicio 5.1 : Retorno múltiple
5.1 Crea una función calcular_area_y_perimetro(lado) que:
Devuelva el área de un cuadrado (lado * lado).
Devuelva el perímetro de un cuadrado (4 * lado).
Llama a la función con un número y guarda ambos valores en variables.
"""

def calcular_area_y_perimetro(lado):
    area_cuadrado=lado * lado
    perimetro = 4 * lado
    return area_cuadrado, perimetro

resultado_area, resultado_perimetro = calcular_area_y_perimetro(9)
print ("Area: ", resultado_area)
print ("Perimetro: ", resultado_perimetro)

"""
Ejercicio 6: Alcance de variables (scope)
6. Haz lo siguiente:
Crea una variable global mensaje = "Soy global".
Define una función mostrar_mensaje() que declare otra variable mensaje = "Soy local" y la imprima.
Imprime también la variable fuera de la función.
"""

mensaje = "Soy global"

# Se define la función 'mostrar_mensaje'
def mostrar_mensaje():
    mensaje = "Soy local"
    print(mensaje) 

# Se llama a la función
mostrar_mensaje()

# Se imprime la variable global 'mensaje'
print(mensaje)

"""
Ejercicio 7: Menú de operaciones
7. Crea una función para cada operación matemática: suma, resta, multiplicacion, division.
Luego crea otra función menu() que muestre opciones (1. Suma, 2. Resta, …, 5. Salir).
👉 Según la opción que elija el usuario, llama a la función correspondiente.
"""
# Funciones de operaciones
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: no se puede dividir entre cero"


# Función menú
def menu():
    while True:
        print("\n--- Menú de Operaciones ---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "5":
            print("¡Adiós! 👋")
            break  # salir del bucle

        # Pedir los números solo si la opción es válida
        if opcion in ["1", "2", "3", "4"]:
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))

            if opcion == "1":
                print("Resultado:", suma(a, b))
            elif opcion == "2":
                print("Resultado:", resta(a, b))
            elif opcion == "3":
                print("Resultado:", multiplicacion(a, b))
            elif opcion == "4":
                print("Resultado:", division(a, b))
        else:
            print(" pción no válida, intenta de nuevo.")


# Llamar al menú principal
menu()
