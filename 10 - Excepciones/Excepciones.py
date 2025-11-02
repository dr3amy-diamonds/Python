"""
| Bloque                     | Uso principal            | Ejemplo típico                |
| -------------------------- | ------------------------ | ----------------------------- |
| `try`                      | Código que podría fallar | abrir un archivo              |
| `except`                   | Capturar error           | `except ValueError:`          |
| `else`                     | Si no hubo error         | mostrar resultado             |
| `finally`                  | Siempre se ejecuta       | cerrar archivo o conexión     |
| `raise`                    | Lanzar error a propósito | `raise ValueError("mensaje")` |
| Excepciones personalizadas | Casos de negocio         | `class ErrorSaldo(Exception)` |

"""


#Ejemplo 1: Evitar que el programa se detenga por un error de tipo

try:
    numero = int(input("Ingresa un número: "))
    resultado = 100 / numero
    print(f"El resultado es {resultado}")
except ValueError:
    print("❌ Error: Debes ingresar un número, no texto.")
except ZeroDivisionError:
    print("❌ Error: No puedes dividir entre 0.")

"""
Explicación:

*   Si escribes texto → se lanza ValueError.

*   Si pones 0 → se lanza ZeroDivisionError.

*   Si todo va bien, se muestra el resultado.
        Esto evita que el programa “reviente” por un error del usuario.
"""

#Ejemplo 2 — Bloques else y finally

try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
else:
    print(f"Todo salió bien. El resultado es {resultado}")
finally:
    print("Fin del programa (este bloque siempre se ejecuta).")

"""
Explicación:

*   else → solo se ejecuta si no hubo error.

*   finally → siempre se ejecuta, haya error o no (ideal para cerrar archivos, conexiones, etc.).
"""

#Ejemplo 3 - Excepciones personalizadas (raise)

def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    elif edad > 120:
        raise ValueError("La edad no puede ser tan alta.")
    else:
        print("Edad válida ✅")

try:
    edad = int(input("Ingresa tu edad: "))
    validar_edad(edad)
except ValueError as e:
    print(f"Error: {e}")

"""
Explicación:

*   raise lanza un error a propósito si se cumple cierta condición.

*   Lo usamos para validar datos.

*   as e captura el mensaje del error y lo imprime.
"""

#Ejemplo 4 — Crear tus propias clases de excepciones

class EdadInvalidaError(Exception):
    """Excepción personalizada para edades inválidas."""
    pass

def registrar_usuario(edad):
    if edad < 0 or edad > 120:
        raise EdadInvalidaError("Edad fuera del rango permitido.")
    print("Usuario registrado con éxito ✅")

try:
    registrar_usuario(-5)
except EdadInvalidaError as e:
    print(f"⚠️ Error de registro: {e}")

"""
Explicación:

*   Creamos una clase que hereda de Exception.

*   Podemos usarla para casos específicos (por ejemplo, “edad inválida”, “saldo insuficiente”).

*   Sirve para organizar errores grandes o sistemas complejos.
"""

#Ejemplo 5 — Excepciones con archivos

try:
    with open("datos.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("❌ El archivo no existe.")
except PermissionError:
    print("❌ No tienes permiso para leer este archivo.")
finally:
    print("📂 Operación de archivo finalizada.")


"""
Explicación:

*   FileNotFoundError → el archivo no existe.

*   PermissionError → el archivo existe, pero no tienes permiso.

*   finally se usa para cerrar o limpiar recursos.
"""

#Ejemplo 6 — Excepciones en POO (con clases)

class FondosInsuficientesError(Exception):
    pass

class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise FondosInsuficientesError("Saldo insuficiente para realizar la operación.")
        self.saldo -= cantidad
        print(f"✅ Retiraste {cantidad}. Saldo restante: {self.saldo}")

try:
    cuenta = CuentaBancaria(1000)
    cuenta.retirar(1500)
except FondosInsuficientesError as e:
    print(f"⚠️ Error: {e}")

"""
Explicación:

*   Se usa una excepción personalizada para un caso concreto de negocio.

*   Esto separa la lógica del error del resto del código.

*   Es una práctica profesional y muy común en sistemas financieros o empresariales.

"""

#Ejemplo 7 — Excepciones combinadas y anidadas

def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("❌ No puedes dividir entre cero.")
    except TypeError:
        print("❌ Ambos valores deben ser números.")
    else:
        print(f"✅ Resultado: {resultado}")
    finally:
        print("🧮 Operación completada.")

dividir(10, 2)
dividir(10, 0)
dividir("10", 2)


"""
Explicación:

*   Puedes manejar varios tipos de error en la misma función.

*   else y finally organizan mejor el flujo.

*   Evitas usar try dentro de try (que se vuelve difícil de leer).

"""

#Ejemplo 8 — Ejemplo realista: Sistema de biblioteca con excepciones

class NoDisponibleError(Exception):
    pass

class Material:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponible = True

    def prestar(self):
        if not self.disponible:
            raise NoDisponibleError(f"'{self.titulo}' no está disponible.")
        self.disponible = False
        print(f"📚 Has prestado '{self.titulo}'.")

    def devolver(self):
        self.disponible = True
        print(f"🔁 Has devuelto '{self.titulo}'.")

try:
    libro = Material("El Principito")
    libro.prestar()
    libro.prestar()  # Intento de nuevo → error
except NoDisponibleError as e:
    print(f"⚠️ Error: {e}")
finally:
    print("✅ Fin del proceso de préstamo.")

"""
Explicación:

*   Si alguien intenta prestar el mismo libro dos veces, el programa lanza una excepción personalizada.

*   Esto protege la lógica de negocio.

*   finally asegura que el programa no se interrumpe.
"""
