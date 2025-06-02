def busca_sequencial(dados, buscado):
    """
    Busca sequencial: procura o valor 'buscado' em 'dados'.
    Retorna a posição (1-based) ou -1 se não encontrar.
    """
    achou = 0
    i = 0
    while i < len(dados) and achou == 0:
        if dados[i] == buscado:
            achou = 1
        else:
            i += 1
    if achou == 0:
        return -1
    else:
        return i + 1  # posição 1-based


if __name__ == "__main__":
    import random
    dados = random.sample(range(10), 10)
    print("Lista:", dados)
    buscado = int(input('Digite o valor que deseja buscar: '))
    pos = busca_sequencial(dados, buscado)
    if pos == -1:
        print('Valor não encontrado.')
    else:
        print(f'Valor encontrado na posição {pos}')
