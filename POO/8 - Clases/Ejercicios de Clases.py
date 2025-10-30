"""

Ejercicio 1:
Crea una clase llamada Persona que tenga los atributos nombre y edad, y un método llamado saludar que imprima un saludo con el nombre de la persona.
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Ejemplo de uso
persona1 = Persona("Emilia", 30)
persona1.saludar()


"""
Ejercicio 2:
Crea una clase llamada Rectangulo que tenga los atributos base y altura. Incluye un método llamado calcular_area que devuelva el área del rectángulo.
"""

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

# Ejemplo de uso
rectangulo1 = Rectangulo(5, 10)
print(f"El área del rectángulo es: {rectangulo1.calcular_area()}")


"""
Ejercicio 3:
Crea una clase llamada CuentaBancaria con los atributos titular y saldo. Incluye los métodos depositar y retirar para modificar el saldo
"""

class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se depositaron {cantidad} unidades. Saldo actual: {self.saldo}")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se retiraron {cantidad} unidades. Saldo actual: {self.saldo}")
        else:
            print("Saldo insuficiente.")

# Ejemplo de uso
cuenta1 = CuentaBancaria("Emilia", 1000)
cuenta1.depositar(500)
cuenta1.retirar(200)



"""
Ejercicio 4:
Crea una clase Estudiante que herede de Persona y añade un atributo carrera. Incluye un método estudiar que imprima un mensaje relacionado con la carrera.
"""

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def estudiar(self):
        print(f"{self.nombre} está estudiando {self.carrera}.")

# Ejemplo de uso
estudiante1 = Estudiante("Ana", 20, "Ingeniería")
estudiante1.saludar()
estudiante1.estudiar()


"""
Ejercicio 5:
Crea una clase Coche con los atributos privados __modelo y __velocidad. Usa métodos públicos (get_modelo, acelerar, frenar) para acceder y modificar estos atributos.
"""

class Coche:
    def __init__(self, modelo):
        self.__modelo = modelo
        self.__velocidad = 0

    def get_modelo(self):
        return self.__modelo

    def acelerar(self, incrementar):
        self.__velocidad += incrementar
        print(f"Velocidad actual: {self.__velocidad} km/h")

    def frenar(self, disminuir):
        self.__velocidad -= disminuir
        print(f"Velocidad actual: {self.__velocidad} km/h")

# Ejemplo de uso
coche1 = Coche("Toyota")
print(f"Modelo: {coche1.get_modelo()}")
coche1.acelerar(50)
coche1.frenar(20)




