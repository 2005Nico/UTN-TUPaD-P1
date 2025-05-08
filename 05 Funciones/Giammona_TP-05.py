###########################################################################################################
# ACTIVIDAD 1
# Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

lista= list(range(4,101,4))
print(lista)

###########################################################################################################
# ACTIVIDAD 2
# Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!

lista = ["futbol", "jardín", "familia", "UTN", "Funes"]
print(lista[3], lista[-2])

############################################################################################################
# ACTIVIDAD 3
# Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
# ejemplo:
# lista_vacia = []

lista = []
print(lista)
lista.append("uno")
lista.append("dos")
lista.append("tres")
print(lista)

#############################################################################################################
# ACTIVIDAD 4
# Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!
# animales = ["perro", "gato", "conejo", "pez"]

animales = ["perro", "gato", "conejo", "pez"]
print(animales)
animales.remove("gato")
animales.remove("pez")
animales.append("loro")
animales.append("oso")
print(animales)
print("##########################")
animales = ["perro", "gato", "conejo", "pez"]
print(animales)
animales.pop(-1)
animales.insert(3, "oso")
animales.pop(-3)
animales.insert(1, "loro")
print(animales)

##############################################################################################################
# ACTIVIDAD 5
# Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# El programa calcula el máximo de los numeros que integran la lista definida en numeros y lo elimina.  
# Además muestra por pantalla la lista modificada.

###############################################################################################################
# ACTIVIDAD 6
# Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.

lista = list(range(10,31,5))
print(lista[0], lista[1])

################################################################################################################
# ACTIVIDAD 7
# Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.
# autos = ["sedan", "polo", "suran", "gol"]

autos = ["sedan", "polo", "suran", "gol"]
print(autos)
autos.pop(1)
autos.pop(1)
autos.insert(1, "citroen_C3")
autos.insert(2, "megane")
print(autos)

################################################################################################################
# ACTIVIDAD 8
# Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

dobles = []
print(dobles)
dobles.append(2*5)
dobles.append(2*10)
dobles.append(2*15)
print(dobles)

#################################################################################################################
# ACTIVIDAD 9
# Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# print(compras)
posicion_2_compras = compras[2]
# print(posicion_2_compras)
posicion_2_compras.append("jugo")
# print(posicion_2_compras)
# print(compras)
posicion_1_compras = compras[1]
# print(posicion_1_compras)
posicion_1_compras.remove("fideos")
# print(posicion_1_compras)
posicion_1_compras.insert(1, "tallarines")
# print(posicion_1_compras)
# print(compras)
posicion_0_compras = compras[0]
# print(posicion_0_compras)
posicion_0_compras.remove("pan")
# print(posicion_0_compras)
print(compras)

###############################################################################################################
# ACTIVIDAD 10
# Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

lista = []
lista.append(15)
lista.append(True)
posicion_2 = []
posicion_2.append(25.5)
posicion_2.append(57.9)
posicion_2.append(30.6)
lista.append(posicion_2)
lista.append(False)
print(lista)