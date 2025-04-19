# ACTIVIDAD 1
# Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

print("ACTIVIDAD 1")

# Definición e inicialización de variable
num = 0

# Generación e imresión de números enteros de 0 a 100 incluyendo ambos extremos
for num in range (101):
    print(num)
    num += 1

print("##########")

#########################################################################################################################

# ACTIVIDAD 2
# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

print("ACTIVIDAD 2")

# Solicita al ususario un número entero
numero = int(input("Ingrese un número entero: "))

# Determina y muestra por pantalla la cantidad de dígitos que contiene el número entero ingresado por el usuario

if (numero > 0):  # Valida si el número ingresado por el usuario es un entero
    texto = str(numero)
    digitos = len(texto)
    print(f"La cantidad de dígitos que tiene el número {numero} es igual a {digitos}")
else:
    print("El número ingresado no es un entero")

print("##########")

##########################################################################################################################

# ACTIVIDAD 3
# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

print("ACTIVIDAD 3")

# Solicita y valida dos números enteros ingresados por el usuario
numero_1 = int(input("Ingrese el primer número entero: "))
numero_2 = int(input("Ingrese el segundo número entero: "))

# Determina cual de los números ingresados es el mayor
if (numero_1 > numero_2):
    numero_maximo = numero_1
    numero_minimo = numero_2
else:
    numero_maximo = numero_2
    numero_minimo = numero_1

# Suma todos los números enteros entre los números ingresados por el usuario
sumatoria = 0
for cont in range ((numero_minimo + 1), numero_maximo):
    sumatoria += cont

# Muestra por pantalla la sumatoria 
print(f"La sumatoria de los números enteros comprendidos entre {numero_minimo} y {numero_maximo} es igual a {sumatoria}")

print("##########")

#########################################################################################################################

# ACTIVIDAD 4
# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

print("ACTIVIDAD 4")

# Solicita al usuario que ingrese un número
numero = int(input("Ingrese un número entero (con el 0 el programa se detiene y muestra el total acumulado): "))

# Inicializa la variable
sumatoria = 0

# Suma los números ingresados
while (numero != 0):
    sumatoria += numero
    numero = int(input("Ingrese un número entero (con el 0 el programa se detiene y muestra el total acumulado): "))

# Muestra por pantalla el valor acumulado   
print(f"El total acumulado es {sumatoria}")

print("##########")

#######################################################################################################################

# ACTIVIDAD 5
# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

print("ACTIVIDAD 5")

# Importa 
import random

# Genera número aleatorio
aleatorio = random.randint(0, 9)

# Solicita numero al usuario
numero = int(input("Ingrese un número: "))

# Inicializa variable
cont = 1

# Compara número ingresado por el usuario y número aleatorio
while (numero != aleatorio):
    cont += 1
    aleatorio = random.randint(0, 9)
    numero = int(input("No adivinó el número aleatorio. Ingrese otro número: "))

# Muestra por pantalla
print(f"El usuario adivinó el número aleatorio {aleatorio} en el intento {cont}")

print("##########")

################################################################################################################

# ACTIVIDAD 6
# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

print("ACTIVIDAD 6")

# Genera números en el rango 0 - 100
for cont in range (100, -1, -1):
    if (cont % 2 == 0):  # Determina si el número es par
        print(cont)

print("##########")

################################################################################################################

# ACTIVIDAD 7
# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

print("ACTIVIDAD 7")

# Inicializa variable
sumatoria = 0

# Solicita un número al usuario
numero = int(input("Ingrese un número entero positivo: "))

while (numero <= 0):
    numero = int(input("Ingrese un número entero positivo: "))

#Calcula la suma
for x in range(0, (numero+1)):
    sumatoria += x

# Muestra por pantalla
print(f"La sumatoria de los números enteros positivos ente 0 y {numero} es {sumatoria}")

print("##########")

###############################################################################################################

# ACTIVIDAD 8
# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

print("ACTIVIDAD 8")

# Inicializa variables
LIMITE_SUP = 10
cont_par = 0
cont_impar = 0
cont_positivo = 0
cont_negativo = 0

# Determina si ,os numeros son pares, impares, positivos, negativos
for x in range(1,(LIMITE_SUP+1)):
    numero = int(input("Ingrese el número entero " + str(x) + ": "))
    if (numero != 0):
        if (numero % 2 == 0):
            cont_par += 1
        else:
            cont_impar += 1
        if (numero > 0):
            cont_positivo += 1
        else:
            cont_negativo += 1

# Muestra por pantalla
print(f"pares {cont_par} ; impares {cont_impar}; positivos {cont_positivo}; negativos {cont_negativo}")

print("##########")

###############################################################################################################

# ACTIVIDAD 9
# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

print("ACTIVIDAD 9")

# Inicializa variables
LIMITE_SUP = 10
sumatoria = 0

# Solicita el ingreso de los valores y los suma
for x in range(1,(LIMITE_SUP+1)):
    numero = int(input("Ingrese el número entero " + str(x) + ":"))
    sumatoria += numero

# Muestra por pantalla
print(f"La media es: {sumatoria / LIMITE_SUP}")
    
print("##########")

###############################################################################################################

# ACTIVIDAD 10
# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

print("ACTIVIDAD 10")

# Solicita un número
numero = int(input("Ingreso un número: "))

# Determina si el número ingresado es negativo
if(numero < 0):
    signo = -1
else:
    signo = 1

# Inicializa variables
invertido = 0
numero_original = numero
numero = abs(numero)

# Invierte el número ingresado
while (numero > 0):
    ultimo_digito = numero % 10
    invertido = invertido * 10 + ultimo_digito
    numero = numero // 10

invertido = invertido * signo

# Muestra por pantalla
print(f"El número {invertido} es el invertido del número ingresado {numero_original}")

print("##########")

###############################################################################################################