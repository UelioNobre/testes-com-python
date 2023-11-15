import json


def write_with_dump(caminho_arquivo, conteudo):
  with open(caminho_arquivo, mode='w') as ponteiro:
    json.dump(conteudo, ponteiro)
    

def write_with_dumps(caminho_arquivo, conteudo):
  with open(caminho_arquivo, mode='w') as ponteiro:
    prepare_json = json.dumps(conteudo)
    ponteiro.write(prepare_json)


def read_with_load(caminho_arquivo):
  with open(caminho_arquivo, mode='r') as ponteiro:
    pokemons = json.load(ponteiro)["results"]
  
  return pokemons


def read_with_loads(caminho_arquivo):
  with open(caminho_arquivo, mode="r") as ponteiro:
    conteudo = json.loads(ponteiro.read())
  
  return conteudo