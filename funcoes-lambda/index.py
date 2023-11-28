def calcular_comissao(valor, porcentagem):
    return valor * porcentagem


def show_extrato_cli(salario, porcentagem, comisao, proventos_totais):
    print(f"Valor do salário: R${salario}")
    print(f"Porcentagem de acréscimo: {porcentagem}%")

    print(f"Valor da comissão: R${comisao}")
    print(f"Total de proventos: R${proventos_totais}", end="\n" * 2)


salarios_e_comissoes = [
    [100, 0.10],
    [1000, 0.15],
]

for valores in salarios_e_comissoes:
    salario, porcentagem = valores
    comissao = calcular_comissao(salario, porcentagem)
    proventos_totais = salario + comissao

    show_extrato_cli(salario, porcentagem, comissao, proventos_totais)


# usando lambda
