"""
Ejercicio 1 :

1. Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
el nombre de una nueva web.
"""
#Creación de pila de desplazamiento

def navegador_web():

    atras = []
    adelante = []
    actual = "Inicio"
    print("Estoy en:", actual)

    while True:
        comando = input("Escribe una página o 'atras'/'adelante': ").strip()
        
        if comando.lower() == "atras":
            if atras:
                adelante.append(actual)
                actual = atras.pop()
            else:
                print("No hay páginas atrás.")
        elif comando.lower() == "adelante":
            if adelante:
                atras.append(actual)
                actual = adelante.pop()
            else:
                print("No hay páginas adelante.")
        elif comando=="salir":
            print("Saliendo del navegador web.")
            break
        else:
            atras.append(actual)
            actual = comando
            adelante.clear()
        
        print("Estoy en:", actual)


#Llamar función
navegador_web()

"""
Ejercicio 2:
2. Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una impresora compartida que recibe documentos y los imprime cuando así se le indica. La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se interpretan como nombres de documentos.
"""

#Creación de cola de desplazamiento
def Impresora():
    impresora=[]

    while True:

        comando = input("Añade un documento o selecciona imprimir/salir: ")

        if comando == "salir":
            break
        elif comando == "imprimir":
            if len(impresora) > 0:
                print(f"Imprimiendo: {impresora.pop(0)}")
            else:
                print("No hay nada que imprimir")
        else:
            impresora.append(comando)

        print(f"Cola de impresión: {impresora}")


Impresora()