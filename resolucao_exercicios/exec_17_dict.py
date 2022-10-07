def main():
    nome = input("Forneça o seu nome:\n-> ")
    idade = int(input("Forneça a sua idade:\n-> "))
    telefone = input("Forneça o seu telefone:\n-> ")
    endereco = input("Forneça o seu endereço:\n-> ")
        
    meus_dados = {}
    meus_dados['nome'] = nome
    meus_dados['idade'] = idade
    meus_dados['telefone'] = telefone    
    meus_dados['endereco'] = endereco

    for chave, valor in meus_dados.items():
        print(f"{chave.capitalize()}: {valor}")


if __name__ == "__main__":
    main()
