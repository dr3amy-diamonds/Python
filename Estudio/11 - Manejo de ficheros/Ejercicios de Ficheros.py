#Solución de Ejercicio 1
with open("mensaje2.txt", "w" ) as archivo:
    archivo.write("Este es mi primer archivo creado desde Python. ")

print("================================================================================================================================================")
#Solución de Ejercicio 2
try:
    archivo = open("mensaje2.txt", "r", encoding="utf-8")
    contenido = archivo.read()
    print(contenido)
    archivo.close()
except FileNotFoundError:
    print("El archivo no existe.")

print("================================================================================================================================================")


#Solución de Ejercicio 3
with open("poema.txt", "r", encoding="utf-8") as archivo:
    contador = 1
    for linea in archivo:
        linea_sin_salto = linea.strip()
        if linea_sin_salto:  # Solo cuenta si NO está vacía
            print(f"{contador}: {linea_sin_salto}")
            contador += 1
        else:
            print("")

print("================================================================================================================================================")

#Solución de Ejercicio 4
with open("datos.txt", "r", encoding="utf-8") as archivo:
    contador = 0
    for linea in archivo:
        linea_sin_salto = linea.strip()
        if linea_sin_salto:  # Solo cuenta si NO está vacía
            contador += 1
        else:
            print("")

print (f"Este Archivo tiene {contador} líneas ")

print("================================================================================================================================================")

#Solución de Ejercicio 5
with open("log.txt", "a", encoding="utf-8") as archivo:
    archivo.write("\nEste es un nuevo texto que se agrega.\n")

print("Revisa el archivo")

print("================================================================================================================================================")

#Solución de Ejercicio 6
origen = "entrada.txt"
destino = "copia.txt"

with open(origen, "r", encoding="utf-8") as archivo_origen:
    with open(destino, "w", encoding="utf-8") as archivo_destino:
        contenido = archivo_origen.read()
        archivo_destino.write(contenido)

print(f"Contenido de '{origen}' copiado a '{destino}'")

print("================================================================================================================================================")

#Solución de Ejercicio 7

archivo = input("Introduce el nombre del archivo junto con su extensión (.txt, .pdf, etc.):\n")
try:
    with open(archivo, 'r',encoding="utf-8" ):
        print("El archivo existe")
except FileNotFoundError:
    print("El archivo no se encontró")

print("================================================================================================================================================")

#Solución de Ejercicio 8

archivo2 = input("Introduce el nombre del archivo junto con su extensión (.txt, .pdf, etc.):\n")
try:
    with open(archivo2, 'r', encoding="utf-8"):
        print("El archivo ya existe, no puedo crearlo")
except FileNotFoundError:
    print("El archivo no existe. Se creará uno nuevo")
    with open(archivo2, "x") as f:
        f.write("Este archivo se creó solo si no existía.")
        print("Archivo creado exitosamente.")

print("================================================================================================================================================")

#Solución de Ejercicio 9
# Abrir el archivo de entrada y el archivo de salida
with open("notas.txt", "r", encoding="utf-8") as entrada, \
    open("notas_filtradas.txt", "w", encoding="utf-8") as salida:

    for linea in entrada:
        linea = linea.strip()  # Quitar saltos de línea

        # Verificar que tenga el formato correcto con ":"
        if ":" not in linea:
            continue  # Línea inválida → no se guarda

        # Separar nombre y nota
        try:
            nombre, nota_str = linea.split(":")
            nota = int(nota_str.strip())  # Convertir la nota a número
        except:
            continue  # Si falla, la línea no es válida

        # Validar rango de la nota
        if 0 <= nota <= 100:
            salida.write(linea + "\n")  # Guardar la línea válida
        

print("================================================================================================================================================")

#Solución de Ejercicio 10
import os

ARCHIVO = "personas.txt"


def asegurar_archivo():
    """Crea el archivo si no existe."""
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            pass  # Solo crear el archivo vacío


def agregar_persona():
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    ciudad = input("Ciudad: ")

    with open(ARCHIVO, "a", encoding="utf-8") as f:
        f.write(f"{nombre},{edad},{ciudad}\n")

    print("Persona agregada correctamente.\n")


def listar_personas():
    asegurar_archivo()

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        contenido = f.readlines()

    if not contenido:
        print("No hay personas registradas.\n")
        return

    print("\n--- Lista de personas ---")
    for linea in contenido:
        print(linea.strip())
    print()


def buscar_persona():
    asegurar_archivo()
    nombre_buscar = input("Nombre a buscar: ").lower()

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        encontrado = False
        for linea in f:
            nombre = linea.split(",")[0].lower()

            if nombre_buscar in nombre:
                print("Encontrado:", linea.strip())
                encontrado = True

        if not encontrado:
            print("No se encontró esa persona.\n")


def eliminar_persona():
    asegurar_archivo()
    nombre_eliminar = input("Nombre de la persona a eliminar: ").lower()

    nueva_lista = []
    eliminado = False

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        for linea in f:
            nombre = linea.split(",")[0].lower()
            if nombre == nombre_eliminar:
                eliminado = True
            else:
                nueva_lista.append(linea)

    # Reescribir el archivo sin la línea eliminada
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        f.writelines(nueva_lista)

    if eliminado:
        print("Persona eliminada correctamente.\n")
    else:
        print("No se encontró una persona con ese nombre.\n")


def menu():
    asegurar_archivo()

    while True:
        print("----- Menú -----")
        print("1. Agregar persona")
        print("2. Listar personas")
        print("3. Buscar persona")
        print("4. Eliminar persona")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_persona()
        elif opcion == "2":
            listar_personas()
        elif opcion == "3":
            buscar_persona()
        elif opcion == "4":
            eliminar_persona()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.\n")


# Ejecutar el programa
menu()
