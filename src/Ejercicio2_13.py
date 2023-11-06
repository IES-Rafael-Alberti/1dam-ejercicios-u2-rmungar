def eco(entrada):
    while entrada != "salir":
        print(entrada)
        entrada = input("Dime otra cosa: ")
    

def main():
    entrada = input("Dime algo: ")
    eco(entrada)


if __name__ == "__main__":
    main()    