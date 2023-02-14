class Delfin:

    def __init__(self, name, age, tipe):
        self.name = name
        self.age = age
        self.tipe = tipe

    def __str__(self):
        return f"{self.name} tiene aproximadamente {self.age} años, y es de tipo {self.tipe}"
    
    def nadar(self):
        print(f"{self.name} puede nadar")
    

fliper = Delfin("Fliper", "7", "Marino")
print(fliper)

fliper.nadar()