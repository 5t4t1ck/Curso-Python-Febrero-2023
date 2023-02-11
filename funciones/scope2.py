variable = 60 # variable global

def funcion():
    variable = 30 # variable local
    if variable < 100:
        print(variable)

print(variable)
funcion()
print(variable)