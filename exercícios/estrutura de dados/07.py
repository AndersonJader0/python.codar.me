from collections import Counter

palavra = input('escreva uma palavra:')
lista_letra = []

for letra in palavra:
    lista_letra.append(letra)

contador = Counter(lista_letra)

print(contador)