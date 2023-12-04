from IPerson import IPerson
from typing import Any


class Printer:
    @staticmethod
    def imprime_cargo(instance: Any):
        if not isinstance(instance, IPerson):
            print("Informe uma instancia de IPerson")
        else:
            instance.print_role()
