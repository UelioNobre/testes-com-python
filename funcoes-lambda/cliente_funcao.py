from show_extrato_cli import show_extrato_cli
from calculos_de_porcentagens import calcular_comissao

salarios_e_comissoes = [
    [100, 0.10],
    [1000, 0.15],
]

for valores in salarios_e_comissoes:
    salario, porcentagem = valores
    comissao = calcular_comissao(salario, porcentagem)
    proventos_totais = salario + comissao

    show_extrato_cli(salario, porcentagem, comissao, proventos_totais)
