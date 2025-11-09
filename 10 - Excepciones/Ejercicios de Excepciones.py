#Nivel 1 — Fundamentos + control de errores

"""
Ejercicio 1: “Calculadora segura”

*   Practicas: entrada de usuario, operadores, excepciones básicas (try/except)
*   Temas: variables, input, operaciones matemáticas

Enunciado:
Crea una calculadora que pida dos números y una operación (+, -, *, /).

Usa try/except para evitar errores de tipo o división por cero.

Si el usuario ingresa algo no válido, vuelve a pedirlo.

    Pista:
Usa un bucle while True: y break cuando el cálculo sea válido.
"""

while True:
    # 1. Muestra el menú
    print("\n--- Calculadora ---")
    print("1. Suma( + )")
    print("2. Resta ( - )")
    print("3. Multiplicacion ( * ) ")
    print("4. Division ( / )")
    print("5. Salir")

    opcion = input("Elige una operación: ")
    if opcion == "5":
        print("Fin del programa")
        break

    num1= float(input("Ingresa el primer número: "))
    num2= float(input("Ingresa el segundo número: "))
    # 2. Realiza la operación
    try:
        if opcion == "1":
            print(f"Resultado: {num1 + num2}")
            break
        elif opcion == "2":
            print(f"Resultado: {num1 - num2}")
            break
        elif opcion == "3":
            print(f"Resultado: {num1 * num2}")
            break
        elif opcion == "4":
            print(f"Resultado: {num1 / num2}")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
    except ZeroDivisionError:
        print("Error: División por cero. Intenta de nuevo.")
    except ValueError:
        print("Error: Entrada no válida. Intenta de nuevo.")
    finally:
        print("Fin del programa")


#Nivel 2 — Funciones y validaciones

"""
Ejercicio 2 — “Verificador de nombres”
🎯 Objetivo:

Practicar el uso de funciones y manejo de errores con try y except.

📘 Instrucciones:

Crea un programa que pida al usuario que escriba su nombre.
Tu tarea será asegurarte de que el nombre sea válido.

Crea una función llamada verificar_nombre(nombre) que haga lo siguiente:

Si el usuario no escribe nada, muestra un error diciendo:
"El nombre no puede estar vacío."

Si el nombre tiene menos de 3 letras, muestra un error diciendo:
"El nombre es demasiado corto."

Si el nombre tiene solo letras (sin números ni símbolos), muestra:
"Nombre válido ✅"

Usa raise ValueError("mensaje") para mostrar los errores dentro de la función.

En el programa principal:

Pide al usuario que escriba su nombre.

Llama a la función dentro de un bloque try/except.

Si hay error, muestra el mensaje y vuelve a pedir el nombre.
"""

def verificar_nombre(nombre):
    if not nombre:
        raise ValueError("El nombre no puede estar vacío.")
    if len(nombre) <3:
        raise ValueError("El nombre es demasiado corto.")

try:
    nombre=input("Escriba su nombre: ")
    verificar_nombre(nombre)
    print(f"Su nombre es {nombre}")
except ValueError as e:
    print(f"Error: {e}")



#Nivel 3 — Listas, bucles y funciones

"""
Ejercicio 3: “Lista de notas”

*   Practicas: listas, bucles, promedio, validaciones
*   Temas: estructuras de datos + try/except

Enunciado:
Crea un programa que pida 5 notas (0–10).
Si el usuario ingresa un valor inválido, muestra un error y vuelve a pedir.
Al final, muestra el promedio y si está aprobado (≥6).

    Pista:
Guarda las notas en una lista, usa sum() y len() para el promedio.
"""
notas = []

while len(notas) < 5:
    while True:
        try:
            datos = float(input("Ingresa una nota (Son 5 notas): "))
            notas.append(datos)
            break
        except ValueError:
            print("Error: Debes ingresar un número válido. Inténtalo de nuevo.")

# Calcular el promedio una vez que se tienen las 5 notas
promedio = sum(notas) / len(notas)
print(f"El promedio de las notas es: {promedio:.2f}")

# Evaluar si aprueba
if promedio >= 6:
    print("El estudiante aprueba.")
else:
    print("El estudiante no aprueba.")

#Nivel 4 — Clases simples

"""
Ejercicio 4 — Sistema de reservas de hotel

Enunciado:

Cree un programa en Python que simule la gestión de reservas de un hotel utilizando Programación Orientada a Objetos.

Implemente una clase llamada ReservaHotel que permita realizar, cancelar y consultar reservas de habitaciones.

La clase debe cumplir con las siguientes condiciones:

Posee los atributos privados:

_habitaciones_totales → número total de habitaciones del hotel.

_habitaciones_ocupadas → número de habitaciones actualmente reservadas.

Debe contener los métodos:

reservar(cantidad) → realiza una reserva.

Si la cantidad ingresada es menor o igual a 0, debe lanzar una excepción CantidadInvalidaError.

Si no hay suficientes habitaciones disponibles, debe lanzar una excepción NoDisponiblesError.

cancelar(cantidad) → cancela una reserva.

Si se intenta cancelar más habitaciones de las ocupadas, debe lanzar una excepción CancelacionInvalidaError.

mostrar_estado() → muestra el número total de habitaciones, las ocupadas y las disponibles.

Cree las siguientes clases de excepciones personalizadas:

CantidadInvalidaError

NoDisponiblesError

CancelacionInvalidaError

En el programa principal:

Cree un objeto de tipo ReservaHotel con un número de habitaciones inicial.

Pruebe distintos casos de reserva y cancelación utilizando bloques try/except para capturar los errores y mostrar mensajes apropiados al usuario.
"""

class CantidadInvalidaError(Exception):
    pass

class NoDisponiblesError(Exception):
    pass

class CancelacionInvalidaError(Exception):
    pass

class ReservaHotel:
    def __init__(self, habitaciones_totales, habitaciones_ocupadas=0, habitaciones_reservadas=0):
        self.__habitaciones_totales = habitaciones_totales
        self.__habitaciones_ocupadas = habitaciones_ocupadas
        self.__habitaciones_reservadas = habitaciones_reservadas

    def reservar(self, habitaciones_a_reservar):
        habitaciones_disponibles = self.__habitaciones_totales - self.__habitaciones_ocupadas - self.__habitaciones_reservadas
        if habitaciones_a_reservar <= 0:
            raise CantidadInvalidaError("Introduzca un número de habitaciones a reservar mayores a 0 por favor.")

        if habitaciones_a_reservar > habitaciones_disponibles:
            raise NoDisponiblesError(f"No hay suficientes habitaciones disponibles, solo quedan {habitaciones_disponibles} habitaciones disponibles.")

        self.__habitaciones_reservadas += habitaciones_a_reservar
        print(f"Se reservaron {habitaciones_a_reservar} habitaciones.")

    def cancelar(self, habitaciones_a_cancelar):
        if habitaciones_a_cancelar > self.__habitaciones_reservadas:
            raise CancelacionInvalidaError("No puedes cancelar un número de habitaciones mayor a las que reservaste.")
        else:
            self.__habitaciones_reservadas -= habitaciones_a_cancelar
            print(f"Se cancelaron {habitaciones_a_cancelar} habitaciones.")

    def mostrar_estado(self):
        disponibles = self.__habitaciones_totales - self.__habitaciones_ocupadas - self.__habitaciones_reservadas
        print(f"Total de habitaciones: {self.__habitaciones_totales}")
        print(f"Habitaciones ocupadas: {self.__habitaciones_ocupadas}")
        print(f"Habitaciones reservadas: {self.__habitaciones_reservadas}")
        print(f"Habitaciones disponibles: {disponibles}")

if __name__ == "__main__":
    hotel = ReservaHotel(50)
    try:
        hotel.reservar(10)
        hotel.mostrar_estado()
        hotel.cancelar(5)
        hotel.mostrar_estado()
        hotel.reservar(45)
    except CantidadInvalidaError as e:
        print(f"Error: {e}")
    except NoDisponiblesError as e:
        print(f"Error: {e}")
    except CancelacionInvalidaError as e:
        print(f"Error: {e}")



#Nivel 5 — Herencia + Polimorfismo + Excepciones

"""
Ejercicio 5: “Sistema de pagos avanzado”

🎯 Practicas: herencia, sobrescritura, manejo de errores
🧠 Temas: POO + polimorfismo + excepciones

Enunciado:
Crea una clase base MetodoPago con atributo _monto y método procesar_pago().
Subclases:

Tarjeta: cobra 5% de comisión

Efectivo: sin comisión

Cripto: cobra 2%

Valida que el monto sea positivo, de lo contrario lanza MontoInvalidoError.
Muestra el total final con cada tipo de pago en un bucle.

💡 Pista:
Cada subclase redefine procesar_pago() aplicando su cálculo propio.
"""

class MontoInvalidoError(Exception):
    pass

class MetodoPago:
    def __init__(self, monto):
        self._monto=monto
    
    def procesar_pago(self):
        if self._monto <=0:
            raise MontoInvalidoError("Monto Invalido, Introduzca un valor superior a $0")
        return f"Pago de {self._monto} procesado con éxito."

class Tarjeta(MetodoPago):
    def procesar_pago(self):
        if self._monto <= 0:
            raise MontoInvalidoError("Monto no válido para procesar el pago.")
        comision = self._monto * 0.05
        total = self._monto + comision
        return f"Pagaste {self._monto} con tarjeta. Se te suma un 5% de comisión ({comision:.2f}). Total: {total:.2f}"

class Efectivo(MetodoPago):
    def procesar_pago(self):
        if self._monto <= 0:
            raise MontoInvalidoError("Monto no válido para procesar el pago.")
        return f"Pagaste {self._monto} en efectivo. No se te agrega comisiones adicionales. Total: {self._monto:.2f}"

class Cripto(MetodoPago):
    def procesar_pago(self):
        if self._monto <= 0:
            raise MontoInvalidoError("Monto no válido para procesar el pago.")
        comision = self._monto * 0.02
        total = self._monto + comision
        return f"Pagaste {self._monto} con criptomonedas. Aplica una comisión del 2% ({comision:.2f}). Total: {total:.2f}"

banco = [
    Tarjeta(10),
    Efectivo(10),
    Cripto(10),
    Tarjeta(-15),
    Efectivo(0),
    Cripto(-100)
]

for metodo in banco:
    try:
        print(metodo.procesar_pago())
    except MontoInvalidoError as e:
        print(f"Error: {e}")



