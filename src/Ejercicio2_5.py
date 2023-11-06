def capital(cantidad, interes, num):
    for inicio in range(1, num):
        cantidad *= (1 + (interes/100)) 
        print (cantidad)

       
        


def main():
    cantidad = int(input("Digame la cantidad de dinero: "))
    interes = int(input("Digame el interés: "))
    num = int(input("Digame el número de años: "))
    capital(cantidad, interes, num)


if __name__ == "__main__":
    main()    