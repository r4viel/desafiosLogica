etapa1 = int(input('Digite a sua nota do primeiro: '))
etapa2 = int(input('Digite a sua nota do segundo: '))
etapa3 = int(input('Digite a sua nota do terceiro: '))
etapa4 = int(input('Digite a sua nota do quarto: '))

PESOSEMESTRE1 = 2
PESOSEMESTRE2 = 3

def calcularNota():
    MDS1=(etapa1*PESOSEMESTRE1)+(etapa2*PESOSEMESTRE1)
    MDS2=(etapa3*PESOSEMESTRE2)+(etapa4*PESOSEMESTRE2)

    MDF=(MDS1+MDS2)//10

    print(MDF)

calcularNota()