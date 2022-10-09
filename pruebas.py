import random as rnd
from timeit import repeat
def acertar(numero):
    print(numero)
    tries=0
    while True:
        elección=int(input("Introduce un numero: "))
        tries+=1
        if elección==numero:
            print("¡Has acertado el número!")
            if tries!=1:
                print("Número de intentos", tries)
                break
            else:
                print("Número de intentos: 1")
                break
        else:
            if elección < numero:
                print("Prueba un número más grande")
            else:
                print("Prueba un número más pequeño")

def limites(first_bound,second_bound):
    if first_bound<second_bound:
        return rnd.randint(first_bound,second_bound)
    elif first_bound>second_bound:
        return rnd.randint(second_bound,first_bound)