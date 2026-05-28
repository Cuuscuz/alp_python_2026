tent = 0

while tent < 3:
    usuario = input("Digite o nome de usuario: ")
    senha = int(input("Digite a senha: "))
    
    if usuario == "aluno" and senha == 12345:
        print("Acesso liberado!")
        break
    
    else:
        tent += 1
        print("Tente novamente")
        if tent == 3:
            print("Você já tentou 3 vezes!")