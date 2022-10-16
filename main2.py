"""
lvl 1 -> 0-100  7 atts
lvl 2 -> 0-1.000   12 atts
lvl 3 -> 0-1.000.000    24 atts
lvl 4 -> 0 1.000.000.000.000     40 atts
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

if dificultad(1,4)==1:
    lim1=0
    lim2=100
    if atts>=7:
        print("has perdido")
        break
elif dificultad(1,4)==2:
    lim1=0
    lim2=1000
    if atts>=12:
        print("has perdido")
        break
elif dificultad(1,4)==3:
    lim1=0
    lim2=1000000
    if atts>=24:
        print("has perdido")
        break
elif dificultad(1,4)==4:
    lim1=0
    lim2=1000000000000
    if atts>=40:
        print("has perdido")
        break
else:
    print("No existe esa dificultad")