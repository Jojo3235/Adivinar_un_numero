"""
lvl 1 -> 0-100  10 atts
lvl 2 -> 0-1.000   17 atts
lvl 3 -> 0-1.000.000    34 atts
lvl 4 -> 0 1.000.000.000.000     60 atts

Para las mejores puntuaciones guardar solo la de los niveles
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

