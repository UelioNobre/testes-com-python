from math import factorial


def map_factorial(numbers):
    result = []

    for num in numbers:
        try:
            result.append(factorial(num))
        except TypeError as err:
            print(f"Não é possivel calcular o fatorial de {num}")
            print(f"Numero: {num}, Type: {type(num)}")
            print(f"Erro: {err}", end="\n" * 3)

    return result


def main():
    input_list = ["um", 2, 3, 4, -5]
    input_factorial = map_factorial(input_list)
    print(input_factorial)


if __name__ == "__main__":
    main()

# O código acima parece que funciona bem, mas
# Não há nenhuma nenhum instrução para saída de dados.
# Sejam elas sys.stdout.write ou o BIF "print"
