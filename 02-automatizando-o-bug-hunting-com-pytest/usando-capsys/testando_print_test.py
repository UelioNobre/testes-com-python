msg_boas_vindas = "Bem vindo!"
msg_erro = "Houve um erro!"


def mensagem_boas_vindas_com_print():
    print(msg_boas_vindas, end="")


def test_mensagem_boas_vindas_exibe_mensagem_legal(capsys):
    mensagem_boas_vindas_com_print()
    saida = capsys.readouterr()
    assert saida.out == msg_boas_vindas


def mensagem_boas_vindas_com_sys_stderr():
    import sys

    sys.stderr.write(msg_erro)


def test_mensagem_boas_vindas_em_sys_std_err(capsys):
    # Act
    mensagem_boas_vindas_com_sys_stderr()
    saida = capsys.readouterr()

    # Assert
    assert saida.err == msg_erro
