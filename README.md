# Testes com Python

### Ambiente virtual

Para obter uma maior independência de uma aplicação em Python é interessante ter um ambiente isolado das dependências do projeto.

Para isso, existe o Ambiente Virtual *(venv)*, que pode ser realizada com o seguinte comando:

```bash
$ python3 -m venv .venv
```

Esse comando irá criar um ambiente virtual isolado, para que as dependencias do projetos fiquem localizadas em uma estrutura própria de diretório, exclusiva da própria aplicação e não do que há instalado computador do usuário.

Dessa forma, é possível "portar" a aplicação para diversos dispositivos, evitando a pronúncia da seguinte frase **"no meu computador funciona"**.

---

#### Ativando o ambiente virtual
Depois de criado o ambiente virtual para aplicação, agora é preciso "ativar". O comando para isso é:

```bash
$ source .venv/bin/activate
```

Ao digitar o comando e pressionar a tecla _ENTER_, o términal terá a seguinte aparência (_ou coisa parecida_):
```bash
(.venv) ➜ testes-com-python 
```

---

#### Desativando o ambiente virtual
Depois de criado o ambiente virtual para aplicação e o ambiente estiver ativado, para **DESATIVAR** é preciso digitar o seguinte comando e pressionar _ENTER_:

```bash
$ deactivate
```