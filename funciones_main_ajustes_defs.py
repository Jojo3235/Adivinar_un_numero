import random as rnd
from definiciones import acertar,limites,pedir_numero_sin_lim
#3 funciones aquí    
def intervalo_rand(intervalo):
    if int(intervalo)>=50:          #Función 3
        lim1_rand=rnd.randint(0,200)            
        lim2_rand=lim1_rand+rnd.randint(30, intervalo)
        rand_bound_num=limites(lim1_rand,lim2_rand)
        acertar(rand_bound_num,lim1_rand,lim2_rand)
    else:
        print("El número introducido es menor a 50")

bounds=input("¿Quieres modificar los límites inferior y superiro del juego?(S/N): ") 

def no_se(random_bounds):
    if random_bounds.lower() == "s":                #Funcion 2 llamando a la funcion 3
        intervalo=pedir_numero_sin_lim("¿Cuál quieres que sea el intervalo máximo entre los límites(>=50)?: ")
    else:               
        lim1=pedir_numero_sin_lim("Elige el primer límite")
        lim2=pedir_numero_sin_lim("Elige el segundo límite")
        num_lim_eleg=limites(lim1,lim2)    
        acertar(num_lim_eleg,lim1,lim2)    
    return intervalo

def idk(random_bounds):
    if bounds.lower() == "s":                 
        random_bounds=input("¿Quieres que los límites sean aleatorios?(S/N): ") #Funcion 1 llamando a la funcion 2 y 3
    