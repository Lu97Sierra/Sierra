# #Tipos de datos 
# #Numericos

# #Entero
# integer = 1
# integerNegative = -1
# zero = 0
# print(type(integer),integer,id(integer))
# print(type(integerNegative),integerNegative, id(integerNegative))
# print(type(zero),zero,id(zero))

# #Float
# floatNum = 3.5
# floatNegative = -3.5
# floatZero = 3.0

# print(type(floatNum),floatNum,id(floatNum))
# print(type(floatNegative),floatNegative, id(floatNegative))
# print(type(floatZero),floatZero,id(floatZero))  

# #Complejos
# complexNum = 5j
# complexNum2 = 2 + 4j
# print(type(complexNum),complexNum,id(complexNum))
# print(type(complexNum2),complexNum2,id(complexNum2))

# intToFloat = float(integer)
# floatToInt = int(floatNum)
# floatToComplex = complex(floatNegative)
# print(type(intToFloat),intToFloat)
# print(type(floatToInt),floatToInt)
# print(type(floatToComplex),floatToComplex)

# #Booleanos

# y = 5
# x = 10
# print(bool(x==y))
# x = None
# print(bool(x))
# x=()
# print(bool(x))
# x=(1,2)
# print(bool(x))
# x={}
# print(bool(x))
# x=0.0
# print(bool(x))
# x=0.1
# print(bool(x))
# x='CadenaNoVacia'
# print(bool(x))
# x=''
# print(bool(x))

# #Cadenas

# print(type('Hello'),'Hello')
# saludo = 'Saludo'
# despedida =  'Adios'
# print(saludo)
# print(saludo,end=',')

# #Interpolacion

# print(f'Saludo:{saludo}, Despedida:{despedida}')
# print(""""
# Esto 
# Es
# Un
# Texto
# Multilinea
# """
# )
# print(f"""Saludo
# {saludo}
# Despedida
# {despedida}
# """)

# for letras in saludo:
#     print(letras)

#     #Revertir cadena

# print(saludo[::-1])
# print(saludo)
# print(''.join[reversed(saludo)])