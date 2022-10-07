def main():
    letras = ["z", "U", "A", "X", "c", "C", "L", "E", "i"]
    
    total_consoantes = 0

    for l in letras:
        if l.upper() not in "AEIOU":
            total_consoantes += 1
    
    print(f"A lista criada hard code, possui o total de {total_consoantes} consoantes.")


if __name__ == "__main__":
    main()
