"""
Crea un programa que analice dos palabras diferentes y realice comprobaciones
para descubrir si son:
Palíndromos
Anagramas
Isogramas
"""

def palabras():
    # Funciones para cada una
    def es_palindromo():
        def palindromos(palabra_polindromo):
            palabra_polindromo = ''.join(palabra_polindromo.lower().split())
            return palabra_polindromo == palabra_polindromo[::-1]

        def confirmacion():
            palabra_palindromo_uno = input("Digita una palabra: ")
            if palindromos(palabra_palindromo_uno):
                print(f"'{palabra_palindromo_uno}' es un palíndromo")
            else:
                print(f"'{palabra_palindromo_uno}' no es un palíndromo")
        return confirmacion()

    def es_anagrama():
        def Anagrama(palabra_a, palabra_b):
            # 1. Normalizar las cadenas (ej: a minúsculas)
            palabra_a = palabra_a.lower()
            palabra_b = palabra_b.lower()

            # 2. Verificar que tengan la misma longitud
            if len(palabra_a) != len(palabra_b):
                return False

            # 3. Ordenar las letras y comparar
            return sorted(palabra_a) == sorted(palabra_b)

        def confirmacion():
            palabra_a = input("Digita una palabraa: ")
            palabra_b = input("Digita otra palabra: ")

            if Anagrama(palabra_a, palabra_b):
                print(f"'{palabra_a}' y '{palabra_b}' son anagramas.")
            else:
                print(f"'{palabra_a}' y '{palabra_b}' no son anagramas.")
        return confirmacion()

    def es_isograma():
        def isograma(palabra):
            palabra = palabra.lower().replace(" ", "")
            letras_unicas = set(palabra)
            return len(letras_unicas) == len(palabra)

        def confirmacion():
            palabra = input("Digita una palabra: ")
            if isograma(palabra):
                print(f"'{palabra}' es un isograma.")
            else:
                print(f"'{palabra}' no es un isograma.")
        return confirmacion()

    # Bucle principal
    while True:
        print("\n Elige una opción")
        print("1. Verificar si es un Palíndromo")
        print("2. Verificar si es un anagrama")
        print("3. Verificar si es isograma")
        print("4. Salir")

        opcion = input("\nSelecciona una opción: ")

        match opcion:
            case "1":
                es_palindromo()
            case "2":
                es_anagrama()
            case "3":
                es_isograma()
            case "4":
                print("Saliendo del menú.")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 4.")

palabras()