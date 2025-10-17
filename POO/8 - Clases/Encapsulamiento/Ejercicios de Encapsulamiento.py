"""
Ejercicio 1: Encapsulamiento básico

Queremos crear una clase llamada CuentaBancaria.
Esta clase tendrá un atributo privado __saldo, y tres métodos:

1.  depositar(cantidad) → suma dinero si la cantidad es positiva

2.  retirar(cantidad) → resta dinero solo si hay suficiente saldo

3.  mostrar_saldo() → imprime el saldo actual
"""

#Solución
class CuentaBancaria:
    def __init__ (self, nombre_titular, saldo):
        self.nombre_titular=nombre_titular
        self.__saldo=saldo
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Saldo actual: {self.__saldo}")
        else:
            print("La cantidad debe ser positiva.")


    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.__saldo:
                self.__saldo -= cantidad
                print(f"Retiro exitoso. Saldo actual: {self.__saldo}")
            else:
                print("Fondos insuficientes.")
        else:
            print("La cantidad debe ser positiva.")

    
    def mostrar_saldo(self):
        print(f"Saldo disponible: {self.__saldo}")

#crear Objeto
Primera_Cuenta = CuentaBancaria("Ana", 120.000)

#Depositar dinero
Primera_Cuenta.depositar(25.000)

#Retirar dinero
Primera_Cuenta.retirar(25000)

#Mostrar saldo
Primera_Cuenta.mostrar_saldo()

"""
Usaremos @property (versión más elegante)
"""

#Solución
class CuentaBancaria:
    def __init__ (self, nombre_titular, saldo):
        self.nombre_titular=nombre_titular
        self.__saldo=saldo
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Saldo actual: {self.__saldo}")
        else:
            print("La cantidad debe ser positiva.")


    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.__saldo:
                self.__saldo -= cantidad
                print(f"Retiro exitoso. Saldo actual: {self.__saldo}")
            else:
                print("Fondos insuficientes.")
        else:
            print("La cantidad debe ser positiva.")

    
    @property
    def saldo(self):
        return self.__saldo


#Mostrar Resultado
Primera_Cuenta = CuentaBancaria("Ana", 120000)
print(Primera_Cuenta.saldo)


"""
Ejercicio 2: Clase de estudiantes

Queremos crear una clase llamada Estudiante con:

un atributo público: nombre

un atributo privado: __nota (va de 0 a 100)

un método para mostrar la información

y luego practicaremos el uso de @property
"""

class Estudiantes:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.__nota = nota


    def mostrar_informacion(self):
        print(f"{self.nombre} ha sacado un {self.__nota}")

    @property
    def nota(self):
        return self.__nota

#Mostrar resultados
e1 = Estudiantes("Sofía", 85)
e1.mostrar_informacion()
print(e1.nota)   # usamos @property

"""
Ejercicio 3: Termómetro

Crea una clase Termometro con:

Un atributo privado __temperatura

Un método mostrar_temperatura()

Un método cambiar_temperatura() que solo acepte valores entre -50 y 100 grados.

Usa @property y @temperatura.setter para controlar el acceso.
"""