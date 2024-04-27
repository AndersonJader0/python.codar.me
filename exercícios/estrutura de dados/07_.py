

palavra = input('Digite uma palavra: ')
lista_letra = []
lista_letra_unica = []
counter = []

for letra in palavra:
    lista_letra.append(letra)

for letra in palavra:
    if letra not in lista_letra_unica:
        lista_letra_unica.append(letra)
        counter.append(lista_letra.count(letra))

# print(palavra, lista_letra, lista_letra_unica, counter)

i = 0
while i < len(lista_letra_unica):
    print(lista_letra_unica[i], ':',counter[i])
    i += 1