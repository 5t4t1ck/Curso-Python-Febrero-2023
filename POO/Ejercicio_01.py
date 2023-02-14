"""
Crear una clase Persona que tenga los
siguientes atributos:

- Nombre
- Apellido
- Cedula
- Edad
- Correo

Y Crear un método para que pueda presentarse 
con los atritutos definidos en la clase 
constructora

Crear 2 instancias de esta clase.
"""

class Persona:

    def __init__(self, Nombre, Apellido, Cedula, Edad, Correo):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Cedula = Cedula
        self.Edad = Edad
        self.Correo = Correo

    def saludar(self):
        return f" Hola mi nombre es {self.Nombre} {self.Apellido} mi número de cédula es {self.Cedula}, mi edad es {self.Edad} y mi correo electrónico es {self.Correo}"
    

Pedro = Persona("Pedro", "Jaramillo", 1154685245, 28, "pedro.jaramillo@gmail.com")
Juan = Persona("Juan", "Gonzaga", 1104578963, 38, "juan.gonzaga@gmail.com")

print(Pedro.saludar())
print(Juan.saludar())