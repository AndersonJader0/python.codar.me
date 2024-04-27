alunos = [
    { #Dicionário dentro de lista
        "nome": "Anderson",
        "nota": 10,
    },
    {
        "nome": "Pep",
        "nota": 9
    }
]


alunos_nota_10 = []

for aluno in alunos:
    if aluno["nota"] == 10:
        alunos_nota_10.append(aluno)

print(alunos_nota_10)

alunos_nota_10 = [aluno for aluno in alunos if aluno["nota"] == 10]

notas = [1, 10, 9, 3, 5, 8, 7, 10]

teste = [i for i in notas if i == 10]

print(teste)