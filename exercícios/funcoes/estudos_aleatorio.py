from random import randint



# lista = []
# for item in range(10):
#     lista.append(item**2)
# print(lista)

#É o mesmo for acima porém em comprehension
lista = [item**2 for item in range(10)]
print(lista)



#Compressão
tupla = tuple(randint(i + 1, 9) for i in range(5))
print('here:',tupla)



#Não comprimido

# Gerando um número aleatório entre 5 e 5 (sempre será 5)
num_iteracoes = 5

# Inicializando uma lista vazia para armazenar os elementos
lista_numeros = []

# Loop for para gerar cada elemento da tupla
for i in range(num_iteracoes):
    # Gerando um número aleatório entre i + 1 e 9
    numero_aleatorio = randint(1, 9)
    # Adicionando o número à lista
    lista_numeros.append(numero_aleatorio)

# Convertendo a lista para uma tupla
tupla = tuple(lista_numeros)

# Imprimindo a tupla
print(tupla)