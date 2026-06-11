quant = 0
soma = 0
maior = 0 

while True:
    num = int(input("Digite um número positivo: "))

    if num > 0:
        quant += 1
        soma = soma + num
        
        if num > maior:
            maior = num
    
    else:
        print("Número negativo informado!")
        break

media = soma / quant

print(f"""
O Somatório de todos os números é {soma}.
A média dos números é {media}.
O maior número é {maior}.
""")