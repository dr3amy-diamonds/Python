import tkinter as tk
from tkinter import ttk
import sys
import numpy as np

# Importamos las funciones lógicas
from Funciones_Necesarias import (
    generar_analizarmatriz, 
    mostrar_matriz, 
    exploracion_data, 
    limpiar_matriz, 
    aplicar_transformaciones, 
    aplicar_estadisticas
)

# --- CLASE MÁGICA: Redirige los 'print' a la ventana ---
class PrintToText(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, s):
        # Escribe el texto en el widget
        self.text_widget.insert(tk.END, s)
        # Hace scroll automático hacia abajo
        self.text_widget.see(tk.END)

    def flush(self):
        pass # Necesario para que Python no marque error

# --- Configuración de la Ventana Principal ---
ventana = tk.Tk()
ventana.title("Analizador de datos")
ventana.geometry("600x600") # Un poco más grande para que quepan los datos

# --- Función que ejecuta todo el análisis ---
def ejecutar_logica_completa():
    # 1. Limpiamos el contenedor azul antes de escribir nada nuevo
    limpiar_frame(contenedor)
    
    # 2. Creamos la "hoja de papel" (Text widget) DENTRO del contenedor azul
    # bg="white" para que parezca una hoja sobre el fondo azul, 
    # o puedes poner bg="lightblue" si quieres que sea transparente.
    texto_salida = tk.Text(contenedor, height=20, width=70, bg="white", fg="black")
    
    # Scrollbar por si hay muchos datos
    scrollbar = tk.Scrollbar(contenedor, command=texto_salida.yview)
    texto_salida.config(yscrollcommand=scrollbar.set)
    
    # Empaquetamos DENTRO del contenedor
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    texto_salida.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    # 3. Redirigimos los prints a este nuevo cuadro de texto
    old_stdout = sys.stdout # Guardamos la salida original
    sys.stdout = PrintToText(texto_salida) 
    
    try:
        # --- AQUÍ LLAMAMOS A LAS FUNCIONES ---
        print(">>> INICIANDO ANÁLISIS EN EL CONTENEDOR AZUL <<<\n")
        
        # a) Generar
        matriz = generar_analizarmatriz()
        
        # b) Mostrar Original
        mostrar_matriz(matriz, "Matriz Original")
        exploracion_data(matriz)
        
        # c) Limpiar
        print("\n>>> LIMPIANDO VALORES... <<<")
        matriz_limpia = limpiar_matriz(matriz)
        
        # d) Transformar y Estadísticas
        mostrar_matriz(matriz_limpia, "Matriz Limpia")
        aplicar_transformaciones(matriz_limpia)
        aplicar_estadisticas(matriz_limpia)
        
        print("\n>>> FIN DEL REPORTE <<<")
        
    except Exception as e:
        print(f"\nERROR CRÍTICO: {e}")
        
    finally:
        # 4. Restauramos la salida normal para no romper nada más
        sys.stdout = old_stdout

# --- Función para limpiar el frame ---
def limpiar_frame(frame):
    # Destruye todo lo que haya dentro del marco (el cuadro de texto anterior)
    for widget in frame.winfo_children():
        widget.destroy()

# --- INTERFAZ GRÁFICA ---

# Botón Principal
boton = ttk.Button(
    ventana,
    text="¡Generar y Analizar datos!",
    command=ejecutar_logica_completa # Llamamos a nuestra función nueva
)
boton.pack(pady=10)

# El Contenedor Azul (Tu frame original)
contenedor = tk.Frame(
    ventana,
    bg="lightblue",
    bd=2,
    relief="groove"
)
contenedor.pack(
    padx=20,
    pady=10,
    fill="both",
    expand=True
)

# Botón de limpieza
boton_limpiar = ttk.Button(
    ventana,
    text="Limpiar datos",
    command=lambda: limpiar_frame(contenedor)
)
boton_limpiar.pack(pady=10)

# Loop principal
ventana.mainloop()