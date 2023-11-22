msg_boas_vindas = "Bem vindo!"


def mensagem_boas_vindas():
    print(msg_boas_vindas, end="")


def test_mensagem_boas_vindas_exibe_mensagem_legal(capsys):
    mensagem_boas_vindas()
    saida = capsys.readouterr()
    assert saida.out == msg_boas_vindas
