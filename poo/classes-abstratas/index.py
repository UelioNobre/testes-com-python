import abc


class InterfaceFormal(abc.ABC):
    @abc.abstractclassmethod
    def example(self) -> None:
        pass


teste = InterfaceFormal()
