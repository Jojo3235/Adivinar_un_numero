import random as rnd
i=1
lista=list()
while i<100:
    i=i+1
    numero= rnd.randint(0, 100)
    print(numero)
    lista.append(numero)
else:
    pass
print(lista)