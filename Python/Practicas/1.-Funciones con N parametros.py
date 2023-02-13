def producto(*numeros:int)-> int:
    print(numeros)
    total = 0
    for n in numeros:
        total += n
    return total
print(producto(1,2,3,4,5,6,7,8,9))