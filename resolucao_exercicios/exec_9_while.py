print("---------- Bem Vindo a Calculadora Python -------------")
opcao = None

while opcao != "5":
    opcao = input("Escolha a operação aritmética:\n\t1- Adição\n\t2- Subtração"\
        "\n\t3- Multiplicação\n\t4- Divisão\n\t5- Sair\n\t-> ")

    if opcao != "5":
        val_1 = float(input("Forneça o valor 1:\n-> "))
        val_2 = float(input("Forneça o valor 2:\n-> "))

    resultado = 0

    match opcao:
        case "1":
            resultado = val_1 + val_2

        case "2":
            resultado = val_1 - val_2

        case "3":
            resultado = val_1 * val_2

        case "4":
            resultado = val_1 / val_2
    
    if opcao != "5":
        print(f"Resultado Total: {resultado}\n")
