from rich import print
from manipuladores_csv import read_csv_file


caminho_arquivo_csv = 'graduacao_unb.csv'
conteudo = read_csv_file(caminho_arquivo_csv)

print(conteudo)
print('FIM')