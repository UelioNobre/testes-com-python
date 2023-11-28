def calcular_comissao(valor, porcentagem):
    return valor * porcentagem


calcular_comissao_lambda = lambda x, y: x * y

salarios_e_comissoes = [
    [100, 0.10],
    [1000, 0.15],
]
