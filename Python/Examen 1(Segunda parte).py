# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra
# que contiene y su frecuencia. Escribir otra funcion que reciba el diccionario generado con la funcion
# anterior y devuelva una tupla con las palabras mas repetidas y su frecuencia.

def contar_palabras(cadena):
    palabras = cadena.split()
    diccionario = {}
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario

def palabras_mas_repetidas(diccionario):
    max_freq = max(diccionario.values())
    palabras = [key for key, value in diccionario.items() if value == max_freq]
    return tuple(sorted([(palabra, max_freq) for palabra in palabras]))

cadena = input("Ingrese una cadena: ")
contar = contar_palabras(cadena)
repetir = palabras_mas_repetidas(contar)
print(repetir)

# -----------------------------------------------------------------------------------------------------------------------
# Crear 10 listas de elementos que dividan los numeros del 1 al 100
# Crear una funcion que reciba un numero entero N entre 0 y 9 capturado por el usuario y arroje como
# resultado la suma de todos los elementos en la posicion N de las 10 listas.
# Guardar dicho resultado en una varibale e imprimirlo en pantalla.

listas = []
for i in range(10):
    inicio = i * 10 + 1
    fin = inicio + 9
    lista = list(range(inicio, fin+1))
    listas.append(lista)

def suma_posicion_n(n, listas):
    suma = 0
    for lista in listas:
        suma += lista[n]
    return suma

n = int(input("Ingrese un número entero entre 0 y 9: "))
resultado = suma_posicion_n(n, listas)
print("La suma de todos los elementos en la posición", n, "de las 10 listas es:", resultado)

#----------------------------------------------------------------------------------------------------------------------------
# Crear una funcion que reciba 2 listas de no necesariamente la misma longitud y devuelva 2 listas, la primera
# lista tendra los elementos que coinciden entre las 2 listas, la segunda lista tendra los elementos
# que coinciden entre las 2 listas.

def coincidencia_listas(lista1, lista2):
    coincidencias = []
    no_coincidencias = []
    for elemento in lista1:
        if elemento in lista2:
            coincidencias.append(elemento)
        else:
            no_coincidencias.append(elemento)
    for elemento in lista2:
        if elemento not in lista1:
            no_coincidencias.append(elemento)
    return coincidencias, no_coincidencias

coincidencias, no_coincidencias = coincidencia_listas(['a','b',2,3],['c','d',3,4])
coincidencias = set(coincidencias)
no_coincidencias = set(no_coincidencias)
print("Coincidencias:", coincidencias)
print("No coincidencias:", no_coincidencias)
print("-------------------------------------------------------")
coincidencias, no_coincidencias = coincidencia_listas(['a','b',2,3],['c','d',4])
coincidencias = set(coincidencias)
no_coincidencias = set(no_coincidencias)
print("Coincidencias:", coincidencias)
print("No coincidencias:", no_coincidencias)
print("-------------------------------------------------------")
coincidencias, no_coincidencias = coincidencia_listas(['a','b',2,2,3],['c','d',2,'a',4])
coincidencias = set(coincidencias)
no_coincidencias = set(no_coincidencias)
print("Coincidencias:", coincidencias)
print("No coincidencias:", no_coincidencias)


