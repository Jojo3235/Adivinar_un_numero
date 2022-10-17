import sys
import random as rnd #Importamos las librerias necesarias
import numpy as np

SI=("s","si","y","yes","1")
VERDADERO=("v","verdadero","t","true","1")

#Tries

def tries(atts):
    atts+=1             #Con la función tries hacemos que los intentos vayan subiendo
    return atts

def atts_max(atts,max):     #Con la función atts_max hacemos que cuando llegue al número de intentos máximo se rompa el bucle y acabe la partida
    while True:         
        tries(atts)
        if atts>=max:
            print("Has perdido")
            break

#Numeros

def pedir_numero_sin_lim(cond):     #Esta función sirve para pedir un número pero sin dar un intervalo
    while True:
        num=input("{}: ".format(cond))
        try:
            num=int(num)
        except:
            print("El número introducido no es válido", file=sys.stderr)
        else:
            return num

def pedir_numero(cond,lim_1,lim_2):     #Esta función nos permite pedir un número en base a una introducción de la pregunta y 2 números que seran el intervalo especificado en el mensaje 
    while True:                                        
        try:        #Intentamos que sea un número entero
            num=input("{} entre {} y {}: ".format(cond,lim_1,lim_2))
            num=int(num)
        except:      #En caso de que no lo esa, mandamos un excepción y volvemos al bucle
            print("No se ha introducido un número válido", file=sys.stderr)
        else:       #Cuando el primer número sea menor que el segundo hacemos que salga del bucle, si no, vuelve a pedir los límites
            if lim_1<lim_2:
                break
    return num

def intentos(atts):         #Con la función intentos ponemos que nos imprima el numero de intentos
    if atts==1:
        print("Número de intentos: 1")
    else:
        print("Número de intentos:", atts)
        
#Numeros


def acertar(numero,lim1,lim2,max_att):     #Esta función es la más básica para que el juego funcione
    atts=0          #Seteamos los intentos a 0 y hacemos que sume uno para la primera entrada
    tries(atts)                        
    while True:    #Hasta que no se acierte el número o se alcancen los intentos máximos el bucle seguira pidiendo números
        atts=tries(atts) #Hacemos que nos diga los intentos que llevamos
        if atts<=max_att:       #Mientras los intentos no superen los intentos máximos se ejecutará el código para introducir el número
            elección=pedir_numero("Introduce un número",lim1,lim2)  #Pedimos un número que esté entre el primer límite y el segundo
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
                            lim1=elección   #Redefinimos los límites para que se vayan modificando a medida que se introducen los números
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
        else:           #Si se supera el número máximo de intentos, entonces se pierde la partido e imprime Game Over
            print("Game Over")
            break

def acertar_sin_ayuda(numero,lim1,lim2,max_att):  #Igual que la función acertar pero los límites no se modifican a medida que avanza el juego
    atts=0
    tries(atts)                     
    while True:    
        atts=tries(atts)             
        if atts<=max_att:
            elección=pedir_numero("Introduce un número",lim1,lim2)
            tries(atts)                           
            if elección==numero:                   
                print("¡Has acertado el número!")
                intentos(atts)
                break
            else:                                     
                if elección < numero:
                    print("Prueba un número más grande")
                    tries(atts)
                elif elección > numero:
                    print("Prueba un número más pequeño")
                    tries(atts)
        else:
            print("Game Over")
            break

#Numeros

def limites(first_bound,second_bound):             #Definimos otra función que establecerá los límites
    if first_bound<second_bound:                   #Con este condicional hacemos que los límites estén primero el menor y despues el mayor, para que así no haya problemas a la hora de la ejecución del programa
        return rnd.randint(first_bound,second_bound)
    elif first_bound>second_bound:
        return rnd.randint(second_bound,first_bound)



def dificultad(dif_1,dif_2):        #La función dificutad nos permite pedir un número entero entre 2 valores (incluidos) y nos devuelve el número
    lvl=pedir_numero("Elige un nivel de dificultad",dif_1,dif_2)    #Pedimos un número entre las difcultades que establezcamos
    if int(dif_1)<=int(lvl)<=int(dif_2):    #Una vez tenemos el número entre los valores esperados miramos que sea un entero, y si lo es, nos devuelve ese número
        try:
            lvl=int(lvl)
        except:
            print("No se ha introducido un número válido")  #En caso de que no lo sea, imprimimos que no se ha introducido un número válido
        return lvl
    else:
        print("No se ha introducido un número válido")

#Intervalos

def intervalo_rand(intervalo_min):      #Con esta función creamos el modo de juego de intervalos aleatorios
    while True:
        intervalo=pedir_numero_sin_lim("Introduce un número para determinar el máximo intervalo entre los límites, mayor a {}".format(intervalo_min)) #Pedimos un número que determinará el intervalo máximo posible
        atts=rnd.randint(7,20)              #Determinamos los intentos entre 7 y 20 de manera aleatoria
        print("Tienes {} intentos".format(atts))      #Imprimimos el número de intentos que ha tocado
        try:
            int(intervalo)>=intervalo_min          #Hacemos que el intervalo sea mayor que el mínimo especificado en los parámetros de la función
            lim1_rand=rnd.randint(0,200)           #Generamos un número aleatorio como cota mínima
            lim2_rand=lim1_rand+rnd.randint(30, intervalo)      #La cota máxima se genera mediante la suma al numero generado previamente y un número aleatorio entre 30 y el que ha introducido el jugador
            rand_bound_num=limites(lim1_rand,lim2_rand)         #Definimos el número a acertar entre el límite 1 y 2 definidos más arriba
            acertar(rand_bound_num,lim1_rand,lim2_rand,atts)    #Llamamos a la función acertar con los parámetros definidos previamente en esta función
            break
        except:
            print("No se ha introducido un número válido", file=sys.stderr)

def intervalo_rand_sin_ayuda(intervalo_min):    #Lo mismo que la función intervalo_rand, pero llamando a la funcion acertar sin ayuda, en vez de la función acertar
    while True:
        intervalo=pedir_numero_sin_lim("Introduce un número para determinar el máximo intervalo entre los límites, mayor a {}".format(intervalo_min))
        atts=rnd.randint(7,30)
        print("Tienes {} intentos".format(atts))
        try:
            int(intervalo)>=intervalo_min
            lim1_rand=rnd.randint(0,200)            
            lim2_rand=lim1_rand+rnd.randint(30, intervalo)
            rand_bound_num=limites(lim1_rand,lim2_rand)
            acertar_sin_ayuda(rand_bound_num,lim1_rand,lim2_rand,atts)
            break
        except:
            print("No se ha introducido un número válido", file=sys.stderr)

def escalado_intentos(lim1,lim2):       #En esta función cremos un escalado de intentos para las funciones de intervalos definidos
    return round(10*(np.log10((int(lim2)-(lim1)))))

def intervalo_def():
    random_bounds_pregunta=input("¿Quieres que los límites sean aleatorios?(S/N): ")    
    if random_bounds_pregunta.lower() in SI:               
        intervalo_rand(50)
    else:               
        lim1=pedir_numero_sin_lim("Elige el primer límite")
        lim2=pedir_numero_sin_lim("Elige el segundo límite")
        num_lim_eleg=limites(lim1,lim2)  
        print("Tienes {} intentos".format(escalado_intentos(lim1,lim2)))  
        acertar(num_lim_eleg,lim1,lim2,(escalado_intentos(lim1,lim2)))    

def intervalo_def_sin_ayuda():
    random_bounds_pregunta=input("¿Quieres que los límites sean aleatorios?(S/N): ")    
    if random_bounds_pregunta.lower() in SI:               
        intervalo_rand(50)
    else:               
        lim1=pedir_numero_sin_lim("Elige el primer límite")
        lim2=pedir_numero_sin_lim("Elige el segundo límite")
        num_lim_eleg=limites(lim1,lim2)    
        print("Tienes {} intentos".format(escalado_intentos(lim1,lim2)))  
        acertar(num_lim_eleg,lim1,lim2,(escalado_intentos(lim1,lim2)))   

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
            atts=8
        elif dif==2:
            lim1=0
            lim2=1000
            atts=15
        elif dif==3:
            lim1=0
            lim2=1000000
            atts=30
        elif dif==4:
            lim1=0
            lim2=1000000000000
            atts=50
        else:
            print("No existe esa dificultad")         
        num=rnd.randint(lim1,lim2)          
        acertar(num,lim1,lim2,atts)


def jugar_una_vez_sin_ayuda():
    bounds=input("¿Quieres modificar los límites inferior y superior del juego?(S/N): ")
    if bounds.lower() in SI:                 
        intervalo_def_sin_ayuda() #Funcion 1 llamando a la funcion 2 y 3
    else:
        dif=dificultad(1,4)  
        if dif==1:
            lim1=0
            lim2=100
            atts=8
        elif dif==2:
            lim1=0
            lim2=1000
            atts=15
        elif dif==3:
            lim1=0
            lim2=1000000
            atts=30
        elif dif==4:
            lim1=0
            lim2=1000000000000
            atts=50
        else:
            print("No existe esa dificultad")         
        num=rnd.randint(lim1,lim2)          
        acertar_sin_ayuda(num,lim1,lim2,atts)
        return dif

def jugar_de_nuevo(cond):
    try:
        return input(cond).lower() in SI
    except:
        return False

def jugar():
    while True:
        ayuda=input("¿Quiere restringir los límites a medida que introduzca números?(S/N): ")
        if ayuda.lower() in SI:
            jugar_una_vez()
        else:
            jugar_una_vez_sin_ayuda()
        if not jugar_de_nuevo("¿Desea jugar una nueva partida?: "):
            print("Hasta la próxima")
            return

if __name__=='__main__':
    print("Se ha ejecutado el módulo")
    jugar()
else:
    print("Se ha importado el módulo")