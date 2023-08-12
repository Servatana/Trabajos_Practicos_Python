#1. Escriba una función que muestre todos los números primos entre 1 y un número n que es 
#       ingresado por parámetro
"""def Numeros_Primos():
    NumeroBase=int(input("Inserte un numero:"))
    for X in range (2, NumeroBase-1):
        if NumeroBase % X == 0:
            print (NumeroBase,"No es un numero primo")
            break
        else:
            print (NumeroBase, "es un numero primo!")
            break


Numeros_Primos ()
"""
#2. Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta
#que el usuario ingrese ‘salir’. Cada vez que se ingrese un condimento, muestre un mensaje
#avisando que ya se agregó el condimento al sándwich. Escriba versiones diferentes del
#programa de acuerdo a estos criterios:
#   • Use un test condicional en el ciclo while para detener la ejecución.
#   • Use un test condicional dentro del ciclo para decidir si continuar la ejecución. 
#
"""
def Armar_un_sandwich():
    Sandwich=[]
    Texto= str()
    while True:
        Texto= str(input("Inserta un ingrediente al sandwith:"))

        if Texto == "Salir":
            print ("Sandwich completado!")
            break
        else:
            Sandwich.append(Texto)
            print (Sandwich)

Armar_un_sandwich()
"""
#3. A) Remera: Escriba una función “hacer_remera()” que tome como parámetros un
#tamaño y el mensaje que debería ir impreso en la remera. La función debe mostrar un mensaje
#describiendo el tamaño de la remera y el mensaje impreso en ella. Llame la función una vez
#usando argumentos por posición. Llámela una segunda vez usando argumentos por clave.
"""
def hacer_remera(Tamaño, MensajeDeRemera):
    while True:
        if Tamaño in ["S", "M", "L", "XL", "XXL"]:
            print("Su camiseta de talla", Tamaño, "será impresa. Con su mensaje", MensajeDeRemera)
            break
        else:
            print("Por favor, inserte un valor posible. Puede seleccionar S, M, L, XL o XXL.")
            Tamaño = input("Inserte un tamaño para su remera:")

hacer_remera("M", "El wiwi")
"""
   
#B)Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por
#defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par de remeras, la primera con los
#valores por defecto, y la segunda con valores diferentes. 
"""
def hacer_remera(Tamaño="L",MensajeDeRemera="Me gusta Python"):
    
    print("Su camiseta de talla:", Tamaño, "será impresa. Con su mensaje:", MensajeDeRemera)
    
hacer_remera()

hacer_remera("S","Ayuda, no quiero seguir con el proyecto D:")
"""

#4 Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros
#de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo
#número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …)
"""
Lista= [0,1]
NuevoValor=0
contador =0
while  contador<10:
  NuevoValor = Lista[-1] + Lista[-2]

  Lista.append(NuevoValor)
  contador ++1 
 
print(Lista)

"""