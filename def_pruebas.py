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
