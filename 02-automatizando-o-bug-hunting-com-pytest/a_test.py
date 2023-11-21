import pytest

"""Usando Fixture

Ao criar um metodo fixture, ele deve ser passado 
com parametro, para a função de teste
"""


@pytest.fixture
def my_list():
    return [1, 2, 3]


def test_um_teste_simples():
    assert True


def test_multiplica_item_da_lista():
    minha_lista = [1, 2, 3]
    assert [item * 3 for item in minha_lista] == [3, 6, 9]


"""
Este teste utiliza uma função do Pytest que age 
como "afterAll/beforeAll"
"""


def test_lista_com_multiplos_items(my_list):
    assert [item * 3 for item in my_list] == [3, 6, 9]
