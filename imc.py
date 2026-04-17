print("""
      Olá! (^^)>
      Vamos ver o seu IMC de acordo com os dados que você irá me fornecer.
      Mas antes observe a seguinte tabela para saber o seu nivel dentre 
      os padrões...

      ----------TABELA IMC----------
      Menor que 18.5 | magreza
      Entre 18.5 e 24.9 | Tranquilo, peso normal
      Entre 25.0 e 29.9 | Sobrepeso
      Entre 30.0 e 39.9 | Obesidade
      Acima de 40 | Slk, vai estourar

      Agora vamos preencher seu dados!!!!

      """)


peso = float(input("Informe seu peso corporal em Kg:"))
altura = float(input("Agora informe sua altura em metros:"))

imc = peso/(altura**2)

if imc < 18.5:
    print("Magreza! Aceita ir em um rodizio?")

elif imc >= 18.5 < 25.0:
    print("Bom peso! Pode se embuxar sem medo.")

elif imc >= 25.0 < 30.0:
    print("Bora começar a se cuidar, está sobrepeso!")

elif imc >= 30.0 < 39.0:
    print("Obesidade... Que tal um nutricionista?")

else:
    print("Tentar fazer dieta? \nRelaxe!!! Não vai dar tempo... (°~°)")