def imprime_lista(dados):
    """Imprime todos os elementos da lista."""
    for i in dados:
        print(i)


def imprime_combinacoes(dadosA, dadosB):
    """Imprime todas combinações de elementos entre duas listas."""
    for i in dadosA:
        for j in dadosB:
            print(i, j)


if __name__ == "__main__":
    imprime_lista([1, 2, 3])
    imprime_combinacoes([1, 2], [3, 4])

