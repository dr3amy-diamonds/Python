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
6. Pide una palabra y cuenta cuántas vocales tiene.
"""
