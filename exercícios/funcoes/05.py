def verificar_lista(lista, item):
    i = 0
    while i < len(lista):
        if item == lista[i]:
            print('Esse elemento existe na lista:',item)
        i += 1

verificar_lista([1, 20, 5, 4], 5)