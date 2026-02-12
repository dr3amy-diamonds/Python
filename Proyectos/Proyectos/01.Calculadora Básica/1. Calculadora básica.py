while True:
    print("\nCalculadora de Operaciones Básicas")
    print("1. Sumar")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Exponenciación")
    print("6. Módulo")
    print("7. Salir")
    opciones = int(input("Introduce la operación que quieres usar: "))


    match opciones:
        case 1:
            num1=float(input("Introduce un número: "))
            num2=float(input("Introduce otro número: "))
            suma_total=num1+num2
            print(f"la suma de {num1} y  {num2} es {suma_total} ")
            break
        case 2:
            num1=float(input("Introduce un número: "))
            num2=float(input("Introduce otro número: "))
            resta_total=num1-num2
            print(f"la resta de {num1} y  {num2} es {resta_total} ")
            break
        case 3:
            num1=float(input("Introduce un número: "))
            num2=float(input("Introduce otro número: "))
            multiplicacion_total=num1*num2
            print(f"la multiplicación de {num1} y  {num2} es {multiplicacion_total} ")
            break
        case 4:
            try:
                num1=float(input("Introduce un número: "))
                num2=float(input("Introduce otro número: "))
                division_total=num1/num2
                print(f"la division de {num1} y  {num2} es {division_total} ")
            except ZeroDivisionError:
                print("No puedes dividir entre cero, vuelve a intentarlo")
            break
        case 5:
            num1=float(input("Introduce un número: "))
            num2=float(input("Introduce otro número: "))
            potencia=num1**num2
            print(f"la potencia de {num1} y  {num2} es {potencia} ")
            break
        case 6:
            num1=float(input("Introduce un número: "))
            num2=float(input("Introduce otro número: "))
            modulacion=num1/num2
            print(f"la modulación de {num1} y  {num2} es {modulacion} ")
            break
        case 7:
            print("Hasta Luego!")
            break
    break

