def capital(cantidad, interes, num):
    cont = 0
    while cont < num:
        cont + 1
        cantidad = cantidad * (1 + (interes/100))
        return cantidad


def main():
    cantidad = int(input("Digame la cantidad de dinero: "))
    interes = int(input("Digame el interés: "))
    num = int(input("Digame el número de años: "))
    print(capital(cantidad, interes, num))


if __name__ == "__main__":
    main()    