def main():
    while True:
        try:
            a = int(input("Digite o primeiro número: "))
            b = int(input("Digite o segundo número: "))
            op = input("Digite a operação (+, -, *, /): ")

            if op == "+":
                resultado = a + b
            elif op == "-":
                resultado = a - b
            elif op == "*":
                resultado = a * b
            elif op == "/":
                resultado = a / b
            else:
                print("Operação inválida. Tente novamente.\n")
                continue

        except ValueError:
            print("Você deve digitar números válidos. Tente novamente.\n")
            continue
        except ZeroDivisionError:
            print("Não é possível dividir por zero. Tente novamente.\n")
            continue
        else:
            print(f"\nResultado: {a} {op} {b} = {resultado}")
            break


if __name__ == "__main__":
    main()
