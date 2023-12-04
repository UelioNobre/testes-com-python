def show_message():
    message = input("Informe seu nome: ")

    return f"A entrada informada foi: {message}"


def mensagem_padrao():
    print("Bem vindo!")


def mensagem_boas_vindas():
    mensagem_padrao()
    result = show_message()
    return result
