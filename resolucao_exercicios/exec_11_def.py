def write_data(name, cpf, address, file_name):
    new_file = open(file_name, "w")
    new_file.write(f"Nome: {name} ")
    new_file.write(f"CPF: {cpf} ")
    new_file.write(f"Endereço: {address} ")

    
def init():
    name = input("Forneça o seu nome: ")
    cpf = input("Forneça o seu CPF: ")
    address = input("Forneça o seu endereço: ")
    file_name = input("Forneça o nome do arquivo em que deseja gravar os seus dados: ")

    write_data(name, cpf, address, file_name)


if __name__ == "__main__":
    init()