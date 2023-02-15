# def mifuncion(x):
#     return 2*x
# y = mifuncion(3)
# print(y)

# def resta(a,b):
#     return a-b 

# print(resta(b=10, a=2))


# def suma(a,b,c=5):
#     return a+b+c

# print(suma(0,0,4))


# lista = [1,5,7,8]
# def suma(numeros):
#     total = 0
#     for n in numeros:
#         total+= n
#     return total
# print(suma(lista))

# def suma(*numeros):
#     print(numeros)
#     print(type(numeros))
#     total = 0
#     for n in numeros:
#         total += n
#     return total
# print(suma(1,2,3,4,5,6,7,8,9))

# def suma(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     suma = 0
#     for key, value in kwargs.items():
#         print(key, value)
#         suma += value
#     return suma
# print(suma(b=2,c=4,a=4,Pedro=2))

# def suma(**kwargs):
#     suma= 0
#     for key, value in kwargs.items():
#         print(key, value)
#         suma+= value
#     return suma

# # di = {'a':10, 'b':12, 'c':13}
# # print(suma(**di))

# # def sumaMedia(a,b,c):
# #     suma = a,b,c
# #     media = suma/3
# #     return suma, media,10

# # print(sumaMedia(1,2,3))
# # sumaResultado,sumaResultadoMedia,x = sumaMedia(1,2,3)
# # print(sumaResultado, sumaResultadoMedia,x)


# # def miFuncionSuma(a,b):
# #     """
# #     Descripcio util de la funcion, como dene ser usada, que parametros
# #     """

# #     return a+b
# # help(miFuncionSuma)
# # print(miFuncionSuma.__doc__)

# def multiplicar(numero: int) ->int:
#     return numero * 3
# print(multiplicar("5.8"))

# def funcion(a,b,*args,**kwargs):
#     print(a)
#     print(b)
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(key,value)

# funcion(10,1,2,2,4,58,7,8,9,6,4,1,54,x=4,c=3,m=10)



# numeros = list(range(1,101,1))
# print(numeros)
# def suma(*numeros):
#     suma = 0
#     for n in numeros:
#         suma+=n
#     return suma
# print(suma(*numeros))


x=lambda a:print(a+10)
x(10)



(lambda a:print(a+10))(90)

(lambda *n:print(sum(n)))(*list(range(0,101,1)))


def multiplicador(n):
    return lambda a: print(a*n)
duplicador = multiplicador(2)
duplicador(800)
triplicador = multiplicador(3)
triplicador(800)


suma = None
try:
    suma=1+"1"
except Exception as e:
    print(e)
else:
    print(suma)
finally:
    print(suma)

#assert

def suma(a,b):
    assert(type(a)==int)
    assert(type(b)==int)
    print(a+b)
suma(1.2,2)
print("Fin.")

