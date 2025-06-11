# -----------------------
# Classe que representa cada elemento (nó) da lista
# -----------------------

class ElementoDaListaSimples:
    # Inicializa o nó com um dado e o ponteiro "próximo" como None
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

    # Representação do objeto como string, útil para print e debug
    def __repr__(self):
        return str(self.dado)


# -----------------------
# Classe que representa Lista encadeada simples
# -----------------------

class ListaEncadeadaSimples:
    # Inicializa a lista. Pode receber uma lista de dados já prontos.
    def __init__(self, nodos=None):
        self.head = None  # Começa a lista
        if nodos is not None:
            nodo = ElementoDaListaSimples(dado=nodos.pop(0))
            self.head = nodo
            for elem in nodos:
                nodo.proximo = ElementoDaListaSimples(dado=elem)
                nodo = nodo.proximo

    # Representação visual da lista
    def __repr__(self):
        nodo = self.head
        nodos = []
        while nodo is not None:
            nodos.append(str(nodo.dado))
            nodo = nodo.proximo
        nodos.append("None")  # final da lista
        return " -> ".join(nodos)

    # Permite percorrer a lista com for-in (iterator)
    def __iter__(self):
        nodo = self.head
        while nodo is not None:
            yield nodo
            nodo = nodo.proximo

    # -------------------------
    # Insere um novo nó no início da lista
    # -------------------------
    def inserirNoInicio(self, nodo):
        nodo.proximo = self.head
        self.head = nodo

    # -------------------------
    # Insere um novo nó no final da lista
    # -------------------------
    def inserirNoFinal(self, nodo):
        if self.head is None:
            self.head = nodo
            return
        nodo_atual = self.head
        while nodo_atual.proximo is not None:
            nodo_atual = nodo_atual.proximo
        nodo_atual.proximo = nodo

    # -------------------------
    # Deleta um nó com o dado informado
    # -------------------------
    def deletar(self, dado):
        if self.head is None:
            raise Exception("Lista vazia")

        if self.head.dado == dado:
            self.head = self.head.proximo
            return

        nodo_anterior = self.head
        for nodo in self:
            if nodo.dado == dado:
                nodo_anterior.proximo = nodo.proximo
                return
            nodo_anterior = nodo

        raise Exception(f"Nó com dado {dado} não encontrado na lista")


# -------------------------
# Menu de interação com o usuário
# -------------------------

def menu():
    lista = ListaEncadeadaSimples()

    while True:
        print("\n--- MENU ---")
        print("1 - Inserir no início")
        print("2 - Inserir no final")
        print("3 - Deletar um elemento")
        print("4 - Mostrar lista")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = input("Digite o valor a ser inserido no início: ")
            lista.inserirNoInicio(ElementoDaListaSimples(valor))

        elif opcao == '2':
            valor = input("Digite o valor a ser inserido no final: ")
            lista.inserirNoFinal(ElementoDaListaSimples(valor))

        elif opcao == '3':
            valor = input("Digite o valor a ser deletado: ")
            try:
                lista.deletar(valor)
                print(f"Valor '{valor}' removido com sucesso.")
            except Exception as e:
                print(e)

        elif opcao == '4':
            print("\nLista atual:")
            for nodo in lista:
                print(nodo, end=' -> ')
            print('None')

        elif opcao == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")



# -------------------------
# Execução principal
# -------------------------
if __name__ == "__main__":
    menu()
# -------------------------
# Observação sobre self:
# -------------------------
# - `self` é a referência ao próprio objeto da classe.
# - É obrigatório como primeiro parâmetro de métodos dentro da classe.
# - Permite acessar e modificar atributos e métodos do objeto atual.

# -------------------------
# Observação sobre raise:
# -------------------------
# - `raise` é usado para **lançar uma exceção** (erro) de forma intencional.
# - Serve para sinalizar que algo deu errado e interromper o fluxo normal do programa.
# - Pode ser usado com tipos de exceções existentes (como Exception, ValueError, etc.)
# - Exemplo: raise Exception("Mensagem de erro")

# -------------------------
# Observação sobre yield:
# -------------------------
# - `yield` transforma uma função comum em um **gerador**.
# - Permite retornar valores um de cada vez, pausando a execução da função entre cada chamada.
# - É útil para **percorrer grandes volumes de dados sem carregar tudo na memória** de uma vez.
# - Em vez de retornar todos os valores com `return`, usa `yield` para produzir um por um.
# - Exemplo: 
#   def contador():
#       for i in range(5):
#           yield i
#   for num in contador():
#       print(num)
