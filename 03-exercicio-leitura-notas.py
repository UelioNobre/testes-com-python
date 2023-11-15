caminho_arquivo_inexistente = '03-arquivo-inexistente.txt'
caminho_arquivo_existente = '03-exercicio-leitura-notas.txt'
caminho_arquivo_pessoas_reprovadas = '03-exercicio-pessoas_reprovadas.txt'

def carregar_arquivos_notas(caminho_arquivo):
  pessoas = []
  
  try:
    with open(caminho_arquivo) as conteudo:
      pessoas = conteudo.readlines()
  except FileNotFoundError:
    print(f":: ERROR :: Não foi possível encontrar o arquivo: {caminho_arquivo}")
    return None
  
  return pessoas

def filtro_pessoas_reprovadas(pessoas):
  if pessoas == None:
    raise ValueError("Lista de pessoas esta vazia")

  pessoas_reprovadas = []
  for pessoa in pessoas:
    nome, nota = pessoa.replace("\n", "").split(" ")
    if int(nota) < 6:
      pessoas_reprovadas.append(nome + "\n")
  
  return pessoas_reprovadas


def processar_pessoas_reprovadas(caminho_arquivo):
  try:
    notas1 = carregar_arquivos_notas(caminho_arquivo)
    pessoas_reprovadas1 = filtro_pessoas_reprovadas(notas1)
    escrever_arquivo(caminho_arquivo_pessoas_reprovadas, pessoas_reprovadas1) 
  except ValueError as error_message:
    print(f"{error_message}")
  
  print("")

processar_pessoas_reprovadas(caminho_arquivo_inexistente)
processar_pessoas_reprovadas(caminho_arquivo_existente)

print("Fim!", end="\n"*2)
