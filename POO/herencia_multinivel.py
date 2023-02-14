class Profesion:

    def __init__(self, nombre):
        self.nombre = nombre

    def yoSoyAbuelo(self):
        print("Yo soy la clase Abuelo")

class Profesiones_Salud(Profesion):

    def __init__(self, area):
        pass

    def soyArea(self):
        print("Soy la clase Padre")

class Profesion_Especialidad(Profesiones_Salud):

    def __init__(self, nombre, area, especialidad):
        self.nombre = nombre
        self.area = area
        self.especialidad = especialidad

    def soyEspecialidad(self):
        print("Soy la clase nieta")

ortodoncista = Profesion_Especialidad("Juan", "Salud", "Ortodoncia")
print(ortodoncista.nombre)
ortodoncista.nombre = "Pedro"
print(ortodoncista.nombre)

ortodoncista.yoSoyAbuelo()
ortodoncista.soyArea()
ortodoncista.soyEspecialidad()