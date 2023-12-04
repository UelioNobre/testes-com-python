import pytest

"""Usando Fixture

Ao criar um metodo fixture, ele deve ser passado 
com parametro, para a função de teste
"""


@pytest.fixture
def listBeforeEachFixture():
    return [1, 2, 3]
