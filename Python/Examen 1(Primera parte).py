#-------------------------
#Numeros de control: 18100233, 16100172
#------------------------------------



# Dividir un cierto entero n por otro entero m hasta n = 1 obteniendo una secuencia de numeros, cada numero de esta secuencia
# almacenados en una lista, las secuencias deben cumplir hasta llegar a n = 1, si n =1 se debera
# imprimir la secuencia entera e imprimir en pantalla "secuencia invalida"

# n = int(input("Ingrese el valor de n: "))
# m = int(input("Ingrese el valor de m: "))

# secuencia = [n]  # Inicializar la lista con el valor inicial de n

# while n != 1:
#     if n % m == 0:
#         n //= m  # División entera de n por m
#         secuencia.append(n)
#     else:
#         print("secuencia invalida")
#         break

# if n == 1:
#     print("Secuencia: ", secuencia)

#----------------------------------------------------------------------------------------------------------------------------------------
# Se requiere hacer un programa que indique cual es mayor de 2 numeros con 3 digitos (cada uno) pero hay
# un problema con la interfaz y esta toma los numeros al reves

# Leer los números como cadenas de texto e invertirlos
# num1_str = input("Ingrese el primer número de 3 dígitos: ")
# num2_str = input("Ingrese el segundo número de 3 dígitos: ")
# resultado_invertido1 = num1_str[::-1]
# resultado_invertido2 = num2_str[::-1]

# # Convertir los números a enteros
# num1 = int(resultado_invertido1)
# num2 = int(resultado_invertido2)

# # Comparar los números
# if num1 > num2:
#     resultado = f"El resultado es: {num1}"
# elif num1 < num2:
#     resultado = f"El resultado es: {num2}"
# else:
#     resultado = f"Los números son iguales"

# # Imprimirlo
# print(resultado)

#------------------------------------------------------------------------------------------------------
# Problema extra

# Una chocolateria lanzara un nuevo producto el cual viene presentado en barras de N segmentos.
# Las barras solo vienen en tamaños que son potencia de 2, es decir 1,2,4,8,16...
# Realizar un programa para realizar una prueba de calidad de dicho producto pero para ello tienes que
# probar al menos k segmentos.
# El problema es que la barra solo se puede partir a la mitad.
# Dicho programa determinara el numero de veces que quebraras la barra para obtener exactamente K segmentos.
# La salida sera el tamaño de barrra que se tendra que pedir para tomar los K segmentos y el segundo nnmero 
# es el menor numero de veces que tendras que romper la barra

import math

# Leer los valores de N y K desde el usuario
N = int(input("Ingrese el tamaño de la barra (potencia de 2): "))
K = int(input("Ingrese el número de segmentos a probar (menor o igual a N): "))

# Verificar que N y K son potencias de 2 y K <= N
if not (math.log2(N).is_integer() and math.log2(K).is_integer() and K <= N):
    print("Entrada inválida. N y K deben ser potencias de 2 y K debe ser menor o igual a N.")
else:
    if K == N:
        print(f"La prueba de calidad fue exitosa con una sola barra de tamaño {N}.")
    else:
        # Dividir la barra en dos partes iguales hasta obtener K segmentos
        veces_dividida = 0
        while N > K:
            N //= 2
            veces_dividida += 1

        # Imprimir el tamaño de la barra y el número de veces que se dividió
        print(f"Se necesita una barra de tamaño {K} para obtener {K} segmentos.")
        print(f"La barra se tuvo que dividir {veces_dividida} veces.")





