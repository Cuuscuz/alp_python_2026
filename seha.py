senha = int(input("Digite a senha: "))

while senha != 12345:
    print("Acesso negado, tente novamente!")
    senha = int(input("Digite a senha novamente: "))

print("Acesso liberado!")