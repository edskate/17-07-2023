
def calcular_fatorial(num):
    fatorial = 1
    for i in range(1, num + 1):
        fatorial *= i
    return fatorial

# Função principal


def main():

    num = int(input("Digite um número inteiro: "))

    fatorial = calcular_fatorial(num)
    print(f"O fatorial de {num} é {fatorial}.")


main()
