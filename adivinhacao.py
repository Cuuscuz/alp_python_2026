from random import randint

numero_sorteado = randint(1, 10)
tentativas = 0

while tentativas < 3:

    jogador = int(input("Digite um número de 1 a 10: "))
    tentativas += 1

    if jogador == numero_sorteado:
        print("Parabéns, você acertou!")
        break

    elif jogador > numero_sorteado:
        print("Você errou!")
        print("Tente um número menor")

    else:
        print("Você errou!")
        print("Tente um número maior")

if jogador != numero_sorteado:
    print("Você perdeu! Fim de jogo.")