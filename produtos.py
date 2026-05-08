
print("Preencha as informações do produto a seguir:")

preco = float(input("Digite o preço do produto:"))
if preco <= 0:
    print("Digite o preço de um produto real e válido.")

else:
    quant = int(input("Agora digite o quantidade que foi comprada deste produto:"))
    total = preco * quant
    print(f"O valor total da compra é de R${total}.")