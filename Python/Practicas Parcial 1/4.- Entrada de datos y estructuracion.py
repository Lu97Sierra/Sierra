
di = {}
print("Ingrese asignatura:")
asig = input()
print("Ingrese creditos de la asignatura:")
cred = input()
di[asig] = cred
respuesta = input("¿Desea ingresar otro asignaura? 'si' o 'no': ")

while respuesta == "si":
    print("Ingrese asignatura:")
    asig = input()
    print("Ingrese creditos de la asignatura:")
    cred = input()
    di[asig] = cred
    respuesta = input("¿Desea ingresar otro asignaura? 'si' o 'no': ")


total_creditos = 0
for asig, cred in di.items():
    print(asig, 'tiene', cred, 'créditos')
    total_creditos += int(cred)
print('Número total de créditos del curso: ', total_creditos)