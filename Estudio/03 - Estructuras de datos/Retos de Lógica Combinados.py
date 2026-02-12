"""
Retos de Lógica Combinados
"""


"""
Ejercicio 1:
1. Crea un programa que guarde en una lista los números del 1 al 20.
Convierte esa lista en un conjunto para eliminar posibles duplicados.
Convierte ese conjunto en una tupla.
Imprime la suma de todos sus elementos.
"""

#Creación de la lista
lista=[]


for x in range(20):
    numero= int(input("Introduce un número del 1 al 20: "))
    
    if numero < 1 or numero > 20:
        print("❌ Número fuera de rango. Intenta de nuevo.")
        continue

    if numero in lista:
        print("⚠️ Ese número ya fue introducido. Elige otro.") #No hace falta convertirla a conjunto si ya tenemos uan condioncal para que no se repita
    else:
        lista.append(numero)
        lista.sort()

#Visualizamos la lista creada       
print(lista)

#Conversión a tupla
tupla=tuple(lista)
print(tupla)

#Imprimri suma
suma_lista=sum(tupla)
print(f'La suma de todos los elementos da como resultado: ', suma_lista)


"""
Ejercicio 2:

2. Diseña un diccionario de contactos, donde la clave sea el nombre de la persona y el valor su número de teléfono.
Agrega 3 contactos.
Muestra todos los contactos.
Permite al usuario buscar un contacto por nombre.
Permite eliminar un contacto.
"""

Contactos={}

for x in range(3):
    nombre=input("Introduce el nombre: ")
    numero_telefono=int(input("Introduce el número de télefono: "))
    Contactos[nombre] = numero_telefono

#Contactos creados
print("Contactos creados creado:")
print(Contactos)

#Buscar contacto por nombre
buscar_contacto = input("Introduce el nombre: ")

if buscar_contacto in Contactos:
    numero = Contactos[buscar_contacto]
    print(f" Número de teléfono de {buscar_contacto}: {numero}")
else:
    print(" Nombre no encontrado en la base de datos.")

#Eliminar contacto
opcion = input("¿Quieres eliminar por nombre (n) o por número (t)? ").lower()

if opcion == "n":
    nombre = input("Introduce el nombre del contacto a eliminar: ")
    if nombre in Contactos:
        del Contactos[nombre]
        print(f" Contacto '{nombre}' eliminado.")
    else:
        print(" Nombre no encontrado.")

elif opcion == "t":
    numero = input("Introduce el número de teléfono a eliminar: ")
    encontrado = None
    for nombre, telefono in Contactos.items():
        if telefono == numero:
            encontrado = nombre
            break
    if encontrado:
        del Contactos[encontrado]
        print(f"Contacto con número '{numero}' eliminado (Nombre: {encontrado}).")
    else:
        print(" Número no encontrado.")

else:
    print("Opción inválida. Usa 'n' para nombre o 't' para teléfono.")

print(Contactos)

"""
Ejercicio 3:
3. Crea un programa que cuente cuántas veces aparece cada palabra en la lista:
palabras = ["python", "java", "python", "c++", "java", "python"]
"""
palabras = ["python", "java", "python", "c++", "java", "python"]

frecuencia = {}

for x in palabras:
    if x in frecuencia:
        frecuencia[x] += 1
    else:
        frecuencia[x] = 1
print(frecuencia) #
