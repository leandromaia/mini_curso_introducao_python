peso = float(input("Digite seu peso:\n\t"))
altura = float(input("Digite a sua altura:\n\t"))

def calcular_imc(peso, altura):
    resultad_imc = peso / (altura ** 2)
    return resultad_imc

resultado_calculo = calcular_imc(peso, altura)

print(f'O seu IMC é {resultado_calculo}')
