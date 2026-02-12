import datetime #Para las fechas y su visualización

tareas = []

class TareaNoGuardada(Exception):
    pass

class TareaNoEliminada(Exception):
    pass

def Agregar_tarea():
    agregar_tareas=input("Agrega el titulo de la tarea: \n ")
    agregar_descripcion=input("Agrega la descripción de la tarea: \n ")
    entrada = input("Introduce la fecha (formato: DD-MM-AAAA): ")
    try:
        fecha = datetime.datetime.strptime(entrada, "%d-%m-%Y")
        fecha_formateada = fecha.strftime("%d-%m-%Y")
        print(" Fecha ingresada correctamente.")
    except ValueError:
        print("❌ Formato inválido. Usa el formato DD-MM-AAAA, por ejemplo: 10-11-2025.")
    
    try:
        tarea = {
        "titulo": agregar_tareas,
        "descripcion": agregar_descripcion,
        "fecha": fecha_formateada
        }
        tareas.append(tarea)
    except Exception as e:
        raise TareaNoGuardada("No se guardó la tarea correctamente.") from e

def visualizar_tarea():
    if not tareas:
        print(" No hay tareas registradas.")
        

    for i, tarea in enumerate(tareas):
        print(f"\nTarea N° {i+1}")
        print(f" Título: {tarea['titulo']}")
        print(f" Descripción: {tarea['descripcion']}")
        print(f" Fecha: {tarea['fecha']}")

def Eliminar_tarea():
    if not tareas:
        print(" No hay tareas para eliminar.")
        

    try:
        eliminar_tareas = int(input("Digita el número de la tarea a eliminar: \n> "))
        if eliminar_tareas < 0 or eliminar_tareas >= len(tareas):
            print("❌ Número fuera de rango. Vuelve a intentarlo.")
            
        tarea_eliminada = tareas.pop(eliminar_tareas)
        print(f" Tarea '{tarea_eliminada['titulo']}' eliminada correctamente.")
    except ValueError:
        print("❌ Digita un número válido, vuelve a intentarlo.")
    except Exception as e:
        raise TareaNoEliminada("La tarea no se eliminó correctamente.") from e

while True:
    print("\n=== Bienvenido al Sistema de Gestión de Tareas ===")
    try:
        opciones = int(input(
        "Por favor, seleccione una opción:\n"
        "1. Agregar tarea\n"  #Se usa lista porque lista es mutable
        "2. Visualizar tareas\n" #Se usa diccionario porque visualizar la tareaa, descripción y fecha de vencimiento
        "3. Eliminar tarea\n" #Se usa lista
        "4. Salir\n"
            )
        )
    except ValueError:
        print("❌ Opción inválida, introduce un número del 1 al 4.")
        continue


    match opciones:
        case 1:
            Agregar_tarea()
        case 2:
            visualizar_tarea()
        case 3:
            Eliminar_tarea()
        case 4:
            print("👋 Saliendo del sistema. ¡Hasta luego!")
            break
        case _:
            print("Opción no válida, intenta de nuevo.")
