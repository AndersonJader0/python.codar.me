
numero = 0
lista = []

while numero % 2 == 0:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    if numero % 2 == 1:
        qntd = len(lista)
        lista.pop(qntd-1)
        # print('número impar removido')

print(lista)