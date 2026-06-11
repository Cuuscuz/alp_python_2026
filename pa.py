a = int(input("Digite o primeiro termo da PA: "))
b = int(input("Digite a quantidade de termos: "))
r = int(input("Digite a razão da PA: "))

for num in range(b):
    print(a + num * r)