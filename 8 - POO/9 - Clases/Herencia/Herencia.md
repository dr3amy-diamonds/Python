# Herencia en Python

La herencia en Python es una característica de la **Programación Orientada a Objetos (POO)** que permite que una clase (hija o subclase) herede los atributos y métodos de otra clase (padre o superclase). Esto evita repetir código y facilita la reutilización.

> En palabras sencillas:
> Una clase hija **“hereda”** lo que la clase padre sabe hacer.

---

## ¿Para qué sirve?
- Para **reutilizar código** sin volver a escribirlo.
- Para crear **jerarquías de clases**, como:
  `Animal → Perro → PerroPolicía`.
- Para **especializar comportamientos** (añadir o modificar métodos).

---

## Estructura General

```python
class ClasePadre:
    # Atributos y métodos comunes
    pass

class ClaseHija(ClasePadre):
    # Hereda todo de ClasePadre
    # Puede agregar o modificar métodos
    pass

