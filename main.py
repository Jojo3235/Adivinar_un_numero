import random as rnd
import sys                              #Importamos las librerias necesarias y también las funciones creadas en el otro archivo (pruebas.py)
from pruebas import acertar,limites     
bounds=input("¿Quieres modificar los límites inferior y superiro del juego?(S/N): ") #Preguntamos si quiere cambiar los límites predeterminados del programa
if bounds.lower() == "s":                 #En caso afirmativo continuamos a la siguiente pregunta
    random_bounds=input("¿Quieres que los límites sean aleatorios?(S/N): ")         #Preguntamos si quiere que los límites sean aleatorios
    if random_bounds.lower() == "s":        #En caso afirmativo establecemos el primer límite como un valor aleatorio()
        intervalo=input("¿Cuál quieres que sea el intervalo máximo entre los límites(>=50)?: ")  #Preguntamos por el intervalo entre límites máximo que quiere el usuario
        try:
            intervalo=int(intervalo)
        except:                 #Con esta excepción controlamos que sea un número el input
            print("No se ha introducido un número o el número introducido es menor a 50", file=sys.stderr())
            sys.exit()
        if int(intervalo)>=50:
            lim1_rand=rnd.randint(0,200)            #El primer límite es aleatorio y el segundo es el primero + un número aleatorio entre 30 y el valor pedido previamente
            lim2_rand=lim1_rand+rnd.randint(30, intervalo)
            rand_bound_num=limites(lim1_rand,lim2_rand)
            print("Adivina el número entre {} y {}".format(lim1_rand,lim2_rand))    #Imprimimos los límites del intervalo a adivinar el número
            acertar(rand_bound_num)       #Llamamos a la función acertar del archivo pruebas con el valor aleatorio dentro del límite
        else:
            print("El número introducido es menor a 50")
            pass
    else:                    #Si quiere establecer el mismo los límites le preguntamos por ambos
        lim1=input("Elige el primer límite: ")
        try:                            #Con estas excepciones controlamos que sean números enteros los 2 límites
            lim1=int(lim1)
        except:               
            print("No se ha introducido ningún número, pruebe de nuevo",
                file=sys.stderr)
            sys.exit()
        lim2=input("Elige el segundo límite: ")
        try:
            lim2=int(lim2)
        except:
            print("No se ha introducido un número, pruebe de nuevo",
                file=sys.stderr)
            sys.exit()
        num_lim_eleg=limites(lim1,lim2)     #Definimos el número a adivinar llamando a la función limites del otro archivo con los valores de ambos límties pedidos previamente como variables
        print("Adivina el número entre {} y {}".format(lim1,lim2))  #Imprimimos el intervalo aadivinar
        acertar(num_lim_eleg)           #Llamamos la función acertar con el numero definido dos líneas arriba como variable
else:           #Si quiere los valores predeterminados entre 0 y 100
    num=rnd.randint(0,100)              #Elige un número entre 0 y 100 
    print("Adivina el número entre 0 y 100")        #Imprimimos el intervalo entre 0 y 100
    acertar(num)        #Llamamos a la función acertar de nuevo con un número aleatorio entre 0 y 100 como variable