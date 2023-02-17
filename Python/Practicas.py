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


