def read_csv_file(caminho_arquivo):
  with open(caminho_arquivo, mode='r') as ponteiro:
    dados = ponteiro.read()
  
  return dados

