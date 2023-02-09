conjunto = {"Diego", "Saavedra", True, 3.1416, 6, "Diego"}
print(type(conjunto))

print(conjunto)


vocales = {"e", "i", "a", "u", "o"}
print(vocales)
print(type(vocales))

letras = {"b", "c", "d", "o"}

diferencia = vocales.difference(letras)
diferencia_v2 = vocales - letras
print(diferencia)
print(diferencia_v2)

numbers_1 = {1, 2, 3, 4, 5}
numbers_2 = {4, 5, 6, 7, 8}

result_1 = numbers_1.difference(numbers_2)
print(result_1)

result_2 = numbers_1.intersection(numbers_2)
print(result_2)

result_3 = numbers_1 & numbers_2
print(result_3)

result_4 = numbers_1.union(numbers_2)
print(result_4)

result_5 = numbers_1 | numbers_2
print(result_5)