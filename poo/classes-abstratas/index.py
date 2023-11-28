import abc


class InterfaceFormal(abc.ABC):
    @abc.abstractclassmethod
    def exibir_mensagem(self) -> None:
        pass


class ClasseConcreta(InterfaceFormal):
    def exibir_mensagem(self):
        print("Olá mundo!")
        pass


# teste = InterfaceFormal() - TypeError
teste = ClasseConcreta()
teste.exibir_mensagem()
