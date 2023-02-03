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


# tupla = (1,2,3)
# print(tupla)
# tupla = 1,2,3
# print(type(tupla))
# print(tupla)
# #tupla[0]=5                     Marcaria error ya que las tuplas son inmutables
# tupla = 1,2,('a','b'),3
# print(tupla)
# print(tupla[2][0])
# tupla = 1,2,3
# x,y,z = tupla
# print(x,y,z)
# lista=[1,2,3]
# tupla = tuple(lista)

# for t in tupla:
#     print(t)

# tupla = (2,2,2,2,2,2,2,2,3,6,5)

# print(tupla.count(2))
# print(tupla.index(3))
# print(tupla.index(5,5))

# lista = [1,2,3,4,5]
# lista = list("1234")
# print(lista)
# lista = [1,"Hola",3.67,[1,2,3]]
# print(lista)
# print(lista[0])
# lista[3][2]=100
# print(lista[3][2])


# l = [1,2,3,4,5,6,7,8,9]
# l2 = l[0:4]
# l3=[0,0,0]
# l[0:3] = l3
# l+=l3
# print(l)

# x,y,z = l3
# print(x,y,z)
lista=[1,2,3,4]
for elemento in lista:
    print(elemento)

for index,l in enumerate(lista):
    print(index,l)

lista2 = ["c","z","a"]

for l1,l2 in zip(lista,lista2):
    print(l1,l2)

for i in range(0,len(lista)):
    print(lista[i])

l = [2,3]
l.append(3)
print(l)
l.extend([1,2,3,4])
print(l)
l.insert(0,100)
print(l)
l.remove(100)
print(l)
l.pop()
print(l)

l.reverse()
print(l)

l.sort()
print(l)
l.sort(reverse=True)
print(l)
