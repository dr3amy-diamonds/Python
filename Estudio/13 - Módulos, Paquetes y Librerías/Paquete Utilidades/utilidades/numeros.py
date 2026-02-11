def es_par():
    try:
        numero = int(input("Ingrese un número entero: ").strip())
        if numero % 2 == 0:
            print(f"{numero} es par.")
        else:
            print(f"{numero} es impar.")
    except ValueError:
        return "Error: Debe ingresar un número entero válido."

