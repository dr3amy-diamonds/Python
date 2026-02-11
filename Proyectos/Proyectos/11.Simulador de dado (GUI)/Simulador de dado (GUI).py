import tkinter as tk
from tkinter import messagebox
import random

#Crear función de números aleatorios
def lanzar_dado():
    numero_random = random.randint(1, 6)
    texto_dado= f'Has lanzado el dado, el número que sacaste es: {numero_random}'
    messagebox.showinfo("Dado", texto_dado)

#Crear ventana principal
ventana = tk.Tk()

#Crear titulo de la ventana
ventana.title("Lanzamiento de dado")

#Crear dimesiones de la ventana
ventana.geometry("400x200")

#Crear titulo 
titulo = tk.Label(
    ventana,
    text="Lanzar Dado",
    font=("Times New Roman", 16, "bold"),
    pady=10
)
titulo.pack()

# Etiqueta para mostrar la frase
etiqueta_frase = tk.Label(
    ventana,
    text="Presiona el botón para lanzar el dado",
    wraplength=450,
    justify="center",
    font=("Arial", 12),
    pady=20
)
etiqueta_frase.pack()

#Creacion del botón
boton_generar = tk.Button(
    ventana,
    text="Lanzar Dado",
    font=("Arial", 12, "bold"),
    bg="#102e4a",
    fg="white",
    padx=10,
    pady=5,
    command=lanzar_dado
)
boton_generar.pack()

#Correr la ventana
ventana.mainloop()