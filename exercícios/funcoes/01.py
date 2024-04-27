"""
número é primo: Somente divisivel por ele mesmo e por 1.
número não primo: divisivel por mais números.
"""

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_divisivel = []
numero = int(input('Digite um número: '))
primo = False

def e_primo(numero):
    for n in lista_numeros:
        if numero % n == 0:
            lista_divisivel.append(n)
        if numero not in lista_numeros:
            if numero % numero == 0:
                if numero % n == 0:
                    lista_divisivel.append(n)

    if len(lista_divisivel) == 2:
        return True
    else:
        return False

primo = e_primo(numero)

print('O número é primo: ', primo)