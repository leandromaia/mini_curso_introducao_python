def main():
    alturas = []
    idades = []
    total_pessoas = 2

    for i in range(total_pessoas):
        altura = float(input(f"Forneça a altura da pessoa {i + 1}:\n-> "))
        idade = int(input(f"Forneça a idade da pessoa  {i + 1}:\n-> "))
        
        alturas.append(altura)
        idades.append(idade)

    for i in range(total_pessoas):
        print(f"Pessoa {i + 1}:\nAltura: {alturas[i]}\nIdade: {idades[i]}\n")


if __name__ == "__main__":
    main()
