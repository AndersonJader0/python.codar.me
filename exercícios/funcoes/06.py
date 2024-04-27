"""
DESAFIO. Uma função fatorial calcula o valor da multiplicação de um certo número
inteiro não-negativo por todos os números positivos menores que ele. A exceção é
o fatorial de zero que é igual a 1. Por exemplo:
"""

def calcula_fatorial(n):
    calculo = 0
    i = n - 1
    while i > 0:
        calculo += n * i
        i -= 1
    return calculo

result = calcula_fatorial(25)

print(result)


numeros = [1, 2, 3, 5, 6, 8, 10]

teste = [p for p in numeros if p % 2 == 0]

print(teste)