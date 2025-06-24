# Repositório de Estudos - Estruturas de Dados em Python

Este repositório contém exemplos e implementações básicas de estruturas de dados e algoritmos em Python, com foco em aprendizado e prática.

## Conteúdo

- `busca_binaria.py`  
  Implementação da busca binária em lista ordenada.  
  Permite encontrar a posição de um elemento usando o algoritmo eficiente de divisão e conquista.

- `busca_sequencial.py`  
  Implementação da busca sequencial (linear).  
  Procura um valor em uma lista não ordenada, retornando sua posição caso exista.

- `imprime_lista.py`  
  Funções para imprimir elementos de listas e imprimir todas as combinações possíveis entre duas listas.

- `lista_encadeada.py`  
  Implementação de uma lista encadeada simples, com classes para o nó e a lista, incluindo inserção e remoção de elementos.

- `pilha.py`  
  Implementação da estrutura de dados **Pilha (Stack)** com operações básicas de inserção (push), remoção (pop) e visualização.  
  Inclui duas versões:  
  - Versão com funções que manipulam explicitamente o topo da pilha  
  - Versão simplificada utilizando lista nativa do Python com limite de tamanho

- `fila.py`  
  Implementação da estrutura de dados **Fila (Queue)** com operações básicas de enfileirar (enqueue), desenfileirar (dequeue) e visualização.  
  Usa funções que manipulam índices de início e fim da fila, além de tratamento para fila cheia e vazia.

- `recursao.py`  
  Exemplos de funções recursivas, incluindo cálculo de fatorial e sequência de Fibonacci.


- `arvore_binaria_busca.py`  
  Implementação de uma **Árvore Binária de Busca (BST)**.  
  Inclui inserção de nós e métodos de percurso: em ordem, pré-ordem, pós-ordem e por nível (largura).


- `arvore_avl_busca.py`  
  Implementação de uma **Árvore AVL (autobalanceada)**.  
  Mantém o balanceamento da árvore após inserções, realizando rotações simples e duplas quando necessário.  
  Inclui método de percurso em ordem.

- `dicionario.py`  
  Exemplo simples de uso de dicionário em Python para mapear frutas com seus preços.  
  Mostra como adicionar, acessar e listar chaves de um `dict`.

- `tabela_hash.py`  
  Implementação básica de uma **tabela hash** com hashing simples por soma dos códigos ASCII.  
  Inclui inserção, remoção e listagem dos dados.

- `tabela_hash_tratamento_colisoes.py`  
  Tabela hash com **tratamento de colisão por tentativa linear (linear probing)**.  
  Em caso de colisão, busca a próxima posição disponível.

- `tabela_hash_lista_encadeada.py`  
  Tabela hash com **encadeamento separado (separate chaining)** utilizando listas encadeadas simples.  
  Permite múltiplos elementos por posição da tabela.


- `grafo_lista_adjacencia.py`  
  Implementação de um **grafo não direcionado** utilizando **lista de adjacência**.  
  Define classes para vértices e para o grafo, permitindo a adição de vértices, arestas e a visualização das conexões entre os nós.


- `grafo_dfs_lista_adjacencia.py`  
  Implementação de um **grafo não direcionado** com **busca em profundidade (DFS)** usando lista de adjacência.  
  Cada vértice registra sua ordem de descoberta ao ser visitado.


- `grafo_dijkstra_lista_adjacencia.py`  
  Implementação de um **grafo ponderado** (com pesos nas arestas) usando **lista de adjacência**.  
  Utiliza o **algoritmo de Dijkstra** para encontrar o menor caminho a partir de um vértice origem até os demais.




## Como usar

Cada arquivo pode ser executado individualmente com o comando

```bash

python3 nome_arquivo.py

```

 para testar os algoritmos implementados.  


