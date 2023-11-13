import sys

if __name__ == "__main__":
  print("SAÍDA DE DADOS")
  print("concatenando", "valores", "em", 2023, True, "com a função print")
  
  print("\n")
  print("Usando separador de parametro para impressao")
  print("Separando", "algumas", "palavras", True, 2023, sep=" - ")
  
  print("\n")
  print("Usando flag de fim de linha")
  print("Imprimindo", end=" ")
  print("Uma linha inteira", end=" ")
  print("De forma separada")
  
  print("\n")
  print("Imprimindo erros na saída do terminal")
  print(f"Imprimindo um erro em stderr", file=sys.stderr)
  print(f"Imprimindo uma mensagem em stdout", file=sys.stdout)
  

