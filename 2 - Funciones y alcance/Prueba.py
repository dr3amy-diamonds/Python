mensaje = "Soy global"

# Se define la función 'mostrar_mensaje'
def mostrar_mensaje():
    mensaje = "Soy local"
    print(mensaje) 

# Se llama a la función
mostrar_mensaje()

# Se imprime la variable global 'mensaje'
print(mensaje)