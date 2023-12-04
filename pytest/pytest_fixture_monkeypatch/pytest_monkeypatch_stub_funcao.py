import funcoes_para_testar


def mock_input_user(_):
    return "Que bela tarde!"


def mock_msg():
    print("Bom dia!")


def test_altera_mensagem_padrao(capsys, monkeypatch):
    expected_mensagem_padrao = "Bom dia!"
    expected_result = "A entrada informada foi: Que bela tarde!"

    # faz um stub de uma funcao do desenvolvedor
    # interceptando a chamada e mudando o valor em tempo de execucao
    monkeypatch.setattr(funcoes_para_testar, "mensagem_padrao", mock_msg)

    # Simula o usuário digitando no terminal
    monkeypatch.setattr("builtins.input", mock_input_user)

    result = funcoes_para_testar.mensagem_boas_vindas()

    captured = capsys.readouterr()

    assert expected_mensagem_padrao in captured.out
    assert expected_result in result
