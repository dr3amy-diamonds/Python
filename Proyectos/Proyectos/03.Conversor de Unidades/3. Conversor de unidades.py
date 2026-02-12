#Creacion de funciones

def kilometros():
    metros = float(input("Ingrese la cantidad de metros a convertir en kilómetros: "))
    kilometros = metros / 1000
    return (f"{metros} metros son equivalentes a {kilometros} kilómetros.")

def Fahrenheit():
    celsius = float(input('Ingrese la temperatura en grados Celsius: '))
    fahrenheit = 9.0/5.0 * celsius +32
    return (f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit")

def libras():
    libras = float(input('Ingrese las libras: '))
    kilogramos = libras / 2.205
    return (f"El peso en kilogramos es: {kilogramos}")

#Creación del menú

while True:
    opciones=int(input("Elige una de las opciones:\n1. Metros a Kilómetros\n2. Celsius a Fahrenheit\n3. Libras a Kilos\n "))
    
    match opciones:
        case 1:
            print(kilometros())
            break
        case 2:
            print(Fahrenheit())
            break
        case 3:
            print(libras())
            break

