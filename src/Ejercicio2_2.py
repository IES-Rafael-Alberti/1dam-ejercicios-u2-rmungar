def años(edad):
    cont = 0
    cadena = "0 "
    while cont < edad:
        cont +=1
        cadena += str(cont) + " "
    return cadena

def main():
    edad = int(input("Dime tu edad: "))
    print(años(edad))


if __name__ == "__main__":
    main()    