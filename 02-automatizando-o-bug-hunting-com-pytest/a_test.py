def test_um_teste_simples():
    assert True


def test_multiplica_item_da_lista():
    minha_lista = [1, 2, 3]
    assert [item * 3 for item in minha_lista] == [3, 6, 9]


"""
Este teste utiliza uma função do Pytest que age
como "afterAll/beforeAll"
"""


def test_lista_com_multiplos_items(listBeforeEachFixture):
    assert [item * 3 for item in listBeforeEachFixture] == [3, 6, 9]


def test_soma_os_itens_de_uma_lista_com_resultado_seis(listBeforeEachFixture):
    assert sum(listBeforeEachFixture) + 1 == 7
