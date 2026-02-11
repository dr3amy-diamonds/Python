import tkinter as tk
from tkinter import messagebox


#Creación de Ventana
Ventana=tk.Tk()

#Crear titulo en la parte superior de la ventana
Ventana.title("Ventana Principal")

#Crear tamaño de la ventana
Ventana.geometry("600x300")

#Crear texto inciial en la ventana
etiqueta = tk.Label(
    Ventana, 
    text="¡Hola, Usuario!", 
    font=("Arial", 16), 
    fg="blue", 
    bg="lightgray"
    )
etiqueta.pack(pady=50)

#Crear Entry
def on_entry_click(event):
    if entry.get() == texto_placeholder:
        entry.delete(0, "end")  # Borra el placeholder
        entry.config(fg="black")  # Cambia el color del texto

def on_focusout(event):
    if entry.get() == "":
        entry.insert(0, texto_placeholder)
        entry.config(fg="gray")
    
texto_placeholder = "Introduce tu nombre"
entry = tk.Entry(Ventana, fg="gray")
entry.insert(0, texto_placeholder)
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_focusout)
entry.pack()

#Crear botón
def saludar():
    nombre = entry.get()
    if nombre != texto_placeholder and nombre != "":
        messagebox.showinfo("Saludo", f"¡Hola, {nombre}!")
    else:
        messagebox.showwarning("Advertencia", "Por favor, introduce tu nombre.")

button=tk.Button(
    Ventana,
    text="Enviar", 
    font=("Arial", 16), 
    fg="blue", 
    bg="lightgray",
    command=saludar)
    
button.pack(pady=20)
#Correr Ventana
Ventana.mainloop()