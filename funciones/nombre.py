Nombre = input("Por favor ingrese su nombre: ")
Apellido = input("Por favor ingrese su apellido: ")

def saludar(Nombre=Nombre, Apellido=Apellido):
    return f"Hola {Nombre} {Apellido}"

saludo = saludar()
saludo1 = saludar("Juan", "Martinez")

print(saludo)
print(saludo1)