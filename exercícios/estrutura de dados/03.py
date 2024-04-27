

lista = [1, 10, 20, 35, 22, 12]
soma = 0
counter = 0
tmn = len(lista)

for i in lista:
    soma += i
    if tmn - 1 == counter:
        print(soma // tmn)
    counter += 1

