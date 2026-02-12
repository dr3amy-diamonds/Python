#Crear funcion

def cadena_texto():
    txt = input("Introduce un texto, no importa el tamaño de este:\n ")
    frase= input("Introduce la letra o palabra que quieras buscar:\n ")
    conteo = txt.count(frase)
    return(f"El número de veces que {frase} aparece en la cadena es:", conteo)

print(cadena_texto())