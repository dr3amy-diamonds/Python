def espacios():
    try:
        texto = input("Ingrese una cadena de texto: ")
        texto_limpio = texto.strip()
        return texto_limpio
    except Exception as e:
        print(f"Error: {e}")