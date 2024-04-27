def maior_idade(lista):
    for n in lista:
        if n >= 18:
            print('É de maior')
        elif n < 18:
            print('É de menor')

maior_idade((18, 19, 20, 9))