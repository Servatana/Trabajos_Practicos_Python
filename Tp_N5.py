#1. Escriba una función redondear() que permita redondear un número
#decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
#entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
#anterior (3). 

def Redondear():
    Numero3= float(input("Inserte un numero:"))
    if Numero3 >3.5:
        print(int(Numero3)+1)
    else:
        print (int(Numero3))


Redondear()
