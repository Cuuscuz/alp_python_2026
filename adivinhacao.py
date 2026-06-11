from random import randint

num_sort = randint(1,10)
tent = 0
acerto = False

while tent != 3 and not acerto:
    num = int(input("Digite um número de 1 à 10:"))

    if num == num_sort:
        acerto = True 
        print("Parabéns, você acertou!!!")

    elif num > num_sort:
        tent += 1
        print("Você errou, tente um número menor!")

    elif num < num_sort:
        tent += 1
        print("Você errou, tente um número maior!")

if tent == 3:
    print("Você já tenou 3 vezes, programa encerrado!!")