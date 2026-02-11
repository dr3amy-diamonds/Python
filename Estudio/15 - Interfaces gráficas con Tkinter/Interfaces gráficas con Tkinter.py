import tkinter as tk

# Importa la librería Tkinter.
# Se usa "as tk" para escribir menos código al llamar a sus funciones.

# Crear la ventana principal de la aplicación
ventana = tk.Tk()
# Sin esta línea no existe la ventana ni la aplicación.

# Establecer el título de la ventana
ventana.title("Mi primera app con Tkinter")
# Este texto aparece en la barra superior de la ventana.

# Definir el tamaño de la ventana (ancho x alto en píxeles)
ventana.geometry("300x200")

# Crear una etiqueta de texto (Label)
etiqueta = tk.Label(
    ventana,              # Ventana donde se coloca el texto
    text="Hola, Tkinter"  # Texto que se mostrará en pantalla
)

# Mostrar la etiqueta en la ventana
etiqueta.pack(pady=20)
# pack() coloca el widget en la ventana
# pady=20 agrega espacio vertical alrededor del texto

# Crear un botón
boton = tk.Button(
    ventana,              # Ventana donde se coloca el botón
    text="Cerrar",        # Texto del botón
    command=ventana.destroy  # Función que se ejecuta al hacer clic
)
# ventana.destroy cierra la aplicación

# Mostrar el botón en la ventana
boton.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
# Mantiene la ventana abierta y escucha eventos como clics y acciones del usuario.
# Siempre debe ir al final del programa.
