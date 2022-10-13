import sys
import random as rnd #Importamos las librerias necesarias

MIN=0
MAX=100
min=MIN
max=MAX
SI=("s","si","y","yes","1")
VERDADERO=("v","verdadero","t","true","1")

def acertar(numero,lim1,lim2):            #Definimos la primera función que será la parte principal del funcionamiento interno del juego               
    tries=0                     #Igualamos los intentos a 0
    while True:                 
        elección=pedir_numero("Introduce un número",lim1,lim2)
        tries+=1                                    #Suma 1 al contador de intentos
        if elección==numero:                    #Si el número es correcto imprime que has acertado y el número de intentos y finaliza el bucle
            print("¡Has acertado el número!")
            if tries!=1:
                print("Número de intentos", tries)
                break
            else:
                print("Número de intentos: 1")
                break
        else:                                      #Si no mandamos que imprima si el número es más grande o más pequeño
            if elección < numero:
                print("Prueba un número más grande")
                while True:
                    if lim1<elección:
                        lim1=elección+1
                    else:
                        break
            else:
                print("Prueba un número más pequeño")
                while True:
                    if lim2>elección:
                        lim2=elección-1
                    else:
                        break

DIF_MIN=1
DIF_MAX=4

def dificultad(dif_1,dif_2):
    lvl=input("Elige un número entre 1 y 4: ")
    if int(dif_1)<int(lvl)<int(dif_2):
        try:
            lvl=int(lvl)
        except:
            print("No se ha introducido un número válido")
        return lvl
    else:
        print("No se ha introducido un número válido")



def limites(first_bound,second_bound):             #Definimos otra función que nos servira para establecer los límites correctamente
    if first_bound<second_bound:                   #Con este condicional hacemos que los límites estén primero el menor y despues el mayor, para que así no haya problemas a la hora de la ejecución del programa
        return rnd.randint(first_bound,second_bound)
    elif first_bound>second_bound:
        return rnd.randint(second_bound,first_bound)

def pedir_numero(cond,lim_1,lim_2):
    while True:
        try:
            num=input("{} entre {} y {}: ".format(cond,lim_1,lim_2))
            num=int(num)
        except:
            print("No se ha introducido un número válido", file=sys.stderr)
        else:
            if lim_1<lim_2:
                break
    return num

def pedir_numero_sin_lim(cond):
    while True:
        num=input("{}: ".format(cond))
        try:
            num=int(num)
        except:
            print("El número introducido no es válido", file=sys.stderr)
        else:
            return num

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
            

def intervalo_def():
    random_bounds_pregunta=input("¿Quieres que los límites sean aleatorios?(S/N): ")    
    if random_bounds_pregunta.lower() in SI:                #Funcion 2 llamando a la funcion 3
        intervalo_rand(50)
    else:               
        lim1=pedir_numero_sin_lim("Elige el primer límite")
        lim2=pedir_numero_sin_lim("Elige el segundo límite")
        num_lim_eleg=limites(lim1,lim2)    
        acertar(num_lim_eleg,lim1,lim2)    

def jugar_una_vez():
    bounds=input("¿Quieres modificar los límites inferior y superior del juego?(S/N): ")
    if bounds.lower() in SI:                 
        intervalo_def() #Funcion 1 llamando a la funcion 2 y 3
    else:           
        num=rnd.randint(0,100)             
        acertar(num,min,max)

def pedir_entrada_si_o_no(cond):
    try:
        return input(cond).lower() in SI
    except:
        return False

def jugar():
    while True:
        jugar_una_vez()
        if not pedir_entrada_si_o_no("¿Desea jugar una nueva partida?: "):
            print("Hasta la próxima")
            return

if __name__=='__main__':
    print("Se ha ejecutado el módulo")
    jugar()
else:
    print("Se ha importado el módulo")