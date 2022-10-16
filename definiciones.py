import sys
import random as rnd #Importamos las librerias necesarias

MIN=0
MAX=100
min=MIN
max=MAX
SI=("s","si","y","yes","1")
VERDADERO=("v","verdadero","t","true","1")

#Tries

def tries(atts):
    atts+=1
    return atts

#Numeros
def intentos(atts):
    if atts==1:
        print("Número de intentos: 1")
    else:
        print("Número de intentos:", atts)

def acertar(numero,lim1,lim2):
    atts=0
    tries(atts)            #Definimos la primera función que será la parte principal del funcionamiento interno del juego               
    while True:    
        atts=tries(atts)             
        elección=pedir_numero("Introduce un número",lim1,lim2)
        tries(atts)                           #Suma 1 al contador de intentos
        if elección==numero:                    #Si el número es correcto imprime que has acertado y el número de intentos y finaliza el bucle
            print("¡Has acertado el número!")
            intentos(atts)
            break
        else:                                      #Si no mandamos que imprima si el número es más grande o más pequeño
            if elección < numero:
                print("Prueba un número más grande")
                while True:
                    if lim1<elección:
                        lim1=elección
                        tries(atts)
                    else:
                        break
            elif elección > numero:
                print("Prueba un número más pequeño")
                while True:
                    if lim2>elección:
                        lim2=elección
                        tries(atts)
                    else:
                        break


#Numeros

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

def dificultad(dif_1,dif_2):
    lvl=pedir_numero("Elige un número",dif_1,dif_2)
    if int(dif_1)<=int(lvl)<=int(dif_2):
        try:
            lvl=int(lvl)
        except:
            print("No se ha introducido un número válido")
        return lvl
    else:
        print("No se ha introducido un número válido")

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
            break
        except:
            print("No se ha introducido un número válido", file=sys.stderr)
            
def dificultades():
    return 
def intervalo_def():
    random_bounds_pregunta=input("¿Quieres que los límites sean aleatorios?(S/N): ")    
    if random_bounds_pregunta.lower() in SI:                #Funcion 2 llamando a la funcion 3
        intervalo_rand(50)
    else:               
        lim1=pedir_numero_sin_lim("Elige el primer límite")
        lim2=pedir_numero_sin_lim("Elige el segundo límite")
        num_lim_eleg=limites(lim1,lim2)    
        acertar(num_lim_eleg,lim1,lim2)    

#Jugar

def jugar_una_vez():
    bounds=input("¿Quieres modificar los límites inferior y superior del juego?(S/N): ")
    if bounds.lower() in SI:                 
        intervalo_def() #Funcion 1 llamando a la funcion 2 y 3
    else:
        dif=dificultad(1,4)  
        if dif==1:
            lim1=0
            lim2=100
        elif dif==2:
            lim1=0
            lim2=1000
        elif dif==3:
            lim1=0
            lim2=1000000
        elif dif==4:
            lim1=0
            lim2=1000000000000
        else:
            print("No existe esa dificultad")         
        num=rnd.randint(lim1,lim2)   
        print(num)          
        acertar(num,lim1,lim2)

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