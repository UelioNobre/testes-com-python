from rich import print
from manipuladores_json import read_with_loads

caminho_pokemons_json = "one-pokemon.json"

pokemon = read_with_loads(caminho_pokemons_json)

print(pokemon)