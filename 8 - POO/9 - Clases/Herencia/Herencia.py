"""
Herencia

Es unmecanismo de la programación orientada a objetos que permite que una clase (la subclase) herede atributos y métodos de otra clase (la superclase).

"""

#Ejemplo: Herencia simple
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")


# Clase Hija
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        # Usamos super() para llamar al constructor de Persona
        super().__init__(nombre, edad)
        self.carrera = carrera

    def estudiar(self):
        print(f"{self.nombre} está estudiando {self.carrera}.")


# Crear objetos
p1 = Persona("Lucía", 30)
p1.presentarse()

e1 = Estudiante("Mateo", 20, "Ingeniería")
e1.presentarse()     # Heredado de Persona
e1.estudiar()        # Propio de Estudiante


#Ejemplo: Sobrescritura de métodos
class Persona:
    def hablar(self):
        print("Hola, soy una persona.")

class Profesor(Persona):
    def hablar(self):
        print("Hola, soy un profesor dando clase.")


p = Persona()
p.hablar()

prof = Profesor()
prof.hablar()   


#Ejemplo 3: Caso Básico

# Clase padre
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("El animal hace un sonido genérico.")
    

# Clase hija (hereda de Animal)
class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau guau!")


# Crear objetos
a = Animal("Animalito")
a.hacer_sonido()

p = Perro("Toby")
p.hacer_sonido()

"""
*   La clase Perro hereda el método __init__ de Animal, así no lo repite.

*   Perro redefine (sobrescribe) el método hacer_sonido() con su propia versión.

*   Se usa super() solo cuando necesitas extender la funcionalidad del padre (aquí no fue necesario).
"""

#Ejemplo 4: Lo que NO debes hacer — duplicar código del padre

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    def __init__(self, nombre):
        # ❌ Esto repite el código del padre
        self.nombre = nombre

"""
Problema:

*   Si en el futuro Animal cambia su constructor, tendrás que actualizar todos los hijos.

Mejor usar:
"""

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)   # ✅ Llama al constructor del padre



#Agregar cosas nuevas sin romper lo heredado
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def mover(self):
        print(f"{self.nombre} se está moviendo.")

class Pajaro(Animal):
    def __init__(self, nombre, puede_volar=True):
        super().__init__(nombre)
        self.puede_volar = puede_volar

    def mover(self):
        if self.puede_volar:
            print(f"{self.nombre} vuela por el cielo.")
        else:
            super().mover()

"""
*   Pajaro amplía la funcionalidad del método mover(), pero no borra el comportamiento original.

*   Gracias a super().mover(), sigue teniendo acceso al código de Animal.
"""

"""
Esto se llama herencia en cadena.
Cada clase hija puede acceder a todo lo heredado desde sus ancestros.
"""

#Ejemplo 5: Herencia en cadena
class SerVivo:
    def respirar(self):
        print("Estoy respirando...")

class Animal(SerVivo):
    def comer(self):
        print("Estoy comiendo...")

class Gato(Animal):
    def maullar(self):
        print("Miau~")


g = Gato()
g.respirar()  # Heredado de SerVivo
g.comer()     # Heredado de Animal
g.maullar()   # Propio de Gato


#Ejemplo 6: Error común — intentar acceder a algo privado del padre
class Persona:
    def __init__(self, nombre, edad):
        self.__edad = edad   # atributo privado
        self.nombre = nombre

class Estudiante(Persona):
    def mostrar_edad(self):
        print(self.__edad)  # ❌ Error: no puede acceder directamente. Da error porque esta encapsulado

#Solución correcta
class Persona:
    def __init__(self, nombre, edad):
        self.__edad = edad
        self.nombre = nombre

    @property
    def edad(self):
        return self.__edad

class Estudiante(Persona):
    def mostrar_edad(self):
        print(self.edad)  # ✅ Usa el getter del padre


"""
| ✅ Haz esto                                                       | ❌ No hagas esto                                             |
| ---------------------------------------------------------------- | ----------------------------------------------------------- |
| Usa `super()` para no repetir código del padre                   | Repetir el mismo `__init__` o métodos del padre             |
| Usa `@property` si necesitas acceder a datos privados del padre  | Acceder directamente a atributos `__privados`               |
| Redefine métodos **solo si necesitas cambiar su comportamiento** | Sobrescribir sin necesidad (rompe la lógica del padre)      |
| Extiende el comportamiento del padre con `super().metodo()`      | Reescribir todo sin llamar al padre cuando aún lo necesitas |

"""