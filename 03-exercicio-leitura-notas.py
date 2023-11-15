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
