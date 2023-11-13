import sys

if __name__ == "__main__":
  
  if len(sys.argv) > 1:
    print("Aplicação executando argumento opcionais")
  else:
    print("Aplicação executando sem argumentos opcionais")
  
  for argumento in sys.argv:
    print(f"Argumento recebido: {argumento}")
  
  print("\n" * 2)
  print("ENTRADA DE DADOS")
  user_input = input("Digite uma mensagem: ")
  print(f"O valor digitado foi: {user_input}")
