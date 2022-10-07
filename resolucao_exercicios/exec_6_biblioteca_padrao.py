from datetime import date


ano = int(input("Forneça o ano:"))

mes = int(input("Forneça o mês:"))

dia = int(input("Forneça o dia: "))

hoje = date.today()
print(hoje)
aniversario = date(ano, mes, dia)
print(aniversario)
resultado = hoje - aniversario

print(f"Você tem o total de {resultado.days} dias")
