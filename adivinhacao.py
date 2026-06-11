from random import randint

num_sort = randint(1,10)
tent = 0

while tent != 3:
    num = int(input("Escolha um número de 1 à 10: "))

    if num < num_sort:
        tent += 1
        if tent == 3: 
            break
        else:
            print("Você errou, tente um número maior!")

    elif num > num_sort:
        tent += 1
        if tent == 3:
            break
        else:
            print("Você errou, tente um número menor!")

    else:
        print("Parabéns, você acertou!")
        break

if tent == 3:
    print("Errou novamente! Limite de tentativas encerrados")