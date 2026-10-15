entrada = []

def mediaDosJuizes(entrada):
    maior = entrada[0]
    menor = entrada[4]
    for notaMNR in entrada:
        if notaMNR < menor:
            menor = notaMNR
    print(menor)
    for notaMR in entrada:
        if notaMR > maior:
            maior = notaMR
    print(maior)
    soma = sum(entrada)
    somaFinal = soma - maior - menor
    media = somaFinal / (len(entrada) - 2)

    print(media)

    
mediaDosJuizes([1,2,3,4,5])