import random as rnd

numero=rnd.randint(0,100)
print(numero)


def elegir_un_número(num):
    while True:
        if num == numero:
            return "No es ese número"
        else:
            return "Has acertado"
print(elegir_un_número(int(input("Introduce un número: "))))