"""Crear una clase Gato que tenga 2 atributos, nombre y sonido. 
También agregar un método que permita saludar, en este método 
indicar que clase es a la que pertenece y cual es su sonido.

Crear una clase Perro con los mismos métodos y atributos del Gato, 
la particularidad es que este debe indicar en el método saludo, que es 
un perro y su sonido."""

class Gato:

    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido

    def __str__(self):
        return f"Soy la clase Gato, mi nombre es {self.nombre} y mi sonido es {self.sonido}"
    
class Perro(Gato):

    def __init__(self, nombre, sonido):
        super().__init__(nombre, sonido)

    def __str__(self):
        return f"Soy la clase Perro, mi nombre es {self.nombre} y mi sonido es {self.sonido}"
    
gato_1 = Gato("Silvestre", "Miau")
print(gato_1)
perro_1 = Perro("Rocky", "Guau")
print(perro_1)
