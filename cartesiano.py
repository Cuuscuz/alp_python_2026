from math import sqrt

x1 = float(input("Informe a localização do Ponto 1 no eixo X:"))
y1 = float(input("Agora informe a localização do Ponto 1 no eixo Y:"))

print("Ótimo, temos o Ponto 1 definido, agora informe o ponto 2 a seguir...")

x2 = float(input("Informe a localização do ponto 2 no eixo X:"))
y2 = float(input("Agora informe a localização do Ponto 2 no eixo Y:"))

d = sqrt(((x2 - x1) ** 2 ) + ((y2 - y1) ** 2 ))

print(f"Pronto!! \nO valor da distâmcia entre o Ponto 1 e o Ponto 2 é {d}")