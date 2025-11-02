# Clases en Python

Una **clase** es una plantilla o plano para crear objetos, actuando como
un molde que define las propiedades (*atributos*) y los comportamientos
(*métodos*) que tendrán todos los objetos de ese tipo.

Los **objetos** son instancias concretas de una clase, y cada objeto
puede tener sus propios valores para los atributos, pero comparte los
métodos y la estructura básica de la clase de la que proviene.

Las clases son una característica fundamental de la **Programación
Orientada a Objetos (POO)** y permiten organizar y estructurar el código
de manera eficiente.

------------------------------------------------------------------------

## Crear una clase vacía

``` python
# Crear una clase vacía
class MiClase:
    pass  # 'pass' significa "no hacer nada" (clase vacía)
```

------------------------------------------------------------------------

## Atributos de clase y constructor

-   **Atributos de clase**: valores compartidos por todos los objetos.\
-   **Constructor (`__init__`)**: método especial que se ejecuta al
    crear un objeto y sirve para inicializar sus atributos.

``` python
class MiClase:
    atributo1 = "valor1"   # atributo de clase
    atributo2 = "valor2"   # atributo de clase

    def __init__(self, argumento1):  # constructor
        self.argumento1 = argumento1  # atributo de instancia
```

------------------------------------------------------------------------

## Añadir métodos

-   **Métodos** son funciones dentro de una clase.\
-   Siempre llevan **self** como primer parámetro (representa al objeto
    en sí).

``` python
class MiClase:
    atributo1 = "valor1"
    atributo2 = "valor2"

    def __init__(self, argumento1):
        self.argumento1 = argumento1

    def funcion1(self):
        print("Esta es la función 1")
```

------------------------------------------------------------------------

## Crear objetos (instancias)

``` python
# Crear objetos (instancias)
mi_objeto = MiClase("Hola")  # se llama al constructor
```

------------------------------------------------------------------------

## Acceder a atributos y métodos

``` python
print(mi_objeto.atributo1)    # valor1
print(mi_objeto.atributo2)    # valor2
print(mi_objeto.argumento1)   # Hola

mi_objeto.funcion1()          # Esta es la función 1
```

------------------------------------------------------------------------

## Ejecución en consola (bash)

``` bash
$ python3 main.py
valor1
valor2
Hola
Esta es la función 1
```
