#Ejercicio 16: Dada la siguiente tupla, crear una lista que sólo incluya los números menor que 5 utilizando un ciclo for:

tupla = (13, 1, 8, 3, 2, 5, 8)

tup = list(tupla)

for i in tup:
    if i <= 5:
        print(i, end=", ")