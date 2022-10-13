"""
lvl 1 -> 0-100
lvl 2 -> 0-1.000
lvl 3 -> 0-1.000.000
lvl 4 -> 0 1.000.000.000.000
"""
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

dificultad(DIF_MIN,DIF_MAX)