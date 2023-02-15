class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return f"guau"
    
class Gato(Animal):
    def hablar(self):
        return f"miau"
    
class Vaca(Animal):
    def hablar(self):
        return f"muu"
    
animales = [Perro(), Gato(), Vaca()]

for animal in animales:
    print(animal.hablar())