"""
Pilas

Una pila es una estructura de datos que puede contener muchos elementos, y el último elemento agregado es el primero en eliminarse.

Como una pila de panqueques, estos se añaden y se retiran desde arriba. Por lo tanto, al retirar un panqueque, siempre será el último que se haya añadido. Esta forma de organizar los elementos se llama LIFO (último en entrar, primero en salir).
"""

"""
Las operaciones básicas que podemos realizar en una pila son:

*   Push: Agrega un nuevo elemento a la pila.
*   Pop: Elimina y devuelve el elemento superior de la pila.
*   Peek: Devuelve el elemento superior (último) de la pila.
*   isEmpty: Comprueba si la pila está vacía.
*   Size: Encuentra el número de elementos en la pila.
"""


#Se usa la pila cuando quieres lo más simple y no tienes demasiados elementos.


#Crear Pila
Pila = []

# Push
Pila.append('A')
Pila.append('B')
Pila.append('C')
print("Pila: ", Pila)

# Peek
Ultimo_Elemento = Pila[-1]
print("Peek: ", Ultimo_Elemento)

# Pop
Eliminar_Elemento = Pila.pop()
print("Pop: ", Eliminar_Elemento)

# Pila después de eliminar un elemento
print("Pila Actualizada: ", Pila)

# isEmpty
isEmpty = not bool(Pila)
print("¿Esta vacia?: ", isEmpty)

# Size
print("Tamaño: ",len(Pila))

"""
Colas

Una cola es una estructura de datos lineal que sigue el principio primero en entrar, primero en salir (FIFO).
"""

"""
Las operaciones básicas que podemos realizar en una cola son:

*   Enqueue: Agrega un nuevo elemento a la cola.
*   Dequeue: Elimina y devuelve el primer elemento (frontal) de la cola.
*   Peek: Devuelve el primer elemento de la cola.
*   isEmpty: Comprueba si la cola está vacía.
*   Size: Encuentra el número de elementos en la cola.
"""

#Úsala solo para ejemplos pequeños, porque pop(0) es lento en listas largas.

#Crear cola
Cola = []

# Enqueue
Cola.append('A')
Cola.append('B')
Cola.append('C')
print("Cola: ", Cola)

# Peek
Primer_Elemento = Cola[0]
print("Elemento: ", Primer_Elemento)

# Dequeue
Elemento_Eliminado = Cola.pop(0)
print("Elemento Eliminado: ", Elemento_Eliminado)

print("Cola actualizada: ", Cola)

# isEmpty
isEmpty = not bool(Cola)
print("¿Esta vacia? ", isEmpty)

# Size
print("Tamaño: ", len(Cola))

"""
Deque (doble cola, de collections)

Collections.deque es una cola de doble extremo (double-ended queue), permite insertar y eliminar elementos en ambos extremos (inicio y final) de forma eficiente (O(1) en promedio). A diferencia de las listas (list), donde insertar o eliminar al inicio es lento, deque lo hace rápidamente.
"""
"""
Es ideal para:

*   Implementar colas (FIFO).

*   Implementar pilas (LIFO).

*   Algoritmos de ventana deslizante (sliding window).

*   Mantener un historial con tamaño limitado (maxlen).
"""

"""
Se importa de esta manera:
    from collections import deque
    cola = deque()
"""

"""
Operaciones principales:

*   append(x) → Inserta al final.

*   appendleft(x) → Inserta al inicio.

*   pop() → Quita del final.

*   popleft() → Quita del inicio.

*   extend(iterable) / extendleft(iterable) → Agregar varios elementos.

*   rotate(n) → Rota los elementos a izquierda o derecha.

*   clear() → Vacía el deque.
"""

#deque es la mejor opción para colas rápidas y también puede reemplazar a las pilas.

#Crear como cola
from collections import deque

cola = deque()

# Enqueue (agregar al final)
cola.append("A")
cola.append("B")
cola.append("C")
print("Cola:", cola)   # deque(['A', 'B', 'C'])

# Dequeue (quitar del inicio)
primero = cola.popleft()
print("Elemento atendido:", primero)  # A
print("Cola actual:", cola)  # deque(['B', 'C'])

#Crear como pila
pila = deque()

# Push
pila.append("A")
pila.append("B")
pila.append("C")
print("Pila:", pila)   # deque(['A', 'B', 'C'])

# Pop (último elemento)
ultimo = pila.pop()
print("Elemento quitado:", ultimo)  # C
print("Pila actual:", pila)  # deque(['A', 'B'])

#Ejemplo
#Con rotate() (simulando turnos en un juego)

jugadores = deque(["Ana", "Luis", "Carlos", "Marta"])
print("Turno inicial:", jugadores[0])  # Ana

jugadores.rotate(-1)  # pasa el turno al siguiente
print("Siguiente turno:", jugadores[0])  

jugadores.rotate(-1)
print("Siguiente turno:", jugadores[0])  


"""
Heap (cola de prioridad, de heapq):

heapq implementa una cola de prioridad usando listas como estructura base. 

Por defecto, es un montículo mínimo (min-heap):

*   El elemento más pequeño siempre está en la raíz.

*   Acceder o quitar el de mayor prioridad es eficiente (O(log n)).
"""

"""
Se importa así:
import heapq
heap = []
heapq.heappush(heap, (prioridad, valor))
elem = heapq.heappop(heap)  # devuelve el de menor prioridad
"""

"""
Operaciones principales:

*   heappush(heap, x) → Inserta un elemento.

*   heappop(heap) → Extrae el menor elemento.

*   heapify(lista) → Convierte una lista en un heap.

*   nlargest(n, iterable) / nsmallest(n, iterable) → Retorna los n elementos más grandes/pequeños.
"""

#heapq se usa cuando no importa el orden de llegada (como en una cola normal), sino la prioridad de los elementos.

#Crear heapq
import heapq

cola_prioridad = []

# Agregar elementos con prioridad
heapq.heappush(cola_prioridad, (2, "Tarea B"))
heapq.heappush(cola_prioridad, (1, "Tarea A"))
heapq.heappush(cola_prioridad, (3, "Tarea C"))

print("Cola de prioridad:", cola_prioridad)

# Sacar elementos en orden de prioridad
while cola_prioridad:
    print("Atendiendo:", heapq.heappop(cola_prioridad))

#Usando heapify() (crear heap desde lista)
numeros = [5, 1, 8, 3, 2]
heapq.heapify(numeros)
print("Heap:", numeros)  

print("Menor elemento:", heapq.heappop(numeros))  
print("Heap actualizado:", numeros) 

#Encontrar los n elementos más pequeños o más grandes
numeros = [10, 4, 7, 2, 15, 6]

print("3 más pequeños:", heapq.nsmallest(3, numeros)) 
print("2 más grandes:", heapq.nlargest(2, numeros))  