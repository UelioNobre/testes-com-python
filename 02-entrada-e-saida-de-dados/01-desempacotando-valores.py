print("Desempacotando string com Python")
string_original = "cd"
a, b = string_original
print(f"String original: {string_original}")
print(f"O valor da variável a: {a}")
print(f"O valor da variável b: {b}", end="\n\n")

print("Desempacotando lista com Python")
localizacao = ['Missão Velha', 'Ceará', 'Brazil']
cidade, estado, pais = localizacao
print(f"Lista original: {localizacao}")
print(f"O valor da variável cidade: {cidade}")
print(f"O valor da variável estado: {estado}")
print(f"O valor da variável pais: {pais}", end="\n\n")

print("Desempacotando tupla com Python")
perfil = ('Uélio Nobre', "Missão Velha", "Ceará", "Brazil")
usuario, *endereco = perfil
print(f"Tupla original: {perfil}")
print(f"O valor da variável usuario: {usuario}")
print(f"O valor da variável endereco: {endereco}", end="\n\n")




