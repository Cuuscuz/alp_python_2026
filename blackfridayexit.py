while True:
    opc = int(input("""
    Qual será a forma de pagamento?
                    0. Sair do progama.
                    1. A vista.
                    2. Débito.
                    3. Crédito.
        
        Digite uma das opções:
"""))
    
    if opc == 0:
        print("Progama finalizado...")
        break

    else:

        valor = int(input("Agora informe o valor da compra: "))

        if (opc == 0 or opc == 1 or opc == 2 or opc == 3):
            if opc == 1:
                desc = valor * 0.15
                valor_f = valor - desc
                print(f"O valor final da compra é de R${valor_f}")

            elif opc == 2:
                desc = valor * 0.10
                valor_f = valor - desc
                print(f"O valor final da compra é de R${valor_f}")

            elif opc == 3:
                desc = valor * 0.05
                valor_f = valor - desc
                print(f"O valor final da compra é de R${valor_f}")
        
        else:
            print("Digite uma das opções válidas.")