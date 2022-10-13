import sys
import random as rnd
from definiciones import acertar,limites,pedir_numero_sin_lim,pedir_numero
#3 funciones aquí    
def intervalo_rand(intervalo_min):
    while True:
        intervalo=pedir_numero_sin_lim("Introduce un número para determinar el máximo intervalo entre los límites, mayor a {}".format(intervalo_min))
        try:
            int(intervalo)>=intervalo_min          #Función 3
            lim1_rand=rnd.randint(0,200)            
            lim2_rand=lim1_rand+rnd.randint(30, intervalo)
            rand_bound_num=limites(lim1_rand,lim2_rand)
            acertar(rand_bound_num,lim1_rand,lim2_rand)
        except:
            print("No se ha introducido un número válido", file=sys.stderr)
        else:
            print("El número introducido es menor a {}".format(intervalo_min))
            break


def intervalo_def():
    random_bounds_pregunta=input("¿Quieres que los límites sean aleatorios?(S/N): ")    
    if random_bounds_pregunta.lower() == "s":                #Funcion 2 llamando a la funcion 3
        intervalo_rand(50)
    else:               
        lim1=pedir_numero_sin_lim("Elige el primer límite")
        lim2=pedir_numero_sin_lim("Elige el segundo límite")
        num_lim_eleg=limites(lim1,lim2)    
        acertar(num_lim_eleg,lim1,lim2)    

def intervalo_predet():
    bounds=input("¿Quieres modificar los límites inferior y superior del juego?(S/N): ")
    if bounds.lower() == "s":                 
        intervalo_def() #Funcion 1 llamando a la funcion 2 y 3
    else:           
        num=rnd.randint(0,100)               
        pedir_numero("Adivina un número",0,100)
        acertar(num,0,100)

