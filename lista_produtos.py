produtos = []

while True:
    opc = str(input("Deseja informar algum produto?(S/N) "))

    if opc.upper() == "N":
        print("A lista dos itens é:")
        for nome in produtos:
            print(nome)
        break

    else:
        produto = str(input("Informe o produto que será adicionado à lista: "))
        produtos.append(produto)