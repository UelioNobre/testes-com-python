base_media = 4
notas_carregadas = []

while len(notas_carregadas) < base_media:
  nota = input(f"Insira o valor da nota {len(notas_carregadas) + 1}: ")
  
  if nota.isdigit() == False:
      raise ValueError(f":: ERROR! O valor da nota ({nota}) é inválido!")
  else:
    notas_carregadas.append(int(nota))

media = sum(notas_carregadas) / base_media
print(f"Media das {base_media} notas {notas_carregadas}: ", media)