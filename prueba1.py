import random as rnd
from pruebas import acertar,limites
bounds=input("¿Quieres modificar los límites inferior y superiro del juego?(S/N): ")
if bounds.lower() == "s":
    random_bounds=input("¿Quieres que los límites sean aleatorios?(S/N): ")
    if random_bounds.lower() == "s":
        lim1_rand=rnd.randint(0,200)
        lim2_rand=lim1_rand+rnd.randint(30, 300)
        rand_bound_num=limites(lim1_rand,lim2_rand)
        print("Adivina el número entre {} y {}".format(lim1_rand,lim2_rand))
        acertar(rand_bound_num)
    else:
        lim1=int(input("Elige el primer límite: "))
        lim2=int(input("Elige el segundo límite: "))
        num_lim_eleg=limites(lim1,lim2)
        print("Adivina el número entre {} y {}".format(lim1,lim2))
        acertar(num_lim_eleg)
else:
    num=rnd.randint(0,100)
    print("Adivina el número entre 0 y 100")
    acertar(num)