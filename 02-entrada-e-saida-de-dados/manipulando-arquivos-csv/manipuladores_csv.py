import csv

def read_csv_file(caminho_arquivo):
  with open(caminho_arquivo, encoding="utf8") as ponteiro:
    dados = csv.reader(ponteiro, delimiter=",", quotechar='"')
  
    header, *conteudo = dados
  
  return (header, conteudo)

def write_csv_file_hard_mode(arquivo_saida, cabecalho, conteudo):
  # Escreve o relatório em CSV
  with open(arquivo_saida, mode='w', encoding='utf-8') as ponteiro:
    writer = csv.writer(ponteiro)
    
    # Registra o cabecalho
    writer.writerow(cabecalho)
    
    # Registra o conteúdo
    for department, grades in conteudo.items():
      row = [department, grades]
      writer.writerow(row)

def department_filter(payload):
  group_by_department = {}
  for row in payload:
    department = row[15]
    
    if department not in group_by_department:
      group_by_department[department] = 0
    
    group_by_department[department] += 1
  
  return group_by_department

def read_csv_as_dict(caminho_arquivo):
# lê os dados
    with open(caminho_arquivo, encoding = "utf-8") as file:
        graduacao_reader = csv.DictReader(file, delimiter=",", quotechar='"')

        # A linha de cabeçalhos é utilizada como chave do dicionário
        # agrupa cursos por departamento
        group_by_department = {}
        for row in graduacao_reader:
            department = row["unidade_responsavel"]
            if department not in group_by_department:
                group_by_department[department] = 0
            group_by_department[department] += 1
    
    return group_by_department