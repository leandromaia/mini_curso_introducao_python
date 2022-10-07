import requests


def main():
    user_cep = input("Forneça o CEP:\n-> ")

    response = requests.get(f"https://viacep.com.br/ws/{user_cep}/json/")

    if response.status_code == 200:
        print(f"O CEP informado: {user_cep} é válido!")
    else:
        print(f"O CEP informado: {user_cep} é inválido!")



if __name__ == "__main__":
    main()