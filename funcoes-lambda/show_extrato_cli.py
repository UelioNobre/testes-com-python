def show_extrato_cli(salario, porcentagem, comisao, proventos_totais):
    print(f"Valor do salário: R${salario}")
    print(f"Porcentagem de acréscimo: {porcentagem}%")

    print(f"Valor da comissão: R${comisao}")
    print(f"Total de proventos: R${proventos_totais}", end="\n" * 2)
