
limite = float(input("Me diga qual a nota máxima que o seu sistema de notas ultiliza:"))
nota1 = float(input("Forneça ao sistema sua nota MENSAL:"))
nota2 = float(input("Forneça ao sistema sua nota BIMESTRAL:"))
quali = float(input("Forneça ao sistema seu QUALITATIVO:"))

media = (nota1 + nota2 + quali) / 3
nota_minima = limite * 0.6

if media >= nota_minima:
    print(f"Aprovado! Sua média é maior que 60%. Pois se trata de {media}")

else:
    print(f"Reprovado!! Sinto muito, sua média é {media} e não ultrapassa 60%. :[")