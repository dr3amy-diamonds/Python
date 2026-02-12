#Ejercicios de Condicionales

"""
Número positivo o negativo
1. Pide un número e indica si es positivo, negativo o cero.
"""
Numero_Uno = int(input("Digita cualquier número: "))

if Numero_Uno >0:
    print("Número Positivo")
elif Numero_Uno < 0:
    print("Número Negativo")
else:
    print("El número es cero")

"""
Mayor de tres números
2. Pide tres números e imprime cuál es el mayor.
"""

Primer_Numero = int(input("Digita el primer número: "))
Segundo_Numero = int(input("Digita el segundo número: "))
Tercer_Numero = int(input("Digita el tercer número: "))

if Primer_Numero == Segundo_Numero and Segundo_Numero == Tercer_Numero:
    print("Los números son iguales")
elif Primer_Numero >= Segundo_Numero and Primer_Numero >= Tercer_Numero:
    print("El número más grande es:", Primer_Numero)
elif Segundo_Numero >= Primer_Numero and Segundo_Numero >= Tercer_Numero:
    print("El número más grande es:", Segundo_Numero)
else:
    print("El número más grande es:", Tercer_Numero)


"""
Clasificación de edades
3. Según la edad ingresada, imprime:
"""
#Niño (0–11)
#Adolescente (12–17)
#Adulto (18–59)
#Adulto mayor (60 o más)

Edad= int(input("Digite su edad: "))

if Edad >= 0 and Edad <=11:
    print("Eres un niño")
elif Edad >=12 and Edad <= 17:
    print ("Eres un adolescente")
elif Edad >=18 and Edad <=59:
    print("Eres un adulto")
else:
    print("Eres un Adulto Mayor")


"""
Pares e impares
4. Pide un número e indica si es par o impar.
"""
Digitar_Numero = int(input("Digite un número: "))

if Digitar_Numero % 2==0:
    print("Es par")
else:
    print("Es impar")

"""
Notas escolares
5. Pide una nota de 0 a 100 y clasifícala:
"""
# 0–59 → Reprobado
# 60–79 → Aprobado
# 80–89 → Notable
# 90–100 → Excelente

Nota_Escolar = int(input("Digite su nota: "))

if Nota_Escolar >= 0 and Nota_Escolar <=59:
    print("Reprobado")
elif Nota_Escolar  >=60 and Nota_Escolar <= 79:
    print ("Aprobado")
elif Nota_Escolar  >=80 and Nota_Escolar <= 89:
    print("Notable")
elif Nota_Escolar>=90 and Nota_Escolar <=100:
    print("Excelente")
else:
    print("Numero fuera de rango o invalido")

#Bucles: for

"""
Contar del 1 al 10
1. Muestra los números del 1 al 10 con un for.
"""

for Numero in range (1,11):
    print(Numero)

"""
Tabla de multiplicar
2. Pide un número e imprime su tabla de multiplicar del 1 al 10.
"""
Numero_Multiplicar = int(input("Ingresa un número para mostrarte su tabla de multiplicar (del 1 al 10): "))

for x in range(1, 11):
    Numero_total = Numero_Multiplicar * x
    print(f"{Numero_Multiplicar} x {x} = {Numero_total}")
else:
    print("Número no valido")

"""
Suma de los primeros N números
3. Pide un número n y calcula la suma de los números del 1 al n.
"""

Numero_Suma= int(input("Digita el número a sumar: "))
limite = int(input("¿Hasta qué número deseas sumar? "))

for  Numero_Suma in range(limite) :
    Numero_Suma_total= Numero_Suma + limite
    print (f"{Numero_Suma} + {limite} = {Numero_Suma_total}")

"""
Factorial
4. Pide un número y calcula su factorial usando for.
"""

num=int(input("Digita el número: "))
factorial = 1

for x in range(1, num + 1):
    factorial = factorial * x
print(f"El factorial de {num} es {factorial}")

"""
Suma
5. Crea un programa que pida al usuario un número entero y calcule la suma de todos los números desde 1 hasta ese número. El programa debe usar un bucle for para realizar la suma.
"""
numero=int(input("Digita el número: "))

suma=0

for x in range(1, numero +1 ):
    suma= suma + x
print(f"La suma de {numero} es {suma}")

"""
Contar vocales
6. Pide una palabra y cuenta cuántas letras tiene.
"""
Palabra=input("Digita una palabra cualquiera: ")
Contador = 0

for x in Palabra.lower():
    Contador+=1
print((f"La palabra '{Palabra}' tiene {Contador} vocales."))

"""
Escribe un programa en Python que:
7.Pida al usuario que ingrese una palabra.
    Recorra la palabra letra por letra.
    Cuente cuántas vocales (a, e, i, o, u) contiene.
    Finalmente, muestre en pantalla un mensaje con el total de vocales encontradas.
"""

termino = input("Digita una palabra cualquiera: ")
medidor = 0
vocales = ["a", "e", "i", "o", "u"]
for x in termino:
    if x.lower() in vocales:
        medidor += 1
print(f"La palabra '{termino}' tiene {medidor} vocales.")
    

"""
Escribe un programa en Python que:

8. Pida al usuario que escriba una frase.
Cuente cuántas palabras tiene la frase.
Muestre en pantalla el resultado.
"""
Cadena=input("Escribe una frase: ")
calcular=1

for x in Cadena:
    if x == " ":
        calcular +=1
print(f"La frase'{Cadena}' tiene {calcular} palabras.")


#Bucle While

"""
Adivina el número
1. Genera un número secreto (ej. 7) y pide al usuario que lo adivine hasta que acierte.
"""
Numero_Secreto= int(input("Digita un número: "))

while Numero_Secreto!=7:
    print("Sigue intendado")
    Numero_Secreto= int(input("Digita un número: "))
else:
    print("Le diste al clavo")

"""
Contador regresivo
2. Pide un número e imprime un conteo regresivo hasta 0.
"""

pedir_numero=int(input("Digita un número: "))

while pedir_numero:
    pedir_numero=pedir_numero-1
    print("El número es: ", pedir_numero )

"""
Suma hasta que el usuario escriba 0
3. Pide números al usuario y súmalos hasta que escriba 0.
"""
random_number_1 = int(input("Digita el primer número al azar: "))
random_number_2 = int(input("Digita el segundo número al azar: "))

if random_number_1 != 0 and random_number_2 != 0:
    suma_random = random_number_1 + random_number_2
    print(f"La suma de '{random_number_1}' y '{random_number_2}' es '{suma_random}'")
else:
    print("No se puede hacer la suma, uno de los números es 0")

"""
Menú interactivo
4. Crea un menú con opciones (ejemplo: 1. Saludar, 2. Sumar, 3. Salir).
Usa un while para que el menú se repita hasta que el usuario elija salir.
"""

opcion = ""  # Inicializamos la variable

while opcion != "3":   # Se repite hasta que elija salir
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Saludar")
    print("2. Sumar")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("¡Hola! Encantado de saludarte 😊")
    elif opcion == "2":
        a = int(input("Dame el primer número: "))
        b = int(input("Dame el segundo número: "))
        print(f"La suma es: {a + b}")
    elif opcion == "3":
        print("¡Adiós!")
    else:
        print("Opción no válida, intenta otra vez.")

"""
Menú de Figuras Geométricas
5. Crea un programa en Python que muestre un menú con las siguientes opciones:
Calcular el área de un cuadrado.
Calcular el área de un triángulo.
Calcular el área de un círculo.
Salir.
El programa debe repetirse hasta que el usuario elija la opción 4 (Salir).
"""
opcion = ""  # Inicializamos la variable

while opcion != "4":   # Se repite hasta que elija salir
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Calcular el área de un cuadrado")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un círculo")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        lado=float(input("Escribe la longitud del lado:"))
        area=lado * lado
        print(f"El área del cuadrado es {area}")
    elif opcion == "2":
        base = float(input("Digita la base: "))
        altura = float(input("Digita la altura: "))
        area_triagulo= (base * altura)/2
        print(f"El área de un triangulo es {area_triagulo}")
    elif opcion == "3":
        radio=float(input("Escribe el radio del circulo: "))
        A= 3.1416 *(radio**2)
        print(f"El área de un triangulo es {A}")
    elif opcion=="4":
        print("¡Hasta luego! 👋")
    else:
        print("Opción no válida, intenta otra vez.")

"""
Número positivo obligatorio
Pide al usuario un número. Si es negativo, vuelve a pedir hasta que ingrese un número positivo.
"""
numero_pos_neg = int(input("Digita un número: "))

while numero_pos_neg>=0:
    print(f"El número digitado es {numero_pos_neg}")
    numero_pos_neg = int(input("Digita un número: "))
else:
    print(f"Número negativo {numero_pos_neg}")