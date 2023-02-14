class Perro:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} de {self.age} años"
    
perro_1 = Perro("Wolf", 7)
print(perro_1)

perro_2 = Perro("Rocky", 3)
print(perro_2)