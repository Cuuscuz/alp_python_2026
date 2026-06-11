a = int(input("Informe o primeiro número inteiro: "))
b =  int(input("Informe o segundo número inteiro: "))
soma = 0

if a >= b:
    print("Erro no programa!")
    

else:
    for num in range(a,b + 1):
        soma += num

    print(f"A soma de todos os números no intervalo de {a} à {b} é {soma}.")