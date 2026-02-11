"""
Importación de estas liberias por el generador de contraseñas
"""
import secrets
import string

def generar_contraseñas():
    letras = string.ascii_letters       #Todas las letras del alfabeto (mayúsculas y minúsculas).
    digitos = string.digits             # Todos los dígitos del 0 al 9.
    caracteres_especiales = string.punctuation #Todos los caracteres especiales.

    alfabeto = letras + digitos + caracteres_especiales #Se combinan las letras, dígitos y caracteres especiales en una sola cadena

    longitud = 12

    while True:
        """
        Genera una contraseña aleatoria y verifica que cumpla:
        - Al menos un carácter especial.
        - Al menos dos dígitos numéricos.
        """

        # Generar contraseña candidata
        contraseña = ''.join(secrets.choice(alfabeto) for _ in range(longitud))

        """
        `tiene_especial`: True si la contraseña contiene al menos un símbolo
        de la lista 'especiales'.
        """
        tiene_especial = any(c in caracteres_especiales for c in contraseña)

        """
        `cantidad_digitos`: cuenta cuántos caracteres de la contraseña
        pertenecen al conjunto 'digitos'.
        """
        cantidad_digitos = sum(c in digitos for c in contraseña)

        # Devolver solo si cumple los requisitos
        if tiene_especial and cantidad_digitos >= 2:
            return "Contraseña Generada: " +contraseña

def verificar_contraseñas():
    letras = string.ascii_letters       # Todas las letras del alfabeto (mayúsculas y minúsculas).
    digitos = string.digits             # Todos los dígitos del 0 al 9.
    caracteres_especiales = string.punctuation # Todos los caracteres especiales.

    # Solicitar la contraseña al usuario
    contraseña = input("Ingresa tu contraseña: ")

    # Verificar que tenga al menos un carácter especial
    tiene_especial = any(c in caracteres_especiales for c in contraseña)

    # Verificar que tenga al menos dos dígitos numéricos
    cantidad_digitos = sum(c in digitos for c in contraseña)

    # Comprobar si cumple con los requisitos
    if tiene_especial and cantidad_digitos >= 2:
        return "La contraseña es válida."
    else:
        return "La contraseña no es válida. Asegúrate de que tenga al menos un carácter especial y dos dígitos numéricos."

#================================================ Menú ================================================================================================
while True:
    print("\n=== Bienvenido al verificador de Contraseñas Seguras ===")
    
    try:
        opciones = int(input(
            "Seleccione una opción:\n"
            "1. Generar Contraseña\n"
            "2. Verificar Contraseña\n"
            "3. Salir\n"
        ))
    except ValueError:
        print("❌ Opción inválida, introduce un número del 1 al 3.")
        continue

    match opciones:
        case 1:
            print(generar_contraseñas())
            break;
        case 2:
            print(verificar_contraseñas())
            break;
        case 3:
            print("¡Hasta Luego!")
            break;
