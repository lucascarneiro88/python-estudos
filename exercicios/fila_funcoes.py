def queue(fila, fim, tam, dado):
  if len(fila) == tam:
    print('Fila cheia! Impossível inserir.')
  else:
    fila.insert(fim, dado)
    fim += 1
  return fila, fim

def dequeue(fila, inicio):
  if len(fila) == 0 or inicio >= len(fila):
    print('Fila vazia! Impossível remover.')
  else:
    print(f'Removido: {fila[inicio]}')
    fila[inicio] = None
    inicio += 1
  return fila, inicio

# Programa principal
inicio = 0
fim = 0
fila = []
tam = 5

while True:
  print('1 - Inserir na fila')
  print('2 - Remover da fila')
  print('3 - Listar a fila')
  print('4 - Sair')

  op = int(input("Escolha uma opção:"))
  if op == 1:
    dado = int(input('Qual número deseja inserir?'))
    fila, fim = queue(fila, fim, tam, dado)
  elif op == 2:
    fila, inicio = dequeue(fila, inicio)
  elif op == 3:
    print('Fila atual:')
    for item in fila:
      print(item, end=" ")
    print()
  elif op == 4:
    print('Encerrando...')
    break
  else:
    print("Selecione outra opção!\n")
