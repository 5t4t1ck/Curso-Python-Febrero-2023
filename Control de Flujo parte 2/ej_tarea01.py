"""
Multiplicar 2 números sin usar el símbolo de la multiplicación.
"""

num1 = int(input("Por favor ingrese el primer valor: "))
num2 = int(input("Por favor ingrese el segundo valor: "))

#result = num1 * num2
result = None
"""while num1 <= num2:
    result = num1 + num1
    print(result)"""
i = 0
for i in range(0, num2):
    i +=1
    num1 = i
    print("contador ->",i)
    print("num2 ->",num2)