"""
Este script sirve para comprobar si los datos que se encuentran en la lista
se almacenan en la variable dato y se comparan
"""

dato = input("Por favor ingrese un dato: ")
#print(type(dato))
print(dato)
    
lista = ["Hola","Mundo"]
#print(lista.count(0))

if lista.count(dato) > 0:
    print("Esta información existe:", dato)
else:
    print("Esta información no existe", dato)