nombre = "Diego"

def saludar(name=nombre):
    #global nombre
    return f"Hola, {name}"

print(saludar())