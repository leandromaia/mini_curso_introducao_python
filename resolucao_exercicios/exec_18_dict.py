def main():
    lista_contatos = []
    
    while True:
        nome = input("Por favor forneça o nome do contato:\n-> ")
        telefone = int(input(f"Forneça o número de telefone do contato: {nome}:\n-> "))
    
        contato = {"nome": nome, "telefone": telefone}
        lista_contatos.append(contato)

        resp = input("Deseja cadastrar mais contatos?\n1- Sim\n2- Não\n-> ")
        if resp == "2":
            break

    exibir_contatos(lista_contatos)


def exibir_contatos(contatos):
    for index, contato in enumerate(contatos):
        print(f"Contato {index + 1}:\n\tnome: {contato.get('nome')}\n\ttelefone: {contato.get('telefone')}")


if __name__ == "__main__":
    main()
