import random as rnd
i=0
numero= rnd.randint(0, 100)
print(numero)
while i<1:
    elección=int(input("Introduce un numero: "))
    if elección==numero:
        i+=1
        print("¡Has acertado el número!")
else:
    pass
