"""
Encapsulamiento

El encapsulamiento es el principio de la POO que consiste en ocultar los datos internos de un objeto para que no puedan modificarse directamente desde fuera de la clase.

En lugar de acceder o cambiar los datos libremente, se hace a través de métodos (por ejemplo, getters y setters).
Así, la clase controla cómo se usan sus atributos.

"""

#Ejemplo 1
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo "privado"

    def depositar(self, cantidad):
        self.__saldo += cantidad
        print(f"Depósito exitoso. Saldo actual: {self.__saldo}")

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Saldo actual: {self.__saldo}")
        else:
            print("Fondos insuficientes.")

    def mostrar_saldo(self):
        print(f"Saldo disponible: {self.__saldo}")

"""
Explicación paso a paso:


*   __saldo tiene dos guiones bajos al inicio → eso lo vuelve privado,
o sea, no se puede acceder directamente desde fuera de la clase.

*En vez de modificarlo directamente, usamos métodos:

    depositar() → aumenta el saldo.

    retirar() → resta saldo si hay fondos.

    mostrar_saldo() → muestra el saldo actual.

*Así controlamos qué se puede hacer con ese dato y cómo se hace.
"""

#Ejemplo 2
class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre       # Atributo público
        self.__nota = nota         # Atributo privado (con __)
    def mostrar_nota(self):
        print(f"La nota de {self.nombre} es {self.__nota}")

    def cambiar_nota(self, nueva_nota):
        if 0 <= nueva_nota <= 10:  # validamos la nueva nota
            self.__nota = nueva_nota
            print("Nota actualizada correctamente.")
        else:
            print("Error: la nota debe estar entre 0 y 10.")

# Crear objeto
est1 = Estudiante("Lucía", 8)

# Acceder mediante métodos
est1.mostrar_nota()          # ✅ correcto
est1.cambiar_nota(9)         # ✅ correcto
est1.cambiar_nota(15)        # ❌ rechazado (nota inválida)
est1.mostrar_nota()

# Intento de acceder directamente (esto falla)
#print(est1.__nota)           # ❌ Error: atributo privado

"""
Setter y Getters

Para poder ver o cambiar el valor de manera segura,
creamos métodos especiales dentro de la clase, llamados getter y setter:
"""

#Ejemplo
class Persona:
    def __init__(self, nombre, edad):
        self.__edad = edad

    def get_edad(self):         # getter → para ver el valor
        return self.__edad

    def set_edad(self, nueva_edad):   # setter → para cambiar el valor
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("Edad no válida")

#Se usa de esta manera
p1 = Persona("Ana", 25)
print(p1.get_edad())   # 🟢 muestra 25
p1.set_edad(-10)       # ❌ Edad no válida
p1.set_edad(30)        # 🟢 cambia a 30
print(p1.get_edad())   # 🟢 muestra 30

"""
Se puede hacer con @property

En Python moderno, no es necesario escribir get_edad() o set_edad() con esos nombres.
Se puede usar el decorador @property para hacer que parezca un atributo normal.
"""

#Ejemplo
class Persona:
    def __init__(self, nombre, edad):
        self.__edad = edad

    @property
    def edad(self):           # getter
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):   # setter
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("Edad no válida")

#Se usa de esta manera
p1 = Persona("Ana", 25)
print(p1.edad)   # llama al getter
p1.edad = 30     # llama al setter
p1.edad = -5     # "Edad no válida"
