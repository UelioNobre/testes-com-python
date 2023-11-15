# Manipulando arquivos JSON com Python

Para manipular arquivo JSON com python, deve-se usar o módulo `json` embutido na linguagem.

```bash
import json
```

Para uma melhor visualização no terminal dos arquivos `.json`, utilizamos uma biblioteca `Python`, chamada `rich`. Dela, importamos a nossa função personalizada `print`, formatando a saída para melhor legibilidade.

```bash
$ pip instal rich
```

---

## Funções básicas do módulo `json`
Para manipular arquivos `json`, temos quatro funções básicas que podem ser utilizadas do módulo `json`.
São elas:

### Para leitura de arquivos:
- **`load`**

  Converte a saída de dados, feito pela leitura de um arquivo (utilizando `open` e `read()`)para uma estrutura válida em `json`.

- **`loads`**

  Converte uma saída de dados (`string`, `bytes`, `bytesarray`) para uma estrutura `json` válida.

#### Exemplo de leitura de arquivos json usando `load`
```python
import json
from rich import print

caminho_pokemons_json = "pokemons.json"

with open(caminho_pokemons_json, mode='r') as conteudo_pokemons:
  pokemons = json.load(conteudo_pokemons)["results"]

primeiro_pokemon = pokemons[0]

print(f"Total de Pokemons: {len(pokemons)}")
print(f"Primeiro pokemon: {primeiro_pokemon}")
```

<details>

<summary>Resultado da saída:</summary>

```json
{
  "results": [
    {
      "national_number": "001",
      "evolution": null,
      "sprites": {
        "normal": "https://img.pokemondb.net/sprites/omega-ruby-alpha-sapphire/dex/normal/bulbasaur.png",
        "large": "https://img.pokemondb.net/artwork/bulbasaur.jpg",
        "animated": "https://img.pokemondb.net/sprites/black-white/anim/normal/bulbasaur.gif"
      },
      "name": "Bulbasaur",
      "type": [
        "Grass",
        "Poison"
      ],
      "total": 318,
      "hp": 45,
      "attack": 49,
      "defense": 49,
      "sp_atk": 65,
      "sp_def": 65,
      "speed": 45
    },
    { ... }
  ]
}
```
</details>

---

#### Exemplo de leitura de arquivos json usando `loads`
```python
import json
from rich import print

caminho_pokemons_json = "one-pokemon.json"

arquivo_pokemon = open(caminho_pokemons_json, mode="r")
json_como_string = arquivo_pokemon.read()

pokemon = json.loads(json_como_string)

print(pokemon)
```

<details>
<summary>Resultado da saída:</summary>

```json
{
  "national_number": "001",
  "evolution": null,
  "sprites": {
    "normal": "https://img.pokemondb.net/sprites/omega-ruby-alpha-sapphire/dex/normal/bulbasaur.png",
    "large": "https://img.pokemondb.net/artwork/bulbasaur.jpg",
    "animated": "https://img.pokemondb.net/sprites/black-white/anim/normal/bulbasaur.gif"
  },
  "name": "Bulbasaur",
  "type": [
    "Grass",
    "Poison"
  ],
  "total": 318,
  "hp": 45,
  "attack": 49,
  "defense": 49,
  "sp_atk": 65,
  "sp_def": 65,
  "speed": 45
}
```
</details>

### Para escrita de arquivos:
- dump
- dumps

## Para leitura

### Usando `load`
Converte a saída de dados, feito pela leitura de um arquivo (utilizando `open` e `read()`)para uma estrutura válida em `json`.

### Usando `loads`
Converte uma saída de dados (`string`, `bytes`, `bytesarray`) para uma estrutura `json` válida.

### Usando `dump`
Salva um conteúdo `json`, em formato `string`, para um arquivo um arquivo `json`.
A diferença básica para o metodo `dump` é que `dumps`, tem o segundo parametro apontando para um ponteiro aberto para escrita de arquivo.

### Usando `dumps``
A função `dumps` prepara um conteúdo, vindo de um ponteiro `file.read()`, para json.
É precisa executar a função de escrito do ponteiro para que o arquivo seja salvo com sucesso.
