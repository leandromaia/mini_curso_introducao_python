import math


val = int(input("Informe um número para ser elevado ao cubo:\n-> "))

val_cubo = math.pow(val, 3)

if val_cubo > 0 and val_cubo < 100:
    print(f"O valor: {val} está na faixa válida de 0 a 100.")
else:
    print(f"O valor: {val} está FORA da faixa válida de 0 a 100.")

print(f"O valor {val} elevado ao cubo é {val_cubo} ")