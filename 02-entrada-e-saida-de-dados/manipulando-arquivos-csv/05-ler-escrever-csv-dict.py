from manipuladores_csv import read_csv_as_dict

arquivo_csv_entrada = 'graduacao_unb.csv'
conteudo_csv = read_csv_as_dict(arquivo_csv_entrada)

print(conteudo_csv)