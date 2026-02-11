import tkinter as tk
from tkinter import messagebox
import random


# Crear ventana principal
ventana = tk.Tk()

# Crear título de la ventana
ventana.title("Adivina el número")

# Crear dimensiones de la ventana
ventana.geometry("500x300")

# Crear título
titulo = tk.Label(
    ventana,
    text="Adivina el número",
    font=("Century Gothic", 15, "bold"),
    pady=20
)
titulo.pack()

# Etiqueta para mostrar la frase
etiqueta_frase = tk.Label(
    ventana,
    text="Introduce el número y presiona el botón a ver si pudiste adivinarlo",
    wraplength=450,
    justify="center",
    font=("Century Gothic", 12),
    pady=15
)
etiqueta_frase.pack()

# Crear Entry
def on_entry_click(event):
    if entry.get() == texto_placeholder:
        entry.delete(0, "end")  # Borra el placeholder
        entry.config(fg="black")  # Cambia el color del texto

def on_focusout(event):
    if entry.get() == "":
        entry.insert(0, texto_placeholder)
        entry.config(fg="gray")
    
texto_placeholder = "Introduce el número"
entry = tk.Entry(ventana, fg="gray")
entry.insert(0, texto_placeholder)
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_focusout)
entry.pack()

# Crear función de número aleatorio y el juego
def iniciar_juego():
    numero_secreto = random.randint(1, 20)
    intentos = 0

    def adivinar():
        nonlocal intentos
        try:
            intento = int(entry.get())
            intentos += 1
            if intento < numero_secreto:
                messagebox.showinfo("Pista", "El número es mayor.")
            elif intento > numero_secreto:
                messagebox.showinfo("Pista", "El número es menor.")
            else:
                messagebox.showinfo("¡Ganaste!", f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                iniciar_juego()  # Reinicia el juego después de ganar
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido.")

    return adivinar


# Crear botón para iniciar el juego
boton_iniciar = tk.Button(
    ventana,
    text="Comenzar a Adivinar",
    font=("Century Gothic", 12, "bold"),
    bg="#102e4a",
    fg="white",
    padx=10,
    pady=5,
    command=iniciar_juego()  # Inicia el juego cuando se hace clic
)
boton_iniciar.pack(pady=30)

# Correr la ventana
ventana.mainloop()
