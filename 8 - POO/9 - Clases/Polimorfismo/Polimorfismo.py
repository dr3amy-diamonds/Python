#Ejemplo 1 Polimorfismo entre clases distintas

class Perro:
    def hablar(self):
        return "Guau!"

class Gato:
    def hablar(self):
        return "Miau!"

# Polimorfismo en acción
animales = [Perro(), Gato()]

for animal in animales:
    print(animal.hablar())


#Ejemplo 2 con herencia 
class Animal:
    def hablar(self):
        return "El animal hace un sonido."

class Perro(Animal):
    def hablar(self):
        return "Guau!"

class Gato(Animal):
    def hablar(self):
        return "Miau!"

animales = [Perro(), Gato(), Animal()]

for a in animales:
    print(a.hablar())



#Ejemplo 3 Formas Geometricas
class Forma:
    def area(self):
        pass  # método "vacío" para que las hijas lo definan

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return 3.14 * self.radio ** 2

formas = [Cuadrado(5), Circulo(3)]

for f in formas:
    print(f.area())
