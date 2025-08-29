#Condicionales
#Primer Ejercicio

Numero = int(input("Ingrese un numero: "))

if Numero>0:
    print("El Número es Positivo")
elif Numero==0:
    print("El Número es Cero")
else:
    print("El Número es Negativo")

#Segundo Ejercicio

Nota=float(input("Ingresa tu nota:" ))
if Nota<5:
    print("Estas Suspendido mi Chikitin")
else:
    print("Estas Aprobado Amiguito")

#Segundo Ejercicio más complicado
Nota=float(input("Ingresa tu nota:" ))
if 0<=Nota and Nota <5:
    print("Estas Suspendido mi Chikitin")
elif 5 <= Nota and Nota <7:
    print("Aprobado")
elif 7 <= Nota and Nota <9:
    print("Notable")
elif 9<= Nota and Nota <=10:
    print("Sobresaliente")
else:
    print("Nota fuera de Rango")
######################################
print("Fin Del Programa")

#Bucles

#While
Contandor =3
while Contandor !=0:
    Contandor=Contandor-1
    print("El número es: ", Contandor )

#For
lista=list((2,1,0))
tupla=tuple((2,1,0))
conjunto=set((2,1,0))
Diccionario=dict(((2,"Dos"),(1,"Uno"),(0, "Cero")))

for iterador in [1,2,3]:
    print(iterador)


for iterador in lista: #Así como tupla, conjunto y diccionario(Recorre solamente los números) reemplazandolo donde dice lista
    print(iterador)

#Para recorrer los valores(Cadenas de caracteres String)
for iterador in Diccionario.values():
    print(iterador)

#Para Recorrer los dos valores (Cadena de Caracyeres String y Datos Númericos)
for iterador in Diccionario.items():
    print(iterador)

#Recorrer a través de índices
lista = ["Vamos", "a","acceder","a", "esta", "lista","por","indices"]
for indice in range(len(lista)): #Len para obtener el número de elementos #Range para una secuencia de indices
    print ("Índice: ",  indice, "Elemento: ", lista[indice])

#Usando Break y True

#Break
for numero in range(5):
    if numero==10:
        break
    print(numero)

#Continue
for numero in range(5):
    if numero==10:
        continue
    print(numero)

#Combinacion de todas las sentencias

Intentos=3
while Intentos >0:
    if input("Digite contraseña: ") =="Mariposa":
        print("Correcta")
        break
    Intentos = Intentos -1 
    print("Contraseña Incorrecta")
else:
    print("Se te acabaron los intentos :( ")
