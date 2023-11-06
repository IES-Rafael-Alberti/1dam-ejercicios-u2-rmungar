def numeros(entrada):
    total= 0
    while entrada != "0":
        total = int(total) + int(entrada)
        entrada = input("Dime otro número: ")
    return total
    

def main():
    entrada = int(input("Dime un numero: "))
    print(numeros(entrada))


if __name__ == "__main__":
    main()    