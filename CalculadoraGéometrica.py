import math


def calcular_area_retangulo():
    print("\n--- Cálculo de Retângulo ---")

    while True:
        try:
            comprimento = float(input("Digite o comprimento do retângulo: "))
            if comprimento > 0:
                break
            else:
                print("O comprimento deve ser um número positivo e maior que zero.")
        except ValueError:
            print("Inválido. Por favor, digite um número.")

    while True:
        try:
            largura = float(input("Digite a largura do retângulo: "))
            if largura > 0:
                break
            else:
                print("A largura deve ser um número positivo e maior que zero.")
        except ValueError:
            print("Inválido. Por favor, digite um número.")

    area = comprimento * largura
    print(f"\nA área do retângulo é: {area:.2f}")

    if comprimento == largura:
        print("Este retângulo é um quadrado.")
    else:
        print("Este retângulo não é um quadrado.")


def calcular_area_circulo():
    print("\n--- Cálculo de Círculo ---")

    # OBTER E VALIDAR RAIO
    while True:
        try:
            raio = float(input("Digite o raio do círculo: "))
            if raio > 0:
                break
            else:
                print("O raio deve ser um número positivo e maior que zero.")
        except ValueError:
            print("Inválido. Por favor, digite um número.")

    area = math.pi * (raio ** 2)

    print(f"\nA área do círculo é: {area:.2f}")


def calcular_volume_tetraedro():
    print("\n--- Cálculo de Volume do Tetraedro ---")

    while True:
        try:
            aresta = float(
                input("Digite o comprimento da aresta do tetraedro: "))
            if aresta > 0:
                break
            else:
                print("A aresta deve ser um número positivo e maior que zero.")
        except ValueError:
            print("Inválido. Por favor, digite um número.")

    numerador = aresta ** 3
    dominador = 6 * math.sqrt(2)

    volume = numerador / dominador
    print(f"\nO volume do tetraedro é: {volume:.2f}")


def main():
    continuar = True

    while continuar:
        print("\n==============================")
        print("Calculadora Géometrica")
        print("==============================")

        escolha = input(
            "Qual forma geométrica deseja calcular? (R)Retângulo, (C)Círculo (T)Tetraedro: ").lower()

        if escolha == 'r':
            calcular_area_retangulo()
        elif escolha == 'c':
            calcular_area_circulo()
        elif escolha == 't':
            calcular_volume_tetraedro()
        else:
            print(
                "Opção inválida. Por favor, digite 'r' para Retângulo, 'c' para Círculo ou 't' para Tetraedro.")
            continue

        resposta = input("\nDeseja fazer outro cálculo? (s/n): ").lower()
        if resposta != 's':
            continuar = False

    print("\nObrigado por usar a calculadora!")


if __name__ == "__main__":
    main()
