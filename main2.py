"""
lvl 1 -> 0-100  10 atts
lvl 2 -> 0-1.000   17 atts
lvl 3 -> 0-1.000.000    34 atts
lvl 4 -> 0 1.000.000.000.000     60 atts
"""

def dificultad(dif_1,dif_2):
    lvl=input("Elige un número entre 1 y 4: ")
    if int(dif_1)<=int(lvl)<=int(dif_2):
        try:
            lvl=int(lvl)
        except:
            print("No se ha introducido un número válido")
        return lvl
    else:
        print("No se ha introducido un número válido")

def atts_max(atts,max):
    while True:
        if atts>=max:
            print("Has perdido")
            break
        else:
            pass

atts=00
if dificultad(1,4)==1:
    lim1=0
    lim2=100
    atts_max(atts,7)
elif dificultad(1,4)==2:
    lim1=0
    lim2=1000
    atts_max(atts,12)
elif dificultad(1,4)==3:
    lim1=0
    lim2=1000000
    atts_max(atts,24)
elif dificultad(1,4)==4:
    lim1=0
    lim2=1000000000000
    atts_max(atts,40)
else:
    print("No existe esa dificultad")