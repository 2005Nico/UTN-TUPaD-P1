# ACTIVIDAD 1
# Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

# Definición de funciones
def imprimir_hola_mundo(x):
    return print(x)
    
# Programa principal
imprimir_hola_mundo("Hola mundo!")

#####################################################################################

# ACTIVIDAD 2
# Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

# Definición funciones
def saludar_usuario(a):
    return print(f"Hola {a} !")

# Programa principal
nombre = (input("Ingrese su nombre: "))
saludar_usuario(nombre)

#####################################################################################

# ACTIVIDAD 3
# Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# Definición funciones
def informacion_personal(a,b,c,d):
    return print(f"Soy {a} {b}, tengo {c} años y vivo en {d}")

# Programa principal
nombre = (input("Ingrese su nombre: "))
apellido = (input("Ingrese su apellido: "))
edad = (input("Ingrese su edad: "))
residencia = (input("Ingrese su residencia: "))

informacion_personal(nombre,apellido,edad,residencia)

#######################################################################################

# ACTIVIDAD 4
# Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
# dio como parámetro y devuelva el área del círculo. calcular_peri-
# metro_circulo(radio) que reciba el radio como parámetro y devuel-
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
# bas funciones para mostrar los resultados.

# Definición de funciones
def leer_decimal_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = float(input(f"{mensaje}: "))
    while n < min or n > max:
        n = float(input(f"ERROR. {mensaje}: "))
    return n

def imprimir_resultados(a,b,c):
    return print(f"Para un radio = {a}, el perímetro = {b} y el área = {c}")

def calcular_perimetro_circulo(r):
    return 3.1416 * r

def calcular_area_circulo(r):
    return 3.1416 * r ** 2


# Programa principal
radio = leer_decimal_validado("Ingrese el radio: ",0)
perimetro = calcular_perimetro_circulo(radio)
area = calcular_area_circulo(radio)
imprimir_resultados(radio,perimetro,area)

########################################################################################

# ACTIVIDAD 5
# Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mos-
# trar el resultado usando esta función.

# Definición de funciones
def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = int(input(f"{mensaje}: "))
    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje}: "))
    return n

def segundos_a_horas(s):
    return s / 3600


# Programa principal
segundos = leer_entero_validado("Ingrese segundos",0)
horas = segundos_a_horas(segundos)
print(f"{segundos} son equivalentes a {horas} horas")

#######################################################################################

# ACTIVIDAD 6
# Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

# Definición de funciones
def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = int(input(f"{mensaje}: "))
    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje}: "))
    return n

def tabla_multiplicar_numero(a,b):   
    return a * b


# Programa principal
numero = leer_entero_validado("Ingrese un número entero positivo",0)
for i in range(1,11):
    num = tabla_multiplicar_numero(numero,i)
    print(f"{numero} x {i} = {num}")

########################################################################################

# ACTIVIDAD 7
# Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado 
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
# de forma clara.

# Definición de funciones
def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = int(input(f"{mensaje}: "))
    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje}: "))
    return n

def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if(b!=0):
        division = a / b
    else:
        division = "No se puede dividir por cero"   
    return suma,resta,multiplicacion,division


# Programa principal
num1 = leer_entero_validado("Ingrese el primer número")
num2 = leer_entero_validado("Ingrese el segundo número")
resultados = operaciones_basicas(num1,num2)
print(resultados)

##################################################################################

# ACTIVIDAD 8
# Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
# ción para mostrar el resultado con dos decimales.

# Definición de funciones
def leer_decimal_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = float(input(f"{mensaje}: "))
    while n <= min or n > max:
        n = float(input(f"ERROR. {mensaje}: "))
    return n

def calcular_imc(a,b):
    return a / b


# Programa principal
peso = leer_decimal_validado("Ingrese su peso",0)
altura = leer_decimal_validado("Ingrese su altura",0)
resultado = round(calcular_imc(peso,altura),2)
print(f"El IMC es {resultado}")

#####################################################################################

# ACTIVIDAD 9
# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

# Definición de funciones
def leer_decimal_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = float(input(f"{mensaje}: "))
    while n < min or n > max:
        n = float(input(f"ERROR. {mensaje}: "))
    return n

def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32


# Programa principal
celsius = leer_decimal_validado("Ingrese una temperatura en celsius")
fahrenheit = round(celsius_a_fahrenheit(celsius),1)
print(f"{celsius} grados celsius equivalen a {fahrenheit} grados fahrenheit")

########################################################################################

# ACTIVIDAD 10
# Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

# Definición de funciones
def leer_decimal_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    n = float(input(f"{mensaje}: "))
    while n < min or n > max:
        n = float(input(f"ERROR. {mensaje}: "))
    return n

def calcular_promedio(a,b,c):
    return (a+b+c) / 3


# Programa principal
num1 = leer_decimal_validado("Ingrese el primer número")
num2 = leer_decimal_validado("Ingrese el segundo número")
num3 = leer_decimal_validado("Ingrese el tercer número")
promedio = round(calcular_promedio(num1,num2,num3),2)
print(f"El promedio es {promedio}")