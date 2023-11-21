from math import factorial


def map_factorial(numbers):
    result = []
    imposible_results = []

    for num in numbers:
        try:
            result.append(factorial(num))
        except TypeError as err:
            print("Erro de tipo")
            print(f"Numero: {num}, Type: {type(num)}")
            print(f"Erro: {err}", end="\n" * 3)
            imposible_results.append(num)
        except ValueError as err:
            print("Erro de valor")
            print(f"Numero: {num}, Type: {type(num)}")
            print(f"Erro: {err}", end="\n" * 3)
            imposible_results.append(num)

    return [result, imposible_results]


def main():
    input_list = ["um", 2, 3, 4, -5]
    results, impossible_results = map_factorial(input_list)
    print(f"Números calculados: {results}")
    print(f"Valores não calculados: {impossible_results}")


if __name__ == "__main__":
    main()

# O código acima parece que funciona bem, mas
# Não há nenhuma nenhum instrução para saída de dados.
# Sejam elas sys.stdout.write ou o BIF "print"
