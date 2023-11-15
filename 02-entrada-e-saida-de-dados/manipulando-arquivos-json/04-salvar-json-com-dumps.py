from rich import print
from manipuladores_json import write_with_dumps, read_with_loads

caminho_pokemons_json = "pokemons.json"
caminho_pokemons_dragoes = 'arquivo-criado-com-json-dumps.json'

pokemons = read_with_loads(caminho_pokemons_json)["results"]

# pegar todos os tipos de pokemons do tipo Dragaao
pokemons_dragoes = [pokemon for pokemon in pokemons if "Dragon" in pokemon['type']]

# salva os pokemons do tipo dragao
write_with_dumps(caminho_pokemons_dragoes, pokemons_dragoes)
print(pokemons_dragoes)
