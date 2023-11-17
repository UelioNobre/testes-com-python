import csv

def read_csv_file(caminho_arquivo):
  with open(caminho_arquivo, encoding="utf8") as ponteiro:
    dados = csv.reader(ponteiro, delimiter=",", quotechar='"')
  
    header, *conteudo = dados
  
  return (header, conteudo)


