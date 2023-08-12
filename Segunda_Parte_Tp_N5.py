import Tp_N5
import datetime
import random
import time
#2. Coloque el módulo del ejercicio anterior dentro de un paquete. En un
#módulo que esté fuera de ese paquete, cree una función de suma de
#decimales que redondee el resultado haciendo uso de la función
#redondear() del paquete recién creado.
"""
def Suma_y_redondeo(Numero1, Numero2):
    Numero1=float(input("Insertar un numero1:"))
    Numero2=float(input("Insertar un numero2:"))

    Numero3= Numero1 + Numero2

    print(Tp_N5.Redondear(Numero3))


Tiempo_inicio1 = time.time()

Suma_y_redondeo(3, 65)

Tiempo_final1 = time.time()


print ("El programa tardo en ejecutarse", (Tiempo_final1 - Tiempo_inicio1), "segundos")
"""
        #Error de codigo

#3. Usando el módulo datetime, escribe un programa que muestre la fecha
#y hora actuales del sistema.
"""
Tiempo_inicio2= time.time()
Hora_actual= datetime.datetime.now()


print(Hora_actual)

Tiempo_final2= time.time()

print ("El programa tardo en ejecutarse", (Tiempo_final2 - Tiempo_inicio2), "segundos")

"""

#4. Escriba un programa que devuelva un número par al azar entre 2 y 10
#(pista: para comprobar si se pueden generar todos los números, pruebe
#ejecutar el programa dentro de un ciclo infinito).

"""
Tiempo_inicial3= time.time()

while True:
    aleatorio= random.randint(2,10)
    if aleatorio % 2 == 0:
        print (aleatorio)
        break
        
Tiempo_final3= time.time()

print("El programa tardo en ejecutarse", (Tiempo_final3 - Tiempo_inicial3), "segundos")

"""

#5. Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
#para la adivinación o para buscar consejo. Su mecanismo es muy simple:
#ante una pregunta del usuario, la bola responde con una de 8 posibles
#respuestas
"""
Tiempo_inicio4= time.time()

def BolaMagica():
        aleatorio = random.randint(1,8)

        if aleatorio == 1:
            print ("Es seguro que sí")
        
        elif aleatorio ==2:
            print ("Las chances son buenas")
        elif aleatorio ==3:
            print ("Puedes contar con ello")
        elif aleatorio ==4:
            print ("Pregúntame de nuevo más tarde")
        elif aleatorio ==5:
            print ("Concéntrate y pregunta de nuevo")
        elif aleatorio ==6:
            print ("No veo con claridad, intenta de nuevo")
        elif aleatorio ==7:
            print ("Mi respuesta es no")
        else:
            print ("Mis fuentes me dicen que no")

BolaMagica()

Tiempo_final4= time.time()

print ("El programa tardo en ejecutarse", (Tiempo_final4 - Tiempo_inicio4), "segundos")

"""
#6. Encuentre el tiempo de ejecución de los programas de los ejercicios
#anteriores (pista: use el módulo time)


#Hora y fecha de la computadora = 0.0029299259185791016 segundos

#Numero aleatorio par = 0.0 segundos

#Bola Magica = 0.0009744167327880859 segundos