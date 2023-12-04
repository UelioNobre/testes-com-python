# Monkeypatch

Um stub Python (ou é mais que isso?)

Para usar a fixture monkeypatch, deve configurar antes de chamar uma determinada funcao.

### monkeypatch.setattr - 3 parametros

A opção `setattr`, recebe três argumentos:
  1 - O arquivo/módulo que deseja ser mockado
  2 - A função do arquivo/modulo
  3 - A função que servirá de mock, do testador

Exemplo: monkeypatch.setattr(`o modulo`, `a funcao do modulo`, `a funcao mock`)

```python
    # Mockando o módulo requests
    def mock_get(*args, **kwargs):
        return MockResponse()

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)
```
### monkeypatch.setattr - 2 parametros

Na versão curta, `setattr`, recebe dois argumentos:
  1 - O arquivo/módulo que deseja ser mockado, seguido da função. Separado por ponto
  2 - A função que servirá de mock, do testador

Exemplo: monkeypatch.setattr(`o modulo`, `a funcao do modulo`, `a funcao mock`)

```python
    # Mockando o módulo requests
    monkeypatch.setattr("requests.get", mock_input_user)
```



Ver mais na [Documentação monkeypatch](https://docs.pytest.org/en/latest/how-to/monkeypatch.html).
