def executar_busca_binaria(lista, valor):
    minimo = 0 
    maximo = len(lista) - 1

    while minimo <= maximo:
        meio = (minimo + maximo) // 2
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return True

    return False

lista = [2, 4, 6, 7, 8, 11, 13, 15, 17, 22]
print(executar_busca_binaria(lista, valor = 13))

