import csv

arquivo_csv_entrada = 'graduacao_unb.csv'

with open(arquivo_csv_entrada, 'w', encoding='utf-8') as ponteiro:
  csv_reader = csv.DictReader(ponteiro, delimiter=",", quotechar='"')
  print(csv_reader)
  
  group_by_department = {}
  for row in csv_reader:
    department = row["unidade_responsavel"]
    
    if department not int group_by_department:
      group_by_department[department] = 0
    
    group_by_department[department] += 1

print(group_by_department)