conteudos = ('Arquivo', 'Editar', 'Janela', 'Ajuda')


caminho_arquivo_simples = 'arquivo-simples.txt'
caminho_arquivo_multilinhas = 'arquivo-multilinhas.txt'

arquivo = open(caminho_arquivo_simples, mode='w')

# Escreve em uma só linha
for conteudo in conteudos:
  arquivo.write(conteudo)

arquivo.close()


# Escreve em várias linhas
linhas = [f"{linha}\n" for linha in conteudos]
arquivo = open(caminho_arquivo_multilinhas, mode='w')
arquivo.writelines(linhas)
arquivo.close()
