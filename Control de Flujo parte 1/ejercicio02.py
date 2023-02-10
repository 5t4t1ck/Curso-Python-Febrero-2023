primerNumero = input("Ingrese el primer número: ")

try:
    primerNumero = int(primerNumero)
except:
    primerNumero = "Cadena"

if primerNumero == "Cadena":
    print("El dato que ingresó no es un número, por favor ingrese un dato válido")
    exit()

segundoNumero = int(input("Ingrese el segundo número: "))

try:
    segundoNumero = int(segundoNumero)
except:
    segundoNumero = "Cadena"

if segundoNumero == "Cadena":
    print("El dato que ingresó no es un número, por favor ingrese un dato válido")
    exit()

simbolo = input("Ingrese la operacion: ")

if simbolo == "+":
    print("Suma: ", primerNumero + segundoNumero)
elif simbolo == "-":
    print("Resta: ", primerNumero - segundoNumero)
elif simbolo == "*":
    print("Multiplicacion: ", primerNumero * segundoNumero)
elif simbolo == "/":
    print("Division: ", primerNumero / segundoNumero)
else:
    print("El simbolo ingresado no es valido")
