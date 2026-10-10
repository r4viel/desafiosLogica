import random 

numero = random.randint(1, 100)

def adivinhar():
    while True:
        tentativa = int(input("Digite um número entre 1 e 100: "))
        if tentativa == numero: 
            print("acertou men")
            break
        elif tentativa > numero:
            print("Menor")
        else:
            print("Maior")


adivinhar()