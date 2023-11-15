from rich import print
from manipuladores_json import read_with_load

caminho_pokemons_json = "pokemons.json"

pokemons = read_with_load(caminho_pokemons_json)
primeiro_pokemon = pokemons[0]

print(f"Total de Pokemons: {len(pokemons)}")
print(f"Primeiro pokemon")
print(primeiro_pokemon)