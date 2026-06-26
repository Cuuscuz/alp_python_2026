usuarios = {}

quantidade = int(input("Quantos usuários deseja cadastrar? "))

for i in range(quantidade):
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    usuarios[usuario] = senha

print("\nLOGIN")

usuario_login = input("Usuário: ")
senha_login = input("Senha: ")

if usuario_login in usuarios:
    if usuarios[usuario_login] == senha_login:
        print("Login realizado com sucesso!")
    else:
        print("Senha incorreta!")
else:
    print("Usuário não cadastrado!")