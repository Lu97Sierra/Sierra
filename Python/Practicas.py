# Escribir un programa que almacene las matrices en una tupla y muestre
# en pantallas su producto, el producto debe estar dado en listas anidadas.

tupla1 = ((1,2,3),(4,5,6))
tupla2 = ((-1,0),(0,1),(1,1))
respuesta = [[0,0],[0,0]]
for i in range(len(tupla1)):
    for w in range(len(tupla2[0])):
        for m in range(len(tupla2)):
            respuesta[i][w] += tupla1[i][m] * tupla2[m][w]
for i in range(len(respuesta)):
    respuesta[i]= tuple(respuesta[i])
respuesta = tuple(respuesta) 
for i in range(len(respuesta)):
    print(respuesta[i])