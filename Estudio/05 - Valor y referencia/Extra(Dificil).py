
"""
Ejercicio:

* Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
    Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
    Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las variables originales y las nuevas, comprobando que se ha invertidosu valor en las segundas.
    Comprueba también que se ha conservado el valor original en las primeras.
"""
#Programa 1 
def intercambiar_valores(x, y):

    return y, x

a = 5
b = 10

nuevo_a, nuevo_b = intercambiar_valores(a, b)

print("Originales:", a, b)      
print("Intercambiados:", nuevo_a, nuevo_b)  

#Programa 2
def intercambiar_listas(l1, l2):
    # Retorna las listas intercambiadas
    return l2, l1

# Listas originales
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Nuevas variables con el resultado
nueva_lista1, nueva_lista2 = intercambiar_listas(lista1, lista2)

print("Originales:", lista1, lista2)      # siguen igual
print("Intercambiadas:", nueva_lista1, nueva_lista2)  # están invertidas

