a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
soma = 0

if a >= b:
    print("Erro no programa!")

else:
    for num in range (a, b + 1):
        soma += num

    print(f"A somatória de todos os números de {a} até {b} é {soma}.")
