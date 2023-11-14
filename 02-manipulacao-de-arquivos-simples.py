conteudos = ('Arquivo', 'Editar', 'Janela', 'Ajuda')


caminho_arquivo_simples = 'arquivo-simples.txt'

arquivo = open(caminho_arquivo_simples, mode='w')

# Escreve em uma só linha
for conteudo in conteudos:
  arquivo.write(conteudo)

arquivo.close()
