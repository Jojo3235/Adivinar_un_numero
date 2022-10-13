import sys
import random as rnd #Importamos las librerias necesarias
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
            else:
                print("Prueba un número más pequeño")

def limites(first_bound,second_bound):             #Definimos otra función que nos servira para establecer los límites correctamente
    if first_bound<second_bound:                   #Con este condicional hacemos que los límites estén primero el menor y despues el mayor, para que así no haya problemas a la hora de la ejecución del programa
        return rnd.randint(first_bound,second_bound)
    elif first_bound>second_bound:
        return rnd.randint(second_bound,first_bound)

def pedir_numero(cond,lim_1,lim_2):
    num=input("{} entre {} y {}: ".format(cond,lim_1,lim_2))
    while True:
        try:
            num=int(num)
        except:
            print("No se ha introducido un número válido", file=sys.stderr)
        else:
            if lim_1<lim_2:
                break
    return num

def pedir_numero_sin_lim(cond):
    num=input("{}: ".format(cond))
    try:
        num=int(num)
    except:
        print("El número introducido no es válido", file=sys.stderr)
    return num