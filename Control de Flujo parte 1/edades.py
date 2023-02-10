"""
Comprobar si una personas es mayor de edad, utilizar los siguientes rangos
a = "Si es menor de Edad"
b = "Si es mayor de Edad"
c = "Si es Adulto Mayor"
"""

edad = int(input("Por favor ingresa tu edad en números: "))
#print(type(edad))
#print(edad)

if edad < 18 and edad > 0:
    print("Usted es menor de edad", edad)

elif edad >= 18 and edad < 60:
    print("Usted es mayor de edad", edad)

elif edad >= 60 and edad <= 120:
    print("Usted es un Adulto Mayor", edad)

else:
    print("El rango de edad no está contemplado")
"""
And: True Ambas condiciones son verdaderas, el resultado es verdadero
Or: True si en al menos una condición es verdadera, el resultado es verdadero
Not: Niega la condición
"""