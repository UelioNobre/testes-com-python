from funcoes_para_testar import show_message
from mock_functions import mock_input_hello_world


def test_show_message(monkeypatch):
    # Simula o usuário digitando no terminal
    monkeypatch.setattr("builtins.input", mock_input_hello_world)
    result = show_message()

    assert result == "A entrada informada foi: Hello world!"
