nome = str(input("Digite o nome do produto:"))
preco = float(input("Digite o preço do produto:"))
estoque = int(input("Qual a quantidade em estoque?:"))
promo = str(input("O produto está em promoção? (S/N)")).upper() == "S"

produto = [nome, preco, estoque, promo]

print(f"Nome......:{produto[0]}")
print(f"Preço.....:{produto[1]}")
print(f"Estoque...:{produto[2]}")
print(f"Promoção..:{"Sim" if produto[3] else "Não"}")