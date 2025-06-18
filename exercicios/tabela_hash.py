def hashFuncSigla(k, n):
    soma = sum([ord(c.upper()) for c in k])  # converte letras para ASCII e soma
    return soma % n

# Programa principal
n = 10
tabelaHash = [None] * n

while True:
  print('1 - Inserir na tabela hash')
  print('2 - Remover na tabela hash')
  print('3 - Listar a tabela hash')
  print('4 - Sair')

  op = int(input("Escolha uma opção:"))
  if op == 1:
    chave = input('Digite a sigla de um estado: ')
    pos = hashFuncSigla(chave, n)
    if tabelaHash[pos] == None:
        tabelaHash[pos] = chave
    else:
        print('Já existe um dado neste lugar!')
  elif op == 2:
    chave = int(input('Digite o que deseja remover: '))
    pos = hashFuncSigla(chave, n)
    if tabelaHash[pos] == chave:
        tabelaHash[pos] = None
    else:
        print('Valor não localizado para a remoção!')
  elif op == 3:
      print('\ntabelaHash')
      for i, v in enumerate(tabelaHash):
         print(f'{i}: {v.upper()}' if v else f'{i}: {v}')
  elif op == 4:
    print('Encerrando...')
    break
  else:
    print("Selecione outra opção!\n")




#Summary

# Listagem da Tabela Hash (op == 3)
#Exibe o conteúdo da tabela hash, mostrando o índice de cada posição e a sigla armazenada (em maiúsculo, se existir).
#Utiliza enumerate para percorrer a tabela e upper() para padronizar a exibição das siglas.