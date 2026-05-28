#Professor pague um café com leite pra mim. (:
print("Informe os nomes e os valores dos médicamentos solicitados.")

valor_t = 0
menor_p = float('inf')

for med in range (1,6):
    med_nome = (input(f"Informe o nome do {med}° médicamento: "))
    med_valor = int(input(f"Informe o valor do {med}° médicamento: "))

    if med_valor < menor_p:
        menor_p = med_valor
        nome_menor_p = med_nome

valor_t = valor_t + med_valor
media = valor_t / 5

print(f"""
    Os resultados são:
      O medicamento mais barato é {nome_menor_p} e seu preço é R${menor_p}.
      A média dos preços informados é {media}.
""")