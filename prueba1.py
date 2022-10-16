#sys.path
import random as rnd
from definiciones import acertar,limites
import sqlite3 as sql
import pandas as pd

"""3. Registrar las mejores puntuaciones

Al final de una partida ganada,
puede también pedir al jugador su 
nombre y guardarlo en la tabla de 
mejores puntuaciones. En primer lugar, 
esta tabla se creará al inicio del programa
y los datos se perderán una vez se cierre.
Cuando tenga algo más de práctica con Python, 
podrá utilizar el módulo pickle para hacer que
estos datos sean persistentes, utilizar sqlite o
incluso sqlalchemy para guardarlos en una base 
de datos embebida.  (Data set)"""
"""
[(nombre, dificultad, atts), (nombre, dificultad, atts),...]
"""
mydataset = {
    "username":["jojo", "elephin", "3235"],
    "modo de juego":["predet 1","predet 2", "predet 3"],
    "atts":[5,32,24]
}

myvar= pd.DataFrame(mydataset)

a=[1,5,3]

myvar= pd.Series(a, index = ["x","y","z"])

print(myvar)
print(myvar["y"])