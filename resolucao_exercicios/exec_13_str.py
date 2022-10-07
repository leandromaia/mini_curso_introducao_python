def main():
    nome = input("Forneça o seu nome e sobrenome separados por espaço:\n-> ")
    nome, sobrenome = nome.split()

    print(f"Confira seu nome e sobrenomes alterados:\n {nome.swapcase()} {sobrenome.swapcase()}")

    

if __name__ == "__main__":
    main()
