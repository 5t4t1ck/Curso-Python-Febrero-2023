archivo = open("Archivos/nombres1.txt", "a")

archivo.write("\nagregamos un ejemplo de línea")

archivo.close()

archivo = open("Archivos/nombres1.txt", "a")

archivo = open("Archivos/nombres1.txt", "r")
print(archivo.readline())
print(archivo.readline())

archivo.close()
