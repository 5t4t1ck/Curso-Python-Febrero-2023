tupla = ("Esto", "es", "un", "un", "ejemplo", "de", "tupla")

print(tupla)
print(type(tupla))

print(tupla.count("un"))
print(tupla.index("de"))

print(tupla[2])

lista = list(tupla)
lista.append("Ejemplo2")

print(lista)
print(type(lista))

tupla2 = tuple(lista)
print(type(tupla2))