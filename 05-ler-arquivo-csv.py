import csv
from rich import print
from manipuladores_csv import read_csv_file


caminho_arquivo_csv = 'graduacao_unb.csv'
header, conteudo = read_csv_file(caminho_arquivo_csv)
print(header)

group_by_department = {}
for row in conteudo:
  department = row[15]
  
  if department not in group_by_department:
    group_by_department[department] = 0
  
  group_by_department[department] += 1
  
print(department)
print(group_by_department)

print('FIM')