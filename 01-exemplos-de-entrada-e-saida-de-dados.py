import sys

print("Imprimindo cada letra do nome do usuário no terminal de duas formas")
username = input("Informe seu nome: ")
letras = list(username)

for linha, letra in enumerate(letras, start=1):
  print(linha, letra)
  
print("\n"*2)
print("Escreva um programa que receba vários números naturais e calcule a soma desses valores.")
numeros = input("Insira números separados por espaço: ")
numeros_separados = numeros.split()
resultado_soma = 0
for numero in numeros_separados:
  if numero.isdigit():
    resultado_soma += int(numero)
  else:
    print(f"Erro ao somar valores, {numero} é um valor inválido", file=sys.stderr)

print(f"O resultado da soma é: {resultado_soma}", file=sys.stdout)
