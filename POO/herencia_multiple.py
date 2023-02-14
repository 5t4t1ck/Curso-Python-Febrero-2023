class Padre:

    def __init__(self, nombre, habilidad_padre):
        self.nombre = nombre
        self.habilidad_padre = habilidad_padre

    def __str__(self):
        return f"Soy la clase Padre"
    
    def cantar(self):
        return f"Soy la clase Padre y puedo Cantar"
    
class Madre:

    def __init__(self, nombre, habilidad_madre):
        self.nombre = nombre
        self.habilidad_madre = habilidad_madre

    def __str__(self):
        return f"Soy la clase Madre"
    
    def hornear(self):
        return f"Soy la clase madre y puedo hornear"
    
class Hijo(Padre, Madre):

    def __init__(self, nombre, habilidad_padre):
        super().__init__(nombre, habilidad_padre)

Juan = Hijo("Juan", "Cantar")

habilidad_padre = Juan.cantar()
print(habilidad_padre)

habilidad_madre = Juan.hornear()
print(habilidad_madre)