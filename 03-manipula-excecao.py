base_media = 4
notas_carregadas = []

while len(notas_carregadas) < base_media:
  nota = input(f"Insira o valor da nota {len(notas_carregadas) + 1}: ")
  
  try:
    if nota.isdigit() == False:
      raise ValueError(f":: ERROR! O valor da nota ({nota}) é inválido!")
    else:
      notas_carregadas.append(int(nota))

  except ValueError as error_message:
    print(error_message, end="\n" * 2)
  
  else:
    print(f"... Nota {len(notas_carregadas)} carregada com sucesso!")
  
  finally:
    print("... Preparando para carregar a próxima nota...")

media = sum(notas_carregadas) / base_media

print("\n" * 2)
print(f"Notas lidas pelo sistema", notas_carregadas)
print(f"Media das {base_media} notas {notas_carregadas} é: ", media)
print("Fim!")
print("\n" * 2)