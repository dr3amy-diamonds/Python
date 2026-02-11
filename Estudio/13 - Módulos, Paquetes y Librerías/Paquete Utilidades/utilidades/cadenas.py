def contar_vocales():
    try:
        texto = input("Ingrese un texto:\n").strip()
        if not isinstance(texto, str):
            raise TypeError("El argumento debe ser una cadena de texto.")
        vocales = "aeiouáéíóúü"
        contador = 0
        for caracter in texto.lower():
            if caracter in vocales:
                contador += 1
        return contador
    except Exception as e:
        print(f"Error: {e}")

total_vocales = contar_vocales()
print(f"El texto contiene {total_vocales} vocal(es).")
