import math

def area_circulo():
    radio=float(input("Introduce el radio: \n"))
    calcular_area=math.pi * (radio ** 2)
    print(f"El área del círculo con radio {radio} es: {calcular_area}")

def raiz_cuadrada():
    try:
        numero=float(input("Introduce la raiz cuadrada: \n"))
        resultado = math.sqrt(numero)
        print(f"La raíz cuadrada de {numero} es: {resultado}")
    except ValueError:
        # Este bloque se ejecuta si se introduce un número negativo
        print("Error: No se puede calcular la raíz cuadrada real de un número negativo.")
        print("Por favor, introduce un número positivo.")

area_circulo()
raiz_cuadrada()
