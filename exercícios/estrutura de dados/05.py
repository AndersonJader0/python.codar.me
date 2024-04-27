alunos = [
    {
        "nome": "Alice",
        "nota": 8,
    },
    {
        "nome": "Bob",
        "nota": 7,
    },
    {
        "nome": "Carlos",
        "nota": 9,
    }
]

inteiro = 0
conversor = []

for nota in alunos:
    conversor.append(alunos[inteiro].values())
    inteiro += 1

soma = 0
for x, y in conversor:
    soma += y

print(soma / len(conversor))