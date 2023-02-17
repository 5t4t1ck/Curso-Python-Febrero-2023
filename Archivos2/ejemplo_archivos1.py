import os

if os.path.exists("Archivos2/nombres.txt"):
    os.remove("Archivos2/nombres.txt")
    print("El archivo a sido eliminado")
else:
    print("El archivo no existe !!!")