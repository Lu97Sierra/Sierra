# Escribir un programa que almacene las matrices en una tupla y muestre
# en pantallas su producto, el producto debe estar dado en listas anidadas.

# tupla1 = ((1,2,3),(4,5,6))
# tupla2 = ((-1,0),(0,1),(1,1))
# respuesta = [[0,0],[0,0]]
# for i in range(len(tupla1)):
#     for w in range(len(tupla2[0])):
#         for m in range(len(tupla2)):
#             respuesta[i][w] += tupla1[i][m] * tupla2[m][w]
# for i in range(len(respuesta)):
#     respuesta[i]= tuple(respuesta[i])
# respuesta = tuple(respuesta) 
# for i in range(len(respuesta)):
#     print(respuesta[i])

#---------------------------------------------------------------------------------------------------------------------

# Escribir un programa que guarde en un diccionario, los precios de las frutas 
# de la tabla, preguntar al usuario por la fruta y el numero de kilos
# y muestre en pantalla el precio de ese numero de kilos.
# Si la fruta no esta en el diccionario debe mostrar un mensaje de ello.

# frutas = {'Platano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
# fruta = input('¿Qué fruta quieres? ').title()
# kg = float(input('¿Cuántos kilos? '))
# if fruta in frutas:
#     print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '$')
# else: 
#     print("Lo siento, la fruta", fruta, "no está disponible.")

#----------------------------------------------------------------------------------------------------------------------------------

# Escribir un programa que reciba una cadena de caracteres y regrese un diccionario con cada palabra que contiene y su frecuencia
# Escribir otra funcion que reciba el diccionario y devuelva una tupla con la palabra mas repetida y su frencuencia

# def creador_dict(cadena):
#   '''Recibe una cadena de caracteres y regresa un diccionario con las palabras (keys) y conteo (value)'''
#   lista_1= cadena.split()
#   dict_1={}
#   for i in lista_1:
#     if i in dict_1:
#       dict_1[i] +=1
#     else:
#       dict_1[i]= 1
#   return dict_1

# def contador_dict(dictionario):
#   '''Recibe un diccionario y regresa una tupla: la palabra mas repetida y cuantas veces aparece'''
#   palabra_frecuente= ''
#   cantidad=0
#   for keys,values in dictionario.items():
#     if values > cantidad:
#       cantidad= values
#       palabra_frecuente= keys
#   return palabra_frecuente,cantidad
# entrada=input('Ingrese su cadena de caracteres: ')
# print(creador_dict(entrada))
# print(contador_dict(creador_dict(entrada)))


#-----------------------------------------------------------------------------------------------------------------------

# en una matriz de 5x4 pedir al usuario los valores, en una segunda matriz
# guardar uno si el numero guardado en la misma posicion es multiplo de 3, guardar un 2 si el numero es multiplo 
# de 5 o guardar un 3 si es multiplo de 5 y 3 a la vez, si no se cumple ninguna de las anteriores 
# guardar un cero imprimir ambas matrizes en formato de matriz.


# Inicializar la primera matriz
matriz1 = []
matriz2 = []
for i in range(5):
    filaM1 = []
    filaM2 = []
    for j in range(4):
        valor = int(input(f"Ingrese el valor en la posición ({i}, {j}): "))
        filaM1.append(valor)
        if valor % 3 == 0 and valor % 5 == 0:
            filaM2.append(3)
        elif valor % 3 == 0:
            filaM2.append(1)
        elif valor % 5 == 0:
            filaM2.append(2)
        else:
            filaM2.append(0)

    matriz1.append(filaM1)
    matriz2.append(filaM2)

# Inicializar la segunda matriz

# for i in range(5):
#     fila = []
#     for j in range(4):
#         valor = matriz1[i][j]
#         if valor % 3 == 0 and valor % 5 == 0:
#             fila.append(3)
#         elif valor % 3 == 0:
#             fila.append(1)
#         elif valor % 5 == 0:
#             fila.append(2)
#         else:
#             fila.append(0)
#     matriz2.append(fila)

# Imprimir ambas matrices
print("Matriz 1:")
for fila in matriz1:
    print(fila)

print("Matriz 2:")
for fila in matriz2:
    print(fila) 



# ------------------------------------------------------------------------------
# Conecta 4, van hacer el primer jugar
# El tablero va a hacer de 6x7
# Se debe visualizar el recorrido de las fichas
# El jugador debe elegir la columna donde quiere su ficha
# Gana el priemro que agrupe 4 fichas
# En horizontal, vertical o diagonal
# Si se acaba el espacio en el tablero es empate
# De lo contrario mostrar el msj del ganador





