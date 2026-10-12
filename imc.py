peso = float(input("digite seu peso em kg"))
altura = float(input("digite sua altura em metros"))

def calcularIMC():
    imc = peso / (altura*2)
    if imc <= 18.5:
        print("peso normal")
    elif imc <= 24.9:
        print("sobre peso")
    elif imc <= 29.9:
        print("obseidade grau 1")
    elif imc <= 34.9:
        print("obseidade grau 2")
    else:
        print("obseidade grau 3")