from collections import deque
import heapq

"""
Nivel 1: básicos
"""

"""
Ejercicio 1: Pila con lista

1. Crea una pila vacía usando una lista. Inserta los números 1, 2 y 3.
Luego elimina el último elemento insertado y muestra cómo queda la pila en cada paso.
"""

#Crear pila vacia
Pila=[]

#Insertar números
Pila.append('1')
Pila.append('2')
Pila.append('3')
print("Pila: ", Pila)

#Eliminar número
Eliminar_Elemento = Pila.pop(-1)
print("Pop: ", Eliminar_Elemento)
print("Pila: ", Pila)

"""
Ejercicio 2: Cola con lista

2. Crea una cola vacía usando una lista. Inserta los números 10, 20 y 30.
Atiende (elimina) al primer número que entró y muestra la cola después de cada operación.
"""

#Crear Cola vacía
Cola = []

#Insertar números
Cola.append('10')
Cola.append('20')
Cola.append('30')
print("Cola: ", Cola)

#Eliminar número
Elemento_Eliminado = Cola.pop(0)
print("Elemento Eliminado: ", Elemento_Eliminado)
print("Cola: ", Cola)

"""
Ejercicio 3: Deque básico

3. Crea un deque vacío. Inserta la letra "A" al inicio y "B" al final.
Después elimina un elemento de cada extremo y muestra el resultado final.
"""

#Crear deque vacío
Cola = deque()

#Insertar letras
Cola.append("A")
Cola.append("AB")
Cola.append("B")
print("Cola:", Cola)

#Eliminar elemento
primero = Cola.popleft()
ultimo = Cola.pop()
print("Elemento eliminado:", primero)
print("Elemento eliminado:", ultimo)
print("Cola actual:", Cola)

"""
Nivel 2: prácticos
"""

"""
Ejercicio 1: Historial de navegador (pila)

1. Usa una pila para simular que un usuario visita estas páginas en orden:
"google", "youtube", "github".
Luego el usuario presiona el botón “atrás” dos veces. ¿En qué página queda al final?
"""

#Crear pila vacia
Pila=[]

#Insertar números
Pila.append('Google')
Pila.append('Youtube')
Pila.append('GitHub')
print("Pila: ", Pila)

#Página Final
pagina_actual = Pila.pop()   
pagina_actual = Pila.pop()   
print("Página actual:", Pila[-1])  

"""
Ejercicio 2: Fila de supermercado (cola)

2. Usa un deque para simular la fila de un supermercado. Llegan en orden:
"Ana", "Luis", "Marta".
Atiende a los dos primeros clientes. ¿Quién queda en la fila?
"""

# Crear deque vacío
cola = deque()

# Agregar clientes a la fila
cola.append("Ana")
cola.append("Luis")
cola.append("Marta")
print("Cola:", cola)

# "Atender" los dos primeros clientes
Elemento_Eliminado1 = cola.popleft()
Elemento_Eliminado2 = cola.popleft()

print("Cliente Atendido:", Elemento_Eliminado1)
print("Cliente Atendido:", Elemento_Eliminado2)
print("Cola:", cola)

"""
Ejercicio 3: Ventana deslizante (deque)
3. Crea un deque con tamaño máximo de 3. Inserta los números del 1 al 5.
Muestra cómo el deque va manteniendo siempre los últimos tres elementos.
"""

# Crear deque con tamaño máximo 3
d = deque(maxlen=3)

# Insertar números del 1 al 5
for i in range(1, 6):
    d.append(i)
    print(f"Después de insertar {i}: {d}")

"""
Nivel 3: retadores
"""

"""
Ejercicio 1: Ordenar con heapq
1.Inserta los números [9, 1, 6, 4] en un heap.
Luego extrae todos los elementos uno a uno hasta que quede vacío.
¿En qué orden salen los números?
"""
#Crear headpq
cola_prioridad = []

#Insertar números
heapq.heappush(cola_prioridad, 9)
heapq.heappush(cola_prioridad, 1)
heapq.heappush(cola_prioridad, 6)
heapq.heappush(cola_prioridad, 4)

print("Cola de prioridad:", cola_prioridad)

while cola_prioridad:
    print("Atendiendo:", heapq.heappop(cola_prioridad))

"""
Ejercicio 2: Simulación de prioridades (heapq)
2. Tienes las siguientes tareas con su prioridad (un número más pequeño = mayor prioridad):

(1, "hacer tarea")

(3, "jugar videojuegos")

(2, "leer")
Usa un heap para ejecutar las tareas en orden de prioridad.
"""

#Crear headpq
cola_prioridad = []

# Agregar elementos con prioridad
heapq.heappush(cola_prioridad, (1, "Hacer tarea"))
heapq.heappush(cola_prioridad, (3, "Jugar Videojuegos"))
heapq.heappush(cola_prioridad, (2, "Leer"))

print("Cola de prioridad:", cola_prioridad)

#Ejecutar prioridad
tarea_alta = heapq.heappop(cola_prioridad)
print(f"Se ejecutó: {tarea_alta}")

tarea_media = heapq.heappop(cola_prioridad)
print(f"Se ejecutó: {tarea_media}")

tarea_baja = heapq.heappop(cola_prioridad)
print(f"Se ejecutó: {tarea_baja}")

"""
Ejercicio 3:
3. Crea un deque.
*   Primero úsalo como pila: agrega tres elementos y retíralos uno a uno por el mismo extremo.
*   Después úsalo como cola: agrega tres elementos y retíralos por el extremo opuesto.
"""

#Como Pila
pila=deque()

#Agregar elementos
pila.append("A")
pila.append("B")
pila.append("C")
print("Pila:", pila) 

#Retirar uno por uno

for i in range(len(pila)):
    ultimo = pila.pop()
    print("Elemento retirado:", ultimo)


#Estado de la pila
isEmpty = not bool(pila)
print("¿Esta vacia?: ", isEmpty)

#Como cola
cola = deque()

#Agregar elementos
cola.append("A")
cola.append("B")
cola.append("C")
print("Cola:", cola) 

#Retirar uno por uno

while cola:
    ultimo = cola.popleft()
    print("Elemento retirado:", ultimo)


#Estado de la cola
isEmpty = not bool(cola)
print("¿Esta vacia?: ", isEmpty)