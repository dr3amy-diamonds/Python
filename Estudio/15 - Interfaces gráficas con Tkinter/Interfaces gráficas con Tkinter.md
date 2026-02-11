# ¿Qué es Tkinter?

**Tkinter** es la librería estándar de **Python** para crear
**interfaces gráficas de usuario (GUI)**.

Una GUI incluye elementos como: - Ventanas\
- Botones\
- Campos de texto\
- Etiquetas

👉 Es lo contrario a los programas que funcionan solo por terminal.

------------------------------------------------------------------------

## Lo más importante

-   ✅ Viene incluida con Python\
-   ❌ No se instala\
-   💻 Funciona en Windows, Linux y macOS

------------------------------------------------------------------------

## ¿Para qué sirve Tkinter?

Tkinter se usa para crear **aplicaciones de escritorio**, por ejemplo:

-   Calculadoras\
-   Formularios\
-   Juegos simples\
-   Gestores de archivos\
-   Aplicaciones educativas\
-   Prototipos rápidos

### Ideal para:

-   Principiantes\
-   Aprender lógica visual\
-   Proyectos **Easy** y **Mid** con interfaz gráfica

------------------------------------------------------------------------

## ¿Para qué NO se usa Tkinter?

Tkinter **no es adecuado** para:

-   Apps móviles\
-   Interfaces modernas tipo redes sociales\
-   Juegos 3D\
-   Aplicaciones web

👉 Es funcional, no "bonito" por defecto.

------------------------------------------------------------------------

## ¿Cómo funciona Tkinter? (Modelo mental)

Tkinter se basa en **3 ideas clave**:

### 1. Ventana principal

Toda aplicación empieza con una ventana principal (`Tk`).

> Si no hay ventana, no hay app.

------------------------------------------------------------------------

### 2. Widgets (elementos visuales)

Los widgets son los componentes visibles:

-   Botones\
-   Textos\
-   Entradas de datos\
-   Listas

Tkinter consiste en **poner widgets dentro de la ventana**.

------------------------------------------------------------------------

### 3. Eventos

Un evento es una acción del usuario:

-   Hacer clic\
-   Escribir texto\
-   Cerrar la ventana

Tkinter: \> espera eventos → responde a eventos

------------------------------------------------------------------------

## Concepto clave: bucle de eventos

Las apps con Tkinter **no terminan solas**.

-   El programa se queda ejecutándose\
-   Escucha acciones del usuario\
-   Reacciona cuando algo ocurre

Esto se llama **bucle de eventos** (`mainloop()`).

------------------------------------------------------------------------

## Componentes principales de Tkinter

### Ventana (`Tk`)

-   Es la aplicación en sí\
-   Solo existe una ventana principal

------------------------------------------------------------------------

### Widgets básicos más usados

  Widget        Función
  ------------- ------------------
  Label         Mostrar texto
  Button        Botón clickeable
  Entry         Entrada de texto
  Text          Texto largo
  Checkbutton   Casilla
  Radiobutton   Opciones
  Listbox       Listas

👉 Con estos widgets puedes crear la mayoría de apps simples.

------------------------------------------------------------------------

### Variables especiales

Tkinter usa variables propias para conectar la lógica con la interfaz:

-   `StringVar`
-   `IntVar`
-   `BooleanVar`

Permiten que la interfaz se actualice dinámicamente.

------------------------------------------------------------------------

## Organización de widgets (Layouts)

Tkinter usa **gestores de geometría**:

### `pack()`

-   Automático\
-   Fácil\
-   Ideal para principiantes

### `grid()`

-   Filas y columnas\
-   Más control\
-   Muy usado

### `place()`

-   Coordenadas exactas\
-   Poco recomendado

⚠️ Nunca mezclar `pack()` y `grid()` en la misma ventana.

------------------------------------------------------------------------

## Conectar lógica con interfaz

Se hace usando **funciones**:

-   Botón → llama a una función\
-   Función → cambia un widget\
-   Usuario → ve el cambio

Aquí aplicas todo Python: - Funciones\
- Condicionales\
- Estructuras\
- Módulos

------------------------------------------------------------------------

## ¿Por qué Tkinter es ideal para aprender?

-   No introduce conceptos complejos\
-   Reutiliza Python básico\
-   Resultados rápidos\
-   Motiva al aprender

👉 Tkinter es un **puente**, no el destino final.

------------------------------------------------------------------------

## Errores comunes de principiantes

-   ❌ Pensar que Tkinter es obsoleto\
-   ❌ Intentar hacerlo "bonito" desde el inicio\
-   ❌ Querer aprender todo Tkinter\
-   ❌ Compararlo con aplicaciones web

------------------------------------------------------------------------

## Resumen final

**Tkinter sirve para crear aplicaciones de escritorio simples y
educativas, y es ideal para aprender interfaces gráficas en Python.**
