"""
Ejercicio 1 — Sistema de Biblioteca

🔹 Tema principal: Herencia + Encapsulamiento + Polimorfismo + Abstracción
🎯 Objetivo: Simular el préstamo y devolución de distintos materiales de una biblioteca.
🧠 Aplicas: atributos privados, métodos heredados, y comportamiento diferente según el tipo de material.

🧾 Enunciado:
Crea un sistema para manejar materiales de una biblioteca.

Crea una clase base Material con los atributos privados _titulo, _autor, _disponible.

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
    def __init__ (self,titulo,autor, disponible):
        self.__titulo=titulo
        self.__autor=autor
        self.__disponible=True
    
    def prestar(self):
        pass