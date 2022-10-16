import sys
def pedir_numero(cond):
    num=input("{}".format(cond))
    while True:
        try:
            num=int(num)
        except:
            print("El número introducido no es válido", file=sys.stderr)
        else:
            return num

def pedir_numero_lim(cond,min,max):
    num=input("{} entre {} y {}: ".format(cond,min,max))
    while True:
        try:
            num=int(num)
        except:
            print("El número introducido no es válido", file=sys.stderr)
            break
        else:
            if min<max:
                break
    return num

while True:
    min=input("Introduzca el valor mínimo")
    max=input("Introduzca el valor máximo")
    if min<max:
        break
from definiciones import intentos,tries

def comparación(elección,numero,atts):
    while True:
        if elección==numero:                    #Si el número es correcto imprime que has acertado y el número de intentos y finaliza el bucle
            print("¡Has acertado el número!")
            intentos(atts)
            break
        else:                                      #Si no mandamos que imprima si el número es más grande o más pequeño
            if elección < numero:
                print("Prueba un número más grande")
                while True:
                    if lim1<elección:
                        lim1=elección+1
                        tries(atts)
                    else:
                        break
            else:
                print("Prueba un número más pequeño")
                while True:
                    if lim2>elección:
                        lim2=elección-1
                        tries(atts)
                    else:
                        break

