import tkinter as tk
from tkinter import messagebox
import random

#Crear lista con frases
lista_frase = [
    "La vida es 10% lo que te ocurre y 90% cómo reaccionas.",
    "El éxito es la suma de pequeños esfuerzos repetidos día tras día.",
    "No cuentes los días, haz que los días cuenten.",
    "La disciplina es el puente entre metas y logros.",
    "Cree que puedes y ya estás a medio camino.",
    "El fracaso es la oportunidad de comenzar de nuevo con más inteligencia.",
    "El único modo de hacer un gran trabajo es amar lo que haces.",
    "La perseverancia es el secreto de todos los triunfos.",
    "No esperes a que las cosas sucedan, sal y haz que sucedan.",
    "Cada día es una nueva oportunidad para cambiar tu vida.",
    "La actitud lo es todo: elige ser positivo.",
    "El miedo es solo una ilusión que te impide avanzar.",
    "La creatividad nace de la angustia como el día nace de la noche oscura.",
    "El cambio empieza cuando decides que es más importante tu futuro que tu pasado.",
    "La confianza en uno mismo es el primer secreto del éxito."
]

#Crear función que valide que la lista no este vacia
def generar_frase():
    try:
        if not lista_frase:
            raise ValueError("La lista de frases está vacía.")
        frase = random.choice(lista_frase)
        messagebox.showinfo("Frase generada", frase)  # Muestra la frase en un messagebox
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo generar la frase: {e}")


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Generador de Frases Aleatorias")
ventana.geometry("600x350")

#Crear titulo 
titulo = tk.Label(
    ventana,
    text="Generador de Frases",
    font=("Arial", 16, "bold"),
    pady=10
)
titulo.pack()

# Etiqueta para mostrar la frase
etiqueta_frase = tk.Label(
    ventana,
    text="Presiona el botón para obtener una frase",
    wraplength=450,
    justify="center",
    font=("Arial", 12),
    pady=20
)
etiqueta_frase.pack()

# Botón para generar frase
boton_generar = tk.Button(
    ventana,
    text="Generar Frase",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5,
    command=generar_frase
)
boton_generar.pack()


#Correr Ventana
ventana.mainloop()
