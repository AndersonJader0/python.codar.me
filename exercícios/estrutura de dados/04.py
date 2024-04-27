alunos = [
    ("Alice", 8),
    ("Bob", 7),
    ("Carlos", 9)
]

# print(alunos[0][1])
qntd = len(alunos)

soma = 0
for i, x in alunos:
    soma += x
    
print(soma / qntd)