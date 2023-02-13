
print("¿En que formato quiere la fecha?")
print("1.- YYYY/MM/DD")
print("2.- MM/DD/YYYY")
num = input()
if num == 1:
    from datetime import date
    now = date.today()  
    print(now)
else:
    from datetime import date
    now = date.today()  
    print(now.__format__("%m-%d-%Y"))