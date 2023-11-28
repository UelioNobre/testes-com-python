def test_multiplica_item_da_lista():
    minha_lista = [1, 2, 3]
    assert [item * 3 for item in minha_lista] == [3, 6, 9]
