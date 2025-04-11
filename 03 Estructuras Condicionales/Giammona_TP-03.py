################################################################################################

# Actividad 1
# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# Solicitar la edad al usuario
edad = int(input("Ingrese la edad: ")) 
# Determinar si el usuario es mayor de edad
if(edad > 18):
    print("Es mayor de edad")

#################################################################################################

# Actividad 2
# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

#Solicitar la nota al usuario
nota = float(input("Ingrese su nota: "))
#Determinar si la nota es mayor o igual a seis
if(nota >= 6):
    print("Aprobado")
else:
    print("Desaprobado")

##################################################################################################

# Actividad 3
# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

# Solicitar al usuario el ingreso de un número par
num = int(input("Ingrese un número par: "))
# Determinar si el numero ingresado es par e imprimir mensaje por pantalla
if(num % 2 == 0):
        print("Ha ingresado un número par")
else: 
    print("Por favor, ingrese un número par")

###################################################################################################

# Actividad 4
# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

# Solicitar al usuaro su edad
edad = int(input("Ingrese su edad: "))
# Determinar a que categoría pertenece
if(edad < 12):
    print("Niño/a: menor de 12 años")
elif(edad >=12 and edad < 18):
    print("Adolescente: mayor o igual que 12 años y menor que 18 años.")
elif(edad >= 18 and edad < 30):
    print("Adulto/a joven: mayor o igual que 18 años y menor que 30 años.")
else:
    print("Adulto/a: mayor o igual que 30 años.")

##############################################################################################

# Actividad 5
# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

# Solicitar contraseña al usuario
contrasena = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
# Evaluar longitud de la contraseña e imprimir mensaje por pantalla
min_len = 8
max_len = 14
contrasena_len = len(contrasena)
if(contrasena_len >= 8 and contrasena_len <= 14):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

###################################################################################################

# Actividad 6
# El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
# siguiente:
# from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# mean(mi_lista)
# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria.

# Definir la lista numeros_aleatorios:
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#Calcular los valores estadísticos media, mediana y moda
from statistics import mode, median, mean
media = float(mean(numeros_aleatorios))
mediana = float(median(numeros_aleatorios))
moda = float(mode(numeros_aleatorios))
#Determminar la forma de la distribución normal
if(media > mediana and mediana > moda):
    print("La distribución normal tiene sesgo positivo")
elif(media < mediana and mediana < moda): 
    print("La distribución normal tiene sesgo negativo")
elif(media == mediana and mediana == moda):
    print("La distribución normal no tiene sesgo")
else:
    print("No es una distribución normal")

######################################################################################################

# Actividad 7
# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

# Solicitar una frase o palabra al usuario
palabra = input("Ingrese una frase o palabra: ")
# Definir cual es la última letra
ultima_letra = palabra [-1]
# Definir si se debe agregar un signo de exclamación e imprimir por pantalla
if(ultima_letra=="a" or ultima_letra=="e" or ultima_letra=="i" or ultima_letra=="o" or ultima_letra=="u"):
    print(f"{palabra}!")
else:
    print(f"{palabra}")

############################################################################################################

# Actividad 8
# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# Solicitar al usuario que ingrese su nombre y la opción para imprimir el nombre
nombre = input("Ingrese su nombre: ")
print("Elija una de las siguientes opciones para imprimir su nombre por pantalla")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.") 
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
opcion = int(input("Ingrese un número dependiendo de la opción que desee: "))
# Definir el formato de impresión según la opción seleccionada
if(opcion == 1):
    nombre_mayuscula = nombre.upper()
    print(f"{nombre_mayuscula}")
elif(opcion == 2):
    nombre_minuscula = nombre.lower()
    print(f"{nombre_minuscula}")
elif(opcion == 3):
    nombre_titulo = nombre.title()
    print(f"{nombre_titulo}")

###############################################################################################################

# Actividad 9
# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# Solicitar al usuario la magnitud de un terremoto
magnitud = int(input("Ingrese la magnitud del terremoto en la escala de Richter (1 a 10): "))
# Evaluar la magnitud del terremoto e imprimir mensaje por pantalla
if(magnitud <=3):
    print("Menor que 3: Muy leve (imperceptible).")
elif(magnitud >= 3 and magnitud < 4):
    print("Mayor o igual que 3 y menor que 4: Leve (ligeramente perceptible).")
elif(magnitud >= 4 and magnitud < 5):
    print("Mayor o igual que 4 y menor que 5: Moderado (sentido por personas, pero generalmente no causa daños).")
elif(magnitud >= 5 and magnitud < 6):
    print("Mayor o igual que 5 y menor que 6: Fuerte (puede causar daños en estructuras# débiles).")
elif(magnitud >= 6 and magnitud < 7):
    print("Mayor o igual que 6 y menor que 7: Muy Fuerte (puede causar daños significativos).")
elif(magnitud >= 7):
    print("Mayor o igual que 7: Extremo (puede causar graves daños a gran escala).")

####################################################################################################################

# Actividad 10
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

# Solicitar al usuario en que hemisferio se encuentra, el mes y el día
hemisferio = input("Ingrese en que hemisferio se encuentra (N/S): ")
mes = int(input("Ingrese el mes del año (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

# Calcular la fecha como un número decimal
fecha_actual = mes + dia / 100

# Dterminar e imprimir por pantalla la estación en la que se encuentra el usuario
if(hemisferio == "S"):
    if(3.21 <= fecha_actual < 6.21):
        estacion = "otoño"
    elif(6.21 <= fecha_actual < 9.21):
        estacion = "invierno"
    elif(9.21 <= fecha_actual < 12.21):
        estacion = "primavera"
    else:
        estacion = "verano"

else:
    if(3.21 <= fecha_actual < 6.21):
        estacion = "primavera"
    elif(6.21 <= fecha_actual < 9.21):
        estacion = "verano"
    elif(9.21 <= fecha_actual < 12.21):
        estacion = "primavera"
    else:
        estacion = "invierno"

print(f"El {dia}.{mes} en el hemisferio {hemisferio} es {estacion}")

######################################################################################################


