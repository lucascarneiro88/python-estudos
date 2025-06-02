def busca_binaria(inicio, fim, dados, buscado):
    """
    Busca binária em lista ordenada.
    Retorna a posição (0-based) ou -1 se não encontrar.
    """
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if buscado > dados[meio]:
            inicio = meio + 1
        elif buscado < dados[meio]:
            fim = meio - 1
        else:
            return meio
    return -1


if __name__ == "__main__":
    import random
    dados = random.sample(range(10), 10)
    dados.sort()
    print("Lista ordenada:", dados)
    buscado = int(input('Digite o valor que deseja buscar: '))
    pos = busca_binaria(0, len(dados) - 1, dados, buscado)
    if pos == -1:
        print('Valor não encontrado.')
    else:
        print(f'Valor encontrado na posição {pos}')
