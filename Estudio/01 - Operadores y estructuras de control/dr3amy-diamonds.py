"""
Operadores Arimeticos
"""

#Suma

suma_uno=4
suma_dos=2

suma_3=suma_uno+suma_dos

print("La suma da como resultado: " + str(suma_3))

#Restas

resta_uno=9
resta_dos=4

resta_tres=resta_uno-resta_dos

print("La resta da como resultado: "  + str(resta_tres))

#Multiplicación

Multiplicacion_Uno=12
Multiplicacion_Dos=8

Multiplicacion_tres=Multiplicacion_Uno*Multiplicacion_Dos

print("La Multiplicación da como resultado: "+ str(Multiplicacion_tres))

#División

Divisor_uno=50
Divisor_Dos=2

Residuo=Divisor_uno/Divisor_Dos

print("El resultado de la división da como resultado: " + str(Residuo))


#Modulación

Dato_uno=58
Dato_Dos=32

Resultado=Dato_uno%Dato_Dos

print("El resultado de la modulación da como resultado: " + str(Resultado))

#Potencia

Potencia_Uno=25
Potencia_Dos=2

Potencia_Resultado=Potencia_Uno**Potencia_Dos

print("El resultado de la potencia da como resultado: " + str(Potencia_Resultado))



"""
Operadores Lógicos
"""

print(False and False or True)
print(True  and not False or True and False)

"""
Operadores De Comparación
"""

#Operador de igualdad (==)
a=5
b=24
c=0

######
a==6
a==5
######
b==24
b==6
######
c==54
c==0


#Operador de desigualdad (!=)
a !=0
a !=21
a !=5

#######
b !=24
b !=15
b != 95
########
c !=0
c !=35
c !=20

#Operador de mayor que (>)
a > 8
a > 0
a >= -3

########
b > -15
b >= 35
b > 12
#######
c >=45
c > 0
c >-1

#Operador de menor que (<)
a < 21
a <= 27
a < 6


#########
b <=65
b < 25
b < 30
########
c < 65
c < 1
c <= 0

"""
Operadores de bit a bit
"""

#Not(~) Bit a Bit

#Como decimales
a=56
b=12

print("Operador Not(~): " , (~a))
print((~b))

c=198
print(bin(~c))

#Operación AND(&) Bit a Bit
#Operación por binarios

print("Operación AND(&) Bit a Bit: " , bin(a & b))

#Operador OR Bit a Bit
#Operación por binarios

print("Operador OR Bit a Bit: " , bin(a | b))

#Operador Xor bit a bit

x=0b1101 ^ 0b110
print("Operador Xor bit a bit: " , bin(x))

"""
Operaciones de Desplazamiento
"""

#Operación (>>) desplazamiento a la derecha

a=0b100011
print( "Operación Derecha: ", bin( a>>2))

b=0b10111
print( "Operación Derecha: ", bin( b>>2))

#Operación (<<) desplazamiento a la izquierda

a=0b10000111
b=0b1101
print( "Operación Izquierda: ", bin( a<<2))
print( "Operación izquierda: ", bin( b<<2))

"""
Estructuras de control
"""

#Condicionales
