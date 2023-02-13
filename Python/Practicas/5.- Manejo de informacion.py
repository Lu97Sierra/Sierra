def info(**kwargs):
    suma = 0
    for key, value in kwargs.items():
     print(key, value)
    return ('')
    
print(info(Mesa=2,Sillas=4,Cuchillos=4,Cucharas=2))