def fatorial(numero):
    resultado = 1

    for i in range(numero, 0, -1):
        resultado = resultado * i

    return resultado


while True:
    numero = int(input("Digite um número inteiro positivo (0 para sair): "))

    if numero == 0:
        print("Programa finalizado...")
        break

    print(f"O fatorial de {numero} é {fatorial(numero)}")