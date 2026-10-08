print("Simulador de Rendimento CDB|Tesouro Direto")

valorInicial = float(input("Digite o valor inicial no padrão: R$00.00 "))
valorInvestido = float(input("Digite o valor a ser investido mensalmente no padrão: R$00.00 "))
tempoMes = int(input("Digite o tempo em meses que deseja investir: "))
rendimentoMensal = float(input("Digite o rendimento mensal em %: "))

def calcularRendimentoBruto():
    valorTotal = valorInicial
    taxa = rendimentoMensal / 100
    for i in range(tempoMes):
        valorTotal += valorInvestido
        rendimentoBruto = taxa * valorTotal
        valorTotal += rendimentoBruto
    return valorTotal

print(f"O valor final será de: R${calcularRendimentoBruto()}")