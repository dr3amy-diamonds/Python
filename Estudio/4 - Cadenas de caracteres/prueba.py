#Crear Función
def programa():
    #Crear variables
    nombre = input("Digita tu nombre por favor: ")
    edad = int(input("Digita tu edad por favor: "))
    edad_sumada=10+edad
    saludo = "Hola, %s.  Tienes %d años." % (nombre, edad_sumada)
    return saludo

print(programa())