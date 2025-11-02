"""
Ejercicio 1: Herencia básica

👉 Objetivo: crear una clase hija que herede del padre sin cambiar nada.

Instrucciones:

Crea una clase Animal con:

un atributo nombre

un método hablar() que solo imprima: "El animal hace un sonido"

Crea una clase hija Perro que herede de Animal.

No agregues nada todavía.

Crea un objeto de tipo Perro y usa el método hablar() heredado.

Pista:
Solo necesitas usar class Perro(Animal): y no repetir el constructor.
"""

class Animal:
    def __init__(self,nombre):
        self.nombre=nombre

    def hablar(self):
        print("El animal hace un sonido")
    
class Perro(Animal):
    pass

p=Perro("Toby")
p.hablar()

"""
Ejercicio 2: Herencia con modificación (sobrescritura)

👉 Objetivo: hacer que la clase hija cambie el comportamiento del método del padre.

Instrucciones:

Usa las clases del ejercicio anterior.

En la clase Perro, agrega su propio método hablar() que imprima:
"Guau! Soy un perro llamado <nombre>".

Crea otro hijo llamado Gato con un método hablar() que imprima:
"Miau! Soy un gato llamado <nombre>".

Pista:
Esto se llama sobrescribir un método (override).
"""



class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("El animal hace un sonido")

class Perro(Animal):
    def hablar(self):
        print(f'Guau! Soy un perro llamado {self.nombre}')

class Gato(Animal):
    def hablar(self):
        print(f'Miau! Soy un gato llamado {self.nombre}')

# Ejemplo de uso:
mi_perro = Perro("Firulais")
mi_gato = Gato("Bigotes")

mi_perro.hablar()
mi_gato.hablar()   


"""
Ejercicio 3: Usar super()

👉 Objetivo: extender el comportamiento del padre sin borrarlo.

Instrucciones:

Crea una clase Vehiculo con:

atributo marca

método mostrar_info() que diga: "Vehículo de marca <marca>"

Crea una clase hija Auto con:

atributo adicional modelo

un nuevo método mostrar_info() que primero llame al del padre (usa super())
y luego imprima "Modelo: <modelo>".
"""

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def mostrar_info(self): 
        print(f'Vehículo de marca {self.marca}')

class Auto(Vehiculo):  
    def __init__(self, marca, modelo):
        super().__init__(marca) 
        self.modelo = modelo

    def mostrar_info(self):
        super().mostrar_info()  
        print(f"Modelo: {self.modelo}")

# Crear objetos
mi_vehiculo = Vehiculo("Mercedes")
mi_auto = Auto("Jeep", "2004")
mi_auto.mostrar_info()

"""
Ejercicio 4: Herencia en cadena

👉 Objetivo: ver cómo una clase puede heredar de otra que ya hereda.

Instrucciones:

Crea tres clases:

SerVivo → método respirar()

Animal hereda de SerVivo → método mover()

Pajaro hereda de Animal → método volar()

Crea un objeto Pajaro y verifica que puede llamar a los tres métodos.
"""

class SerVivo:
    def respirar(self):
        print("Estoy respirando...")

class Animal(SerVivo):
    def mover(self):
        print("Me estoy moviendo...")

class Pajaro(Animal):
    def volar(self):
        print("Estoy volando...")

# Crear un objeto
mi_pajaro = Pajaro()

# Usar los métodos heredados
mi_pajaro.respirar()  
mi_pajaro.mover()     
mi_pajaro.volar()     


"""
Ejercicio 5: Herencia y atributos privados

👉 Objetivo: entender el acceso correcto a atributos privados del padre.

Instrucciones:

Crea una clase Persona con:

atributo privado __edad

método mostrar_edad() que muestre la edad

@property para obtener la edad

Crea una clase Estudiante que herede de Persona.

Agrega atributo curso

Método mostrar_info() que muestre el curso y la edad (usando el getter del padre).
"""

class Persona:
    def __init__(self, edad):
        self.__edad = edad

    def mostrar_edad(self):
        return self.__edad

    @property
    def edad(self):
        return self.__edad

class Estudiante(Persona):
    def __init__(self, edad, curso):
        super().__init__(edad)
        self.curso=curso

    def mostrar_info(self):
        print(f"Información del estudiante\n"
        f"Edad: {self.edad}\n"
        f"Curso: {self.curso}")

Mi_persona=Persona(15)
Mi_Estudiante=Estudiante(25, "Lenguas Extranjeras")

Mi_Estudiante.mostrar_info()


"""
Ejercicio 6 (extra): mezcla práctica

👉 Objetivo: combinar herencia + encapsulamiento + super()
(una mini práctica final)

Instrucciones:

Crea una clase Empleado con:

atributos privados __nombre y __salario

método mostrar_info() que imprima ambos valores

Crea una clase Gerente que herede de Empleado:

agrega atributo departamento

redefine mostrar_info() para mostrar también el departamento
(pero usa super().mostrar_info() para no repetir código)
"""

class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre=nombre
        self.__salario=salario
    
    def mostrar_info(self):
        print(f"Nombre: {self.__nombre}\nSalario: {self.__salario}")

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento=departamento

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Departamento: {self.departamento}")

#Crear objetos e instancias

mi_empleado=Empleado("Tobias", 250)
mi_gerente=Gerente("Caicedo", 800, "Finanzas")
mi_gerente.mostrar_info()


"""
Ejercicio 7: Herencia múltiple

👉 Objetivo: usar más de una clase padre.

Instrucciones:

1. Crea una clase Volador con método volar().
2. Crea una clase Nadador con método nadar().
3. Crea una clase Pato que herede de ambas y tenga método presentarse()
    que diga: "Soy un pato, puedo volar y nadar".
4. Comprueba que el objeto Pato puede llamar a los tres métodos.
"""

class Volador:
    def volar(self):
        return "Puedo volar"

class Nadador:
    def nadar(self):
        return "Puedo nadar"
    

class Pato(Volador, Nadador):
    def presentarse(self):
        print(f'Hola, soy un pato, {self.volar()} y {self.nadar()}')

#Crear objetos

pato=Pato()
pato.volar()
pato.nadar()
pato.presentarse()

"""
Ejercicio 8: Llamadas encadenadas con super()

👉 Objetivo: observar el orden de ejecución en una herencia en cadena.

Instrucciones:

1. Crea tres clases: A, B(A), y C(B).
2. Cada una debe tener un método saludar() que imprima su nombre de clase
    y luego llame a super().saludar().
3. Crea un objeto C y llama a saludar().
4. Observa el orden en que se imprimen los mensajes.
"""

class A:
    def saludar(self):
        print("Hola soy la Clase A")

class B(A):
    def saludar (self):
        super().saludar()
        print("Hola, Soy la clase B")

class C(B):
    def saludar(self):
        super().saludar()
        print( "Hola, soy la clase C")

obj = C()
obj.saludar()
