from random import randint


def maior_numero_aleatorio():
    numeros_aleatorios = []

    for i in range(10):
        numeros_aleatorios.append(randint(1,10))

    tupla = tuple(numeros_aleatorios)

    maior_numero = max(tupla)

    print(tupla, maior_numero)

maior_numero_aleatorio()