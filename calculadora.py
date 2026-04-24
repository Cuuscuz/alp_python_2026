print("""
      Olá, bem vindo à calculadora de 4 operações!!
      Escolha a desejada:
      1. Soma.
      2. Subtração.
      3. Divisão.
      4. Multiplicação.
      """)

oper = int(input("Já se decidiu? Digite a operação desejada: "))

if oper < 1 or oper > 4:
    print("Infelizmente essa não é uma opção válida...\nTente novamente!")

else:
    print("Ok, diga-me os números.")
    num1 = float(input("Primeiro número: "))
    num2 = float(input("Segundo número: "))

    if oper == 1:
        soma = num1 + num2
        print(f"O resultado da soma é {soma}!")

    elif oper == 2:
        subt = num1 - num2
        print(f"O resultado da subtração é {subt}!")

    elif oper == 3:
        div = num1 / num2
        print(f"O resultado da divisão é {div}!")

    elif oper == 4:
        mult = num1 * num2
        print(f"O resultado da multiplicação é {mult}")
        