def num(nom):
    di = {'0':'Cero', '1':'Uno','2':'Dos','3':'Tres','4':'Cuatro','5':'Cinco','6':'Seis','7':'Siete','8':'Ocho','9':'Nueve','10':'Diez','11':'Once','12':'Dosce','13':'Trece','14':'Catorce','15':'Quince','16':'Diesises','17':'Diesisiete','18':'Dieciocho','19':'Diescinueve','20':'Veinte'}
    print(di.get(str(nom)))
num(input("Teclee un numero del 0 al 20:"))

