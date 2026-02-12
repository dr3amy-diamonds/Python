"""
Abstracción

La abstracción es el principio de ocultar los detalles innecesarios y mostrar solo lo importante de un objeto.
En la práctica: cuando programamos, no nos interesa cómo funciona internamente todo, sino qué hace y cómo lo podemos usar.
"""

#Ejemplo 1
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def arrancar(self):
        print("El coche está arrancando...")

# Uso
mi_coche = Coche("Toyota", "Corolla")
mi_coche.arrancar()

#Ejemplo 2
class Cajero:
    def __init__(self, saldo):
        self.saldo = saldo 

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiraste {cantidad} pesos")
        else:
            print("Saldo insuficiente")

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depositaste {cantidad} pesos")

    def saldo_disponible(self):
        return self.saldo

# Uso
cajero = Cajero(1000)
cajero.depositar(500)
print("Saldo actual:", cajero.saldo_disponible())
cajero.retirar(300)


