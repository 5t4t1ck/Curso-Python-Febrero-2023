class Padre:

    def __init__(self, nombre, profesion):
        self.nombre = nombre
        self.profesion = profesion

    def __str__(self):
        return f"{self.nombre} tiene la profesion de {self.profesion}, soy la clase padre"
    
class Hijo(Padre):

    def __init__(self, nombre, profesion):
        super().__init__(nombre, profesion)

    def profesion_hijo(self):
        return f"Soy la clase hijo"


Juan = Padre("Juan", "Arquitecto")
print(Juan)

Pedro = Hijo("Pedro", "Programador")
print(Pedro.profesion_hijo())
print(Pedro.profesion)