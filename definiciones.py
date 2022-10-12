import sys
import random as rnd #Importamos las librerias necesarias
def acertar(numero):            #Definimos la primera función que será la parte principal del funcionamiento interno del juego
    print(numero)               
    tries=0                     #Igualamos los intentos a 0
    while True:                 
        elección=input("Introduce un numero: ")   #Pedimos un número
        try:                                    
            elección = int(elección)                #Si el número es un int no da error
        except:                                     #Si no lo es devuelve el error controlado
            print("No se ha introducido ningún número, pruebe de nuevo",
                file=sys.stderr)
            sys.exit()
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