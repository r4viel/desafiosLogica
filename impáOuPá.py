import random

numero = int(input("Digite um número: "))

def impaOuPa():
    if numero % 2 == 0:
        print("é pá")
    else:
        print("é impá")

impaOuPa()

def advineSeEPa():
    num = random.randint(1, 100)

    adivinho = input("digite impa ou pa para chutar: ")
    if adivinho == "pa":
        if num % 2 == 0:
            print("acerto miseravi")
        else:
            print("erro lixoooo!!")
    elif adivinho == "impa":
        if num % 2 !=0:
            print("acerto miseravi")
        else:
            print("erro lixoooo!!")

advineSeEPa()