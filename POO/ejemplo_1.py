class Monster:

    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria

    def myFunc(self):
        print("Hey, yo soy " + self.nombre)

#Instancia de clases o creación del objeto

mounstrito = Monster("Sullivan", "Asustador")
mounstrito.myFunc()
print(mounstrito.nombre)
print(mounstrito.categoria)