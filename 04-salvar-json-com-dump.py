
from rich import print
from manipuladores_json import write_with_dump, read_with_loads


caminho_arquivo_json_dump = 'arquivo-criado-com-json-dump.json'
string_json = '{"uma": "json", 2: "formatados", "como": "string", "numeros": [1, 3, 4]}'

write_with_dump(caminho_arquivo_json_dump, string_json)
conteudo = read_with_loads(caminho_arquivo_json_dump)

print(conteudo)