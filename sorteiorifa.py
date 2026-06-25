import random

participantes = []

qtd = int(input("Quantas rifas foram vendidas? "))

cont = 0

while cont < qtd:
    nome = input("Nome do comprador: ")
    participantes.append(nome)
    cont += 1

ganhador = random.choice(participantes)

print(f"\nO ganhador foi: {ganhador}")