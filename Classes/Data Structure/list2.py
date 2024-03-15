pessoa = ["Gabriel", 27, "123123"]

print("O nome é", pessoa[0])
print("A idade é", pessoa[1])


pessoas = [
    ["Anderson", 20],
    ["Teste", 30],
]

notas = [10, 9, 8, 7, 6, 5]

notas.sort()

i = 0
total = 0
qtd = len(notas)
while i < qtd:
    total = total + notas[i]
    i = i + 1

media = total / 5

print("O total é: ", total)
print("A média é: ", media)