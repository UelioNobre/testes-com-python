def calcular_comissao(valor, porcentagem):
    return valor * porcentagem


salarios_e_comissoes = [
    [100, 0.10],
    [1000, 0.15],
]

for valores in salarios_e_comissoes:
    salario, porcentagem = valores

    print(f"Valor do salário: R${salario}")
    print(f"Porcentagem de acréscimo: {porcentagem}%")

    valor_comissao = calcular_comissao(salario, porcentagem)
    proventos_totais = salario + valor_comissao

    print(f"Valor da comissão: R${valor_comissao}")
    print(f"Total de proventos: R${proventos_totais}", end="\n" * 2)
