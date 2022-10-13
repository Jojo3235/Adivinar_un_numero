import random as rnd
import sys                              #Importamos las librerias y funciones necesarias y también las funciones creadas en el otro archivo (pruebas.py)
from definiciones import acertar,limites,pedir_numero,pedir_numero_sin_lim    
bounds=input("¿Quieres modificar los límites inferior y superiro del juego?(S/N): ") #Preguntamos si quiere cambiar los límites predeterminados del programa
if bounds.lower() == "s":                 #En caso afirmativo continuamos a la siguiente pregunta
    random_bounds=input("¿Quieres que los límites sean aleatorios?(S/N): ")         #Preguntamos si quiere que los límites sean aleatorios
    if random_bounds.lower() == "s":        #En caso afirmativo establecemos el primer límite como un valor aleatorio()
        intervalo=pedir_numero_sin_lim("¿Cuál quieres que sea el intervalo máximo entre los límites(>=50)?: ")
        if int(intervalo)>=50:
            lim1_rand=rnd.randint(0,200)            #El primer límite es aleatorio y el segundo es el primero + un número aleatorio entre 30 y el valor pedido previamente
            lim2_rand=lim1_rand+rnd.randint(30, intervalo)
            rand_bound_num=limites(lim1_rand,lim2_rand)
            acertar(rand_bound_num,lim1_rand,lim2_rand)       #Llamamos a la función acertar del archivo pruebas con el valor aleatorio dentro del límite
        else:
            print("El número introducido es menor a 50")
    else:                    #Si quiere establecer el mismo los límites le preguntamos por ambos
        lim1=pedir_numero_sin_lim("Elige el primer límite")
        lim2=pedir_numero_sin_lim("Elige el segundo límite")
        num_lim_eleg=limites(lim1,lim2)     #Definimos el número a adivinar llamando a la función limites del otro archivo con los valores de ambos límties pedidos previamente como variables
        acertar(num_lim_eleg,lim1,lim2)           #Llamamos la función acertar con el numero definido dos líneas arriba como variable
else:           #Si quiere los valores predeterminados entre 0 y 100
    num=rnd.randint(0,100)              #Elige un número entre 0 y 100 
    pedir_numero("Adivina un número",0,100)        #Imprimimos el intervalo entre 0 y 100
    acertar(num,0,100)        #Llamamos a la función acertar de nuevo con un número aleatorio entre 0 y 100 como variable