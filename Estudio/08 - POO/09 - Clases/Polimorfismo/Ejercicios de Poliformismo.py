#Nivel 1 — Básico

"""
Ejercicio 1: “Sonidos de animales”

Crea una clase base llamada Animal con un método sonido().
Luego, crea tres clases hijas (Perro, Gato y Vaca) que sobrescriban ese método con diferentes mensajes.
Finalmente, guarda los objetos en una lista y muestra sus sonidos en un bucle.
"""

class Animal:
    def sonido(self):
        return "Este animal emite un sonido"
class Perro(Animal):
    def sonido(self):
        return "Este Perro emite un sonido: ¡GUAU!"
class Gato(Animal):
    def sonido(self):
        return "Este gato emite un sonido: ¡MIAU!"
class Vaca(Animal):
    def sonido(self):
        return "Esta vaca emite un sonido: ¡MUUUU!"

animales = [Vaca(), Gato(), Perro(),Animal()]

for a in animales:
    print(a.sonido())


"""
Ejercicio 2: “Acciones de personajes”

Crea tres clases (Guerrero, Mago, Arquero) y en cada una define un método llamado atacar().
Cada clase debe imprimir una forma distinta de ataque.
Después, crea una lista con distintos personajes y haz que todos ataquen en un bucle.
"""

class Guerrero:
    def atacar(self):
        return "Atacar con Espada"
class Mago:
    def atacar(self):
        return "Atacar con hechizos"
class Arquero:
    def atacar(self):
        return "Defender porteria"

ataques = [Guerrero(), Mago(),Arquero()]

for combatientes in ataques:
    print(combatientes.atacar())


"""
Ejercicio 3: “Notificaciones”

Diseña un sistema de notificaciones con una clase base Notificacion y tres subclases:

Email

SMS

Push
Cada una debe tener un método enviar(mensaje) que muestre un texto distinto al enviar el mensaje.
"""

class Notificacion:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def enviar(self):
        print("Enviando notificación genérica...")

class Email(Notificacion):
    def enviar(self):
        print(f" Enviando email: {self.mensaje}")
class SMS(Notificacion):
    def enviar(self):
        print(f" Enviando SMS: {self.mensaje}")
class Push(Notificacion):
    def enviar(self):
        print(f" Enviando Push: {self.mensaje}")

#Creación de objetos

#Email
aviso_email = Email("Hola")
aviso_email.enviar()

#SMS
aviso_sms=SMS("Hola Mundo")
aviso_sms.enviar()

#Push
aviso_push=Push("¡HOLA!")
aviso_push.enviar()


#Nivel 2 — Intermedio

"""
Ejercicio 4: “Tipos de transporte”

Crea una clase base Transporte con un método moverse().
Luego crea clases hijas como Auto, Barco, y Avion, que sobrescriban ese método con mensajes diferentes.
Guarda varios tipos en una lista y muestra cómo se mueve cada uno.
"""

class Transporte:
    def moverse(self):
        return "Se está moviendo"

class Auto(Transporte):
    def moverse(self):
        return "El auto se está acelerando"

class Barco(Transporte):
    def moverse(self):
        return "El barco está navegando"

class Avion(Transporte):
    def moverse(self):
        return "El avión está volando"


Transportes = [Transporte(),Auto(), Barco(),Avion()]

for movimiento in Transportes:
    print(movimiento.moverse())

"""
Ejercicio 5: “Calculadora de áreas”

Crea una clase base Figura con un método area().
Luego crea tres clases hijas:

*   Rectangulo → recibe base y altura

*   Circulo → recibe radio

*   Triangulo → recibe base y altura

Cada clase debe calcular su área con su fórmula correspondiente.
Crea una lista con objetos de distintas figuras y muestra sus áreas en pantalla.
"""

class Figura:
    def area(self):
        pass

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
    
    def area(self):
        area=self.base*self.altura
        return area

class Circulo(Figura):
    def __init__(self,radio):
        self.radio=radio
    
    def area(self):
        area=3.14*(self.radio)**2
        return area

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
    
    def area(self):
        area=(self.base*self.altura)/2
        return area


#Creación de lista
Areas_Geometricas = [Rectangulo(10,2),Circulo(3.15),Triangulo(25,10)]

for Figuras_Geometricas in Areas_Geometricas:
    print(f"El área es: {Figuras_Geometricas.area()}")


"""
Ejercicio 6: “Sistema de pagos”

Crea una clase base MetodoPago con un método pagar(cantidad).
Luego, crea tres clases hijas:

*   Tarjeta

*   Efectivo

*   Cripto

Cada una debe imprimir un mensaje diferente al realizar un pago.
Simula varios pagos con distintos métodos.
"""

class MetodoPago:
    def __init__(self,cantidad):
        self.cantidad=cantidad

    def pagar(self):
        pass

class Tarjeta(MetodoPago):
    def pagar(self):
        mensaje= f"Has pagado {self.cantidad} con tarjeta"
        return mensaje

class Efectivo(MetodoPago):
    def pagar(self):
        mensaje= f"Has pagado {self.cantidad} con efectivo"
        return mensaje

class Cripto(MetodoPago):
    def pagar(self):
        mensaje= f"Has pagado {self.cantidad} con Cripto"
        return mensaje

#Creación de lista
Formas_Pago = [Tarjeta(1200),Efectivo(1500),Cripto(3000)]

for Pagos in Formas_Pago:
    print(Pagos.pagar())


#Nivel 3 — Avanzado (lógica más real)

"""
Ejercicio 7: “Empleados y bonificaciones”

Crea una clase Empleado con un método calcular_bono().
Luego, crea subclases:

*   Gerente: el bono es el 20% del salario.

*   Asistente: el bono es el 10%.

*   Practicante: el bono es 5%.

Crea una lista de empleados y muestra cuánto gana cada uno con su bono incluido.
"""

class Empleado:
    def __init__(self, saldo):
        self.saldo=saldo

    def calcular_bono(self, porcentaje):
        return self.saldo * (porcentaje / 100)

class Gerente(Empleado):
    def calcular_bono(self):
        bono = super().calcular_bono(20)
        return f"El pago del gerente más su bono es de: {self.saldo + bono}"

class Asistente(Empleado):
    def calcular_bono(self):
        bono= super().calcular_bono(10)
        return f"El pago del asistente más su bono es de: {self.saldo + bono}"

class Practicante(Empleado):
    def calcular_bono(self):
        bono = super().calcular_bono(5)
        return f"El pago del practicante más su bono es de: {self.saldo + bono}"

Empleados=[Gerente(5000000), Asistente(4000000), Practicante(1700000)]

for Empresas in Empleados:
    print(Empresas.calcular_bono())


"""
Ejercicio 8: “Instrumentos musicales”

Crea una clase Instrumento con un método tocar().
Luego crea varias clases (Piano, Guitarra, Batería, Flauta) que sobrescriban ese método.
Crea una lista con varios instrumentos y haz que “toquen” todos.

"""

class Instrumento:
    def tocar(self):
        pass

class Piano (Instrumento):
    def tocar(self):
        return "El piano se esta tocando"

class Guitarra (Instrumento):
    def tocar(self):
        return "La guitarra se esta tocando"

class Bateria (Instrumento):
    def tocar(self):
        return "La bateria se esta tocando"

class Flauta (Instrumento):
    def tocar(self):
        return "La flauta se esta tocando"

intrumentos = [Piano(),Guitarra(), Bateria(),Flauta()]

for intrumentos_Musicales in intrumentos:
    print(intrumentos_Musicales.tocar())


"""
Ejercicio 9: “Dispositivos electrónicos”

Crea una clase Dispositivo con un método encender().
Luego crea subclases:

*   Computadora

*   Teléfono

*   Televisor

Cada una debe imprimir su forma particular de encenderse.
Usa una lista para recorrer los dispositivos y mostrar su comportamiento.
"""

class dispositivos:
    def encender(self):
        pass

class Computadora(dispositivos):
    def encender(self):
        return "La computadora se ha encendido"

class Telefono(dispositivos):
    def encender(self):
        return"El telefono se ha encendido"

class Televisor(dispositivos):
    def encender(self):
        return "El televisor se ha encendido"
    
Dispositivo =[Computadora(),Telefono(),Televisor()]

for Dispositivo_Electronicos in Dispositivo:
    print(Dispositivo_Electronicos.encender())


"""
Ejercicio 10: “Personas en una escuela”

Crea una clase base Persona con un método accion().
Luego crea:

*   Profesor: imprime “enseña una clase”.

*   Estudiante: imprime “estudia y hace tareas”.

*   Director: imprime “supervisa la escuela”.

Crea una lista con distintas personas y haz que cada una realice su acción
"""

class Persona:
    def accion(self):
        pass

class Profesor (Persona):
    def accion(self):
        return "enseña una clase"

class Estudiante (Persona):
    def accion(self):
        return "estudia y hace tareas"

class Director (Persona):
    def accion(self):
        return "supervisa la escuela"

Escuela = [Profesor(), Estudiante(), Director()]

for x in Escuela:
    print(x.accion())