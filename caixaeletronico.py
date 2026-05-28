
senha = int(input("Olá, digite a senha: "))
tent = 3

while tent != 0:
    if senha == 123456:
        print("Olá, ALISSON. Seja bem vindo ao nosso banco!")
        break
        
    else: 
        if tent > 1:
            tent -= 1
            print(f"Senha errada, você ainda tem {tent} tentativas!")
            senha = int(input("Digite novamente sua senha: "))

        else:
            tent -= 1
            print("Sua senha foi bloqueada! Vá até alguma agência para desbloquear.")
            