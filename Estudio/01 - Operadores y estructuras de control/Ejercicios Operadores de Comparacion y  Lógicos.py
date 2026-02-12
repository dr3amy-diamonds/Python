#Ejercicios de Operadores de Comparación
"""Mayor de dos números
1. Escribe un programa que pida dos números e imprima si el primero es mayor, menor o igual al segundo.
"""
Numero_1=float(input("Digite el primer número: "))
Numero_2=float(input("Digite el segundo número: "))

if Numero_1 < Numero_2:
    print(Numero_1)
elif Numero_1 == Numero_2:
    print("Números iguales")
else:
    print("Número mayor que ", +Numero_2)

"""
Edad mínima
2. Pide la edad de un usuario y determina si puede votar (≥ 18 años).
"""

Edad=int(input("Digita tu edad: "))

if Edad >=18:
    print("Eres Mayor de edad. Puedes Votar")
else:
    print("No eres mayor de edad. No puedes votar")

"""
Contraseña correcta
3. Crea una variable clave = "python123".
Pide al usuario que ingrese una contraseña y verifica si es correcta.
"""

Contrasena=input("Digita tu contraseña: ")

if Contrasena == "python123":
    print("¡CONTRASEÑA CORRECTA!")
else:
    print("¡CONTRASEÑA INCORRECTA!")

"""
Número dentro de un rango
4. Pregunta un número y comprueba si está entre 1 y 10 (inclusive).
"""

Comprobar = int(input("Tipea un número: "))

if Comprobar <= 10:
    print("Número dentro del rango")
else:
    print("Número fuera del rango")


"""
Comparación de strings
5. Pide dos palabras e indica si son iguales o diferentes.
"""

Palabra_Uno = input("Digita cualquier cosa: ")
Palabra_Dos = input("Digita cualquier cosa: ")

if Palabra_Uno == Palabra_Dos:
    print("Son Iguales")
else:
    print("Son diferentes")

########################################################################################################################################################################

#Ejercicios de Operadores de Comparación
"""
Año bisiesto (simplificado)
1. Un año es bisiesto si es divisible por 4 y no por 100, o si es divisible por 400.
Pide un año y determina si lo es.
"""

Ano = int(input("Digita un año cualquiera"))

if Ano%4 == 0 or Ano % 400==0:
    print("Es Bisiesto")
else:
    print("No es Bisiesto")

"""
Acceso a descuento
2. Pregunta la edad y si es estudiante (True/False).
El descuento se aplica si la edad es menor a 18 o si es estudiante.
"""

Edad_Dos= int(input("Digite su edad: "))
Pregunta_Uno = input("¿Eres Estudiante?: ").lower()

if Edad_Dos <18 or Pregunta_Uno in  ["Sí", "Si","sí","si"]:
    print("Aplicas a Descuento. ¡FELICITACIONES!")
else:
    print("¡No aplicas al Descuento!")


"""
Acceso a un sitio
3. Para entrar a un sitio se necesita:
Ser mayor de 18 años
Y tener una invitación
Pide los datos y valida si la persona puede entrar.
"""

Edad_Tres = int(input("Digite su edad: "))
Inivitacion = input("¿Tienes invitación? ").lower()
Pass = input("Digita la contraseña: ")

if Edad_Tres >= 18 and Inivitacion in ["Sí", "Si","sí","si"] and Pass=="123456":
    print("Puedes Entrar")
else:
    print("No puedes entrar")

"""
Número par y múltiplo de 5
4. Pregunta un número y verifica si es par y también múltiplo de 5.
"""

Multiplos =  int(input("Digita un número: "))

if Multiplos % 2 == 0 and Multiplos % 5 == 0:
    print ("¡Es par y múltiplo de 5!")
elif Multiplos % 2 != 0 or Multiplos % 5 == 0:
    print("No es par pero sí es multiplo de 5")
else:
    ("¡No es para ni multiplo de 5!")

"""
Usuario y contraseña
5. Define:
usuario = "admin"
contrasena = "1234"
Pide al usuario ingresar sus credenciales y comprueba si puede iniciar sesión.
"""

Usuario = "admi"
Password = "1234"

Usuario_uno = input("Introduce el usuario: ")
Pass_Word = input("Introduce Contraseña: ")

if Usuario_uno == Usuario and Pass_Word == Password:
    print("Credenciales correctas. Bienvenido/a")
else:
    print("Credenciales incorrectas. Vuelva a intentar")

