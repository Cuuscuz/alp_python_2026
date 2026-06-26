usuarios = []
senhas = []

quantidade = int(input("Quantos usuários deseja cadastrar? "))

for i in range(quantidade):
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    usuarios.append(usuario)
    senhas.append(senha)

print("\nLOGIN")

usuario_login = input("Usuário: ")
senha_login = input("Senha: ")

if usuario_login in usuarios:
    posicao = usuarios.index(usuario_login)

    if senha_login == senhas[posicao]:
        print("Login realizado com sucesso!")
    else:
        print("Senha incorreta!")
else:
    print("Usuário não cadastrado!")