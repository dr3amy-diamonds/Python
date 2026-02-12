from collections import deque  # Cola y Pila

# Crear cola y pila
cola = deque()
pila = deque()

# Manejo de errores
class ColaVacia(Exception):
    pass

class PilaVacia(Exception):
    pass

###############-----------------Funciones de la cola--------------##########################
def cola_Agregarelementos():
    elemento = input("Ingrese un elemento: ").strip()
    if not elemento:
        print(" No se puede agregar un elemento vacío.")
        return
    cola.append(elemento)
    print(f"✅ '{elemento}' agregado a la cola.")

def cola_Visualizarelementos():
    if not cola:
        print(" No hay elementos en la cola.")
        return
    print(f"Elementos en la cola: {list(cola)}\n")

def cola_Eliminarelementos():
    if not cola:
        raise ColaVacia(" No hay elementos en la cola")
    eliminado = cola.popleft()
    print(f" '{eliminado}' eliminado de la cola.")
    return eliminado

###############-----------------Funciones de la Pila--------------##########################
def pila_Agregarelementos():
    elemento = input("Ingrese un elemento: ").strip()
    if not elemento:
        print(" No se puede agregar un elemento vacío.")
        return
    pila.append(elemento)
    print(f" '{elemento}' agregado a la pila.")

def pila_Visualizarelementos():
    if not pila:
        print(" No hay elementos en la pila.")
        return
    print(f"Elementos en la pila: {list(pila)}\n")

def pila_Eliminarelementos():
    if not pila:
        raise PilaVacia("❌ No hay elementos en la pila")
    eliminado = pila.pop()
    print(f" '{eliminado}' eliminado de la pila.")
    return eliminado

###############-----------------Menú principal con match-case--------------##########################
while True:
    print("\n=== Bienvenido al simulador de Pila o Cola ===")
    
    try:
        opciones = int(input(
            "Seleccione una opción:\n"
            "1. Elegir Cola\n"
            "2. Elegir Pila\n"
            "3. Salir\n"
        ))
    except ValueError:
        print("❌ Opción inválida, introduce un número del 1 al 3.")
        continue

    match opciones:
        case 1:  # Menú Cola
            while True:
                try:
                    opcion_cola = int(input(
                        "\n--- Menú Cola ---\n"
                        "1. Agregar elemento\n"
                        "2. Ver elementos\n"
                        "3. Eliminar elemento\n"
                        "4. Volver al menú principal\n"
                    ))
                except ValueError:
                    print(" Opción inválida, introduce un número del 1 al 4.")
                    continue

                match opcion_cola:
                    case 1:
                        cola_Agregarelementos()
                    case 2:
                        cola_Visualizarelementos()
                    case 3:
                        try:
                            cola_Eliminarelementos()
                        except ColaVacia as e:
                            print(e)
                    case 4:
                        break
                    case _:
                        print(" Opción no válida")
        
        case 2:  # Menú Pila
            while True:
                try:
                    opcion_pila = int(input(
                        "\n--- Menú Pila ---\n"
                        "1. Agregar elemento\n"
                        "2. Ver elementos\n"
                        "3. Eliminar elemento\n"
                        "4. Volver al menú principal\n"
                    ))
                except ValueError:
                    print(" Opción inválida, introduce un número del 1 al 4.")
                    continue

                match opcion_pila:
                    case 1:
                        pila_Agregarelementos()
                    case 2:
                        pila_Visualizarelementos()
                    case 3:
                        try:
                            pila_Eliminarelementos()
                        except PilaVacia as e:
                            print(e)
                    case 4:
                        break
                    case _:
                        print("❌ Opción no válida")
        
        case 3:
            print(" ¡Gracias por usar el simulador!")
            break

        case _:
            print(" Opción no válida, introduce un número del 1 al 3.")
