"""
Ejercicio 1: Teléfono Móvil
1. Crea una clase Telefono que permita:

*   Hacer llamadas (llamar(numero)) → imprime "Llamando al número ..."

*   Enviar mensajes (enviar_mensaje(numero, texto)) → imprime "Mensaje a ...: ..."

Como usuario, no te interesa cómo se conecta a la red, solo qué métodos puedes usar. 
"""

class Telefono:
    def __init__(self, marca):
        self.marca = marca

    def llamar(self, numero): 
        print(f"Llamando al número {numero}...")

    def enviar_mensaje(self, numero, texto):  
        print(f"Mensaje a {numero}: {texto}")

# Crear objeto
telefono=Telefono("Samsung")

# Usar métodos
telefono.llamar(31452157)
telefono.enviar_mensaje(31452157, "Hola")


"""
Ejercicio 2: Bicicleta

2. Crea una clase Bicicleta que tenga:

*   Un método pedalear() → imprime "Pedaleando..."

*   Un método frenar() → imprime "La bicicleta se detuvo"

El que usa la clase no necesita saber cómo giran las ruedas, solo los métodos disponibles.
"""

class Bicicleta:
    def __init__(self, tipo):
        self.tipo = tipo

    def pedalear(self):
        print("Pedaleando...")

    def frenar(self):
        print("La bicicleta se detuvo")


# Crear objeto
mi_bici = Bicicleta("Montaña")

# Usar métodos
mi_bici.pedalear()
mi_bici.frenar()


"""
Ejercicio 3: Pizzería

Crea una clase Pizzeria que tenga:

*   Un método pedir_pizza(sabor) → imprime "Preparando pizza de {sabor}"

*   Un método entregar_pizza() → imprime "Pizza entregada"

El usuario no ve cómo se hace la pizza, solo pide y recibe.
"""

class Pizzeria:
    def __init__(self, size):
        self.size = size

    def pedir_pizza(self, sabor):
        print(f"Preparando pizza de {sabor}")
    
    def entregar_pizza(self):
        print("Pizza entregada")

# Crear objeto
mi_pizza = Pizzeria("Familiar")

# Usar métodos
mi_pizza.pedir_pizza("Jamón y Champiñones")
mi_pizza.entregar_pizza()

"""
Ejercicio 4: Computadora

4. Crea una clase Computadora que permita simular algunas acciones básicas.

Métodos:

*   Encender() → imprime "La computadora se está encendiendo..."

*   Abrir_programa(programa) → imprime "Abriendo el programa {programa}"

*   Apagar() → imprime "La computadora se está apagando..."
"""

class Computadora:
    def __init__(self,marca):
        self.marca=marca
    
    def Encender(self):
        print("La computadora se está encendiendo...")
    
    def Abrir_programa(self, programa):
        print(f'Abriendo el programa {programa}')
    
    def Apagar(self):
        print("La computadora se está apagando...")

# Crear objeto
mi_computadora = Computadora("HP")

# Usar métodos
mi_computadora.Encender()
mi_computadora.Abrir_programa("Paint")
mi_computadora.Apagar()


"""
Ejercicio 5: Auto

5. Crea una clase Auto con los siguientes métodos:

Métodos:

*   arrancar() → imprime "El auto arrancó."

*   acelerar() → imprime "El auto está acelerando..."

*   detener() → imprime "El auto se ha detenido."
"""

class Auto:

    def __init__(self, color):
        self.color=color
    
    def arrancar(self):
        print("El auto arrancó.")
    
    def acelerar(self):
        print("El auto está acelerando...")

    def detener(self):
        print("El auto se ha detenido.")

#Crear Objeto
mi_auto=Auto("Negro")

#Usar métodos
mi_auto.arrancar()
mi_auto.acelerar()
mi_auto.detener()

"""
Ejercicio 5: Estudiante

5. Crea una clase Estudiante que represente a un alumno.

Atributos (en el __init__):

*   nombre

*   curso

Métodos:

*   presentarse() → imprime "Hola, soy {nombre} del curso {curso}"

*   estudiar(materia) → imprime "Estoy estudiando {materia}"
"""

class Estudiante:

    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso
    
    def presentarse(self):
        print(f'Hola, soy {self.nombre} del curso {self.curso}')
    
    def estudiar(self, materia):
        print(f"Estoy estudiando {materia}")

# Crear objeto
mi_estudiante = Estudiante("Camila", "11°")

# Usar métodos
mi_estudiante.presentarse()
mi_estudiante.estudiar("Lectura")
