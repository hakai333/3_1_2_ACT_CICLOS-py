#Ejemplos de ciclos

#Ciclo comun hasta 5 - muestra de 0 a 4
'''
for i in range(5):
    print(i)
'''

#Ciclo con string - separa el string caracter por caracter
'''
for i in "Hola":
    print(i)
'''

#Ciclo con suma, muestra 5 numeros pero comienza en 2
'''
for i in range(5):
    i = i + 2
    print(i)
'''


'''



#Calcular factorial

#Inciamos un "auxiliar" que nos ayudara a ir multiplicando el contenido de "i" 
aux = 1

#Pedimos el numero para multiplicar el factorial
numFac = int(input("Ingrese un numero: "))

#Imprimimos 
print(f"{numFac}! = ", end="  ")

#Ciclo, para "i" (desde"numFac" - hasta 0 - de uno en uno descendente)
for i in range(numFac, 0, -1):
    print(f" {i} ", end=" ")
    aux *= i

#Imprimimos el total
print(aux)


'''

'''
#Numero Impar

#Ciclo infinito hasta "break"
while(True):
    #Pedimos un numero
    num = int(input("Ingrese un numero IMPAR: "))
    #Si es par, mostramos ERROR
    if num % 2 == 0:
        print("El numero ingresado es PAR")
        print("ERROR")
    else:
        #Si es impar, terminamos el programa
        print("El numero ingresado es IMPAR")
        print("Fin programa")
        break

'''


'''


#Calcular potencia
#Ingresamos un auxiliar
aux = 1
#Pedimos la base
base = int(input("Ingrese la BASE de la potencia: "))
#Pedimos el exponente
exponente = int(input("Ingrese el EXPONENTE de la potencia: "))

#Ciclo, i hasta el exponente
for i in range(exponente):
    #Multiplicamos la base por la cantidad de exponentes que hay
    #Y lo guardamos en el auxiliar
    aux *= base

#Imprimimos el auxiliar que contiene el resultado de la potencia
print(f"El total es: {aux}")


'''
'''
#Numero primo
#Ciclo infinito
while True:
    num = int(input("Ingrese un numero entero POSITIVO: "))
    #Aqui descartamos que sea negativo para volver a preguntar
    if num > 0:
        #Si numero es 2 es primo
        if num == 2:
            es_primo = True
        #Si numero es divisible por 2 no es primo
        elif num % 2 == 0:
             es_primo = False
        else:
            #El resto si ese primo
            es_primo = True
            #Aqui dividimos el numero por todos los numeros hasta su raiz cuadrada (formula) 
            for i in range(3, int(num**0.5) + 1, 2):
                if num % i == 0:
                     es_primo = False
        break
    else:
        print("ERROR")

if es_primo:
    print("Numero primo")
else:
    print("Numero no primo")
'''


'''
#Inciamos un "auxiliar" que nos ayudara a ir multiplicando el contenido de "i" 
aux1 = 1
aux2 = 1
aux3 = 1

#Ciclo infinito 
while True:
    #Pedimos tres numeros 
    numFac1 = int(input("Ingrese un numero: "))
    numFac2 = int(input("Ingrese un numero: "))
    numFac3 = int(input("Ingrese un numero: "))
    if numFac1 > 0 and numFac2 > 0 and numFac3 > 3:
        #Imprimimos factorial numero 1
        print(f"{numFac1}! = ", end="  ")
        for i in range(numFac1, 0, -1):
            print(f" {i} ", end=" ")
            aux1 *= i

        print("\n\n")
        print(f"Factorial 1: {aux1}")
        print("\n\n")
        
        #Imprimimos factorial numero 2
        print(f"{numFac2}! = ", end="  ")
        for i in range(numFac2, 0, -1):
            print(f" {i} ", end=" ")
            aux2 *= i

        print("\n\n")
        print(f"Factorial 2: {aux2}")
        print("\n\n")

        #Imprimimos factorial numero 3
        print(f"{numFac3}! = ", end="  ")
        for i in range(numFac3, 0, -1):
            print(f" {i} ", end=" ")
            aux3 *= i
        print("\n\n")
        print(f"Factorial 3: {aux3}")
        print("\n\n")

        break
    #En caso de ingresar UN solo numero mal, vuelve a pedir tres numeros
    else:
        print("\n\n")
        print("ERROR")
        print("\n\n")
'''


#Fibonacci
#Generamos un auxiliar
aux = 0
#Pedimos un numero entre 7 y 10 
num = int(input("Ingrese un numero entre 7 y 10: "))
#Generamos el numero anterior para comenzar la secuencia
numAnt = num - 1
print("\n")

#Generamos un ciclo de 10 ciclos 
for i in range(10):
    #Imprimimos el numero 
    print(num)
    #Pasamos el numero al auxiliar
    aux = num
    #Sumamos el numero + numeroAnterior para imprimir el sgte numero de la secuencia
    num += numAnt
    #NumeroAnterior ahora es el numero actual
    numAnt = aux 
    
