import csv
from rich import print
from manipuladores_csv import read_csv_file, write_csv_file_hard_mode, department_filter


caminho_arquivo_csv = 'graduacao_unb.csv'
header, conteudo = read_csv_file(caminho_arquivo_csv)

cabecalho = ['Departamento', 'Total de Cursos']
group_by_department = department_filter(conteudo)

write_csv_file_hard_mode("department_report.csv", cabecalho, group_by_department)


print('FIM')