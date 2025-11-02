"""
Ejercicio 1 — Sistema de Biblioteca

🔹 Tema principal: Herencia + Encapsulamiento + Polimorfismo + Abstracción
🎯 Objetivo: Simular el préstamo y devolución de distintos materiales de una biblioteca.
🧠 Aplicas: atributos privados, métodos heredados, y comportamiento diferente según el tipo de material.

🧾 Enunciado:
Crea un sistema para manejar materiales de una biblioteca.

Crea una clase base Material con los atributos protegidos _titulo, _autor, _disponible.

Métodos comunes:

prestar(): cambia el estado del material a no disponible.

devolver(): lo marca como disponible.

mostrar_info(): método abstracto (debe redefinirse en cada subclase).

Subclases:

Libro → agrega num_paginas

Revista → agrega num_edicion

DVD → agrega duracion

Cada una debe sobrescribir mostrar_info() mostrando sus propios datos.

En el programa principal, crea una lista con distintos materiales y haz que cada uno se muestre y se preste.

💡 Pista: El método mostrar_info() demostrará polimorfismo porque se comporta distinto en cada clase.
"""

class Material:
    def __init__(self, titulo, autor, disponible=True):
        self._titulo = titulo
        self._autor = autor
        self._disponible = disponible

    def prestar(self):
        if not self._disponible:
            return "No está disponible"
        self._disponible = False
        return "Material prestado con éxito"

    def devolver(self):
        if self._disponible:
            return "El material ya está disponible"
        self._disponible = True
        return "Material devuelto con éxito"

    def mostrar_info(self):
        disponibilidad = "Sí" if self._disponible else "No"
        informacion = (
            f"Información disponible del material:\n"
            f"1- Título: {self._titulo}\n"
            f"2- Autor: {self._autor}\n"
            f"3- ¿Está disponible?: {disponibilidad}"
        )
        return informacion

class Libro(Material):
    def __init__(self, titulo, autor, numpaginas, disponible=True):
        super().__init__(titulo, autor, disponible)
        self._numpaginas = numpaginas

    def mostrar_info(self):
        disponibilidad = "Sí" if self._disponible else "No"
        informacion = (
            f"Información disponible del libro:\n"
            f"1- Título: {self._titulo}\n"
            f"2- Autor: {self._autor}\n"
            f"3- Número de páginas: {self._numpaginas}\n"
            f"4- ¿Está disponible?: {disponibilidad}"
        )
        return informacion

class Revista(Material):
    def __init__(self, titulo, autor, numedicion, disponible=True):
        super().__init__(titulo, autor, disponible)
        self._numedicion = numedicion

    def mostrar_info(self):
        disponibilidad = "Sí" if self._disponible else "No"
        informacion = (
            f"Información disponible de la revista:\n"
            f"1- Título: {self._titulo}\n"
            f"2- Autor: {self._autor}\n"
            f"3- Número de edición: {self._numedicion}\n"
            f"4- ¿Está disponible?: {disponibilidad}"
        )
        return informacion

class DVD(Material):
    def __init__(self, titulo, autor, duracion, disponible=True):
        super().__init__(titulo, autor, disponible)
        self._duracion = duracion

    def mostrar_info(self):
        disponibilidad = "Sí" if self._disponible else "No"
        informacion = (
            f"Información disponible del DVD:\n"
            f"1- Título: {self._titulo}\n"
            f"2- Autor: {self._autor}\n"
            f"3- Duración: {self._duracion}\n"
            f"4- ¿Está disponible?: {disponibilidad}"
        )
        return informacion



libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 96)
revista1 = Revista("National Geographic", "Varios autores", 258)
dvd1 = DVD("Interstellar", "Christopher Nolan", 169)

materiales = [libro1, revista1, dvd1]

for m in materiales:
    print(m.mostrar_info())

"""
Ejercicio 2 — “Gestión escolar”
🎯 Conceptos: herencia + encapsulamiento + polimorfismo

Enunciado:
Diseña un sistema donde haya una clase base Persona y tres subclases:

Profesor

Estudiante

Director

Cada una tiene:

Atributos protegidos (_nombre, _edad)

Un método accion() distinto:

El profesor enseña.

El estudiante estudia.

El director supervisa.

🧠 Pista:
Usá un bucle que recorra una lista de objetos (de distintas clases) y llame al mismo método accion() — eso demuestra polimorfismo.
"""

class Persona:
    def __init__(self, nombre,edad):
        self._nombre=nombre
        self._edad=edad
    
    def accion(self):
        return "Esta persona hace algo"
    

class Profesor(Persona):
    def __init__(self, nombre,edad):
        super().__init__(nombre,edad)
    
    def accion(self):
        return "El profesor enseña"

class Estudiante(Persona):
    def __init__(self, nombre,edad):
        super().__init__(nombre,edad)
    
    def accion(self):
        return "El estudiante estudia"

class Director(Persona):
    def __init__(self, nombre,edad):
        super().__init__(nombre,edad)
    
    def accion(self):
        return "El director supervisa"

profesor1=Profesor("Estelle",25)
estudiante1=Estudiante("Ziemann", 15)
director1=Director("Larson",56)

cuerpo=[profesor1,estudiante1,director1]

for x in cuerpo:
    print(x.accion())

"""

Ejercicio 3 — Sistema de Pagos Mejorado (Versión Integrada)

🎯 Objetivo: Extender el sistema base para incluir comisiones, descuentos y validaciones, aplicando los 4 pilares de la POO.

🧾 Enunciado actualizado:

Parte de la clase base MetodoPago que ya tienes (con _monto como atributo protegido).

Agrega validación para que no se permita pagar con montos menores o iguales a 0.

Si el monto es inválido, muestra un mensaje: "Monto no válido para procesar el pago."

Extiende las subclases para que cada método de pago aplique una lógica distinta:

*   Tarjeta → cobra un 5% de comisión adicional.

*   Efectivo → no tiene comisión ni descuento.

*   Cripto → aplica una comisión del 2%.

Crea un método mostrar_total() que indique el total real a pagar después de aplicar la comisión.

Crea una lista con varios tipos de pago y muestra el monto final de cada uno.

*   Pista:

Usa el método procesar_pago() para calcular el monto final según el tipo de pago, y método mostrar_total() para mostrarlo.
Este es el punto donde aplicarás polimorfismo, ya que cada subclase hará su cálculo de forma diferente.

"""

class MetodoPago:
    def __init__(self, monto):
        self._monto = float(monto) if isinstance(monto, str) else monto

    def procesar_pago(self):
        if self._monto <= 0:
            return "Monto no válido para procesar el pago."
        return f"Pago de {self._monto} procesado con éxito."

class Tarjeta(MetodoPago):
    def procesar_pago(self):
        if self._monto <= 0:
            return "Monto no válido para procesar el pago."
        comision = self._monto * 0.05
        total = self._monto + comision
        return f"Pagaste {self._monto} con tarjeta. Se te suma un 5% de comisión ({comision:.2f}). Total: {total:.2f}"

class Efectivo(MetodoPago):
    def procesar_pago(self):
        if self._monto <= 0:
            return "Monto no válido para procesar el pago."
        return f"Pagaste {self._monto} en efectivo. No se te agrega comisiones adicionales. Total: {self._monto:.2f}"

class Cripto(MetodoPago):
    def procesar_pago(self):
        if self._monto <= 0:
            return "Monto no válido para procesar el pago."
        comision = self._monto * 0.02
        total = self._monto + comision
        return f"Pagaste {self._monto} con criptomonedas. Aplica una comisión del 2% ({comision:.2f}). Total: {total:.2f}"


pagos = [
    Tarjeta(500),
    Efectivo(300),
    Cripto(1200)
]

for metodo in pagos:
    print(metodo.procesar_pago())


"""

Ejercicio 4 — “Empleados y bonificaciones PRO”
🎯 Conceptos: herencia múltiple + encapsulamiento + polimorfismo

Enunciado:
Crea un sistema con una clase base Empleado y otra clase Beneficio.

Empleado: tiene _nombre y _salario.

Beneficio: tiene un método calcular_bono() que será redefinido.

Subclases de Empleado:

Gerente

Asistente

Practicante

Cada uno debe calcular un bono distinto, usando la herencia de Beneficio.

🧠 Pista:
Probá heredar de dos clases (Empleado y Beneficio) y sobreescribir el cálculo del bono.
Después imprimí nombre, salario y bono total.

"""

class Empleado:
    def __init__(self, nombre, salario):
        self._nombre = nombre
        self._salario = float(salario) if isinstance(salario, str) else salario

    @property
    def nombre(self):
        return self._nombre

    @property
    def salario(self):
        return self._salario

class Beneficio:
    def calcular_bono(self):
        return 0  

class Gerente(Empleado, Beneficio):
    def calcular_bono(self):
        return self._salario * 0.20
    

class Asistente(Empleado, Beneficio):
    def calcular_bono(self):
        return self._salario * 0.10

class Practicante(Empleado, Beneficio):
    def calcular_bono(self):
        return self._salario * 0.05

# Ejemplo de uso
gerente = Gerente("Ana", 5000)
asistente = Asistente("Luis", 3000)
practicante = Practicante("Carlos", 1500)

# Imprimir resultados
for empleado in [gerente, asistente, practicante]:
    print(f"Nombre: {empleado.nombre}, Salario: ${empleado.salario:.2f}, Bono: ${empleado.calcular_bono():.2f}")


"""
Ejercicio 5— Vehículos Inteligentes

*   Tema principal: Abstracción + Polimorfismo
*   Objetivo: Simular vehículos con comportamientos distintos.
*   Aplicas: clases abstractas, sobreescritura de métodos, atributos compartidos.

*   Enunciado:
Crea una clase abstracta Vehiculo con atributos _marca y _modelo.
Define métodos:

encender(): imprime un mensaje genérico.

acelerar(): método abstracto (cada tipo lo redefine).

Subclases:

Auto: imprime “El auto acelera rápidamente.”

Moto: imprime “La moto acelera con agilidad.”

Bicicleta: imprime “La bicicleta se acelera con pedaleo.”

Guarda varios vehículos en una lista y haz que todos “aceleren” en un bucle.
Esto demostrará polimorfismo en acción.

"""

class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca=marca
        self._modelo=modelo

    def encender(self):
        return "Este vehiculo esta encendido"

    def acelerar(self):
        pass

class Auto(Vehiculo):
    def acelerar(self):
        return "El auto acelera rápidamente."

class Moto(Vehiculo):
    def acelerar(self):
        return "La moto acelera con agilidad."

class Bicicleta(Vehiculo):
    def acelerar(self):
        return "La bicicleta se acelera con pedaleo."

auto1=Auto("Toyota", "Deportivo")
moto1=Moto("Kawasaki","Carreras")
bicicleta1=Bicicleta("Scott","Montaña")

for vehiculos in [auto1,moto1,bicicleta1]:
    print(vehiculos.acelerar())