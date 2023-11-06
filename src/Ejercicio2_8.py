def triangulo(num):
    for i in range(1, num+1, 2):
        for a in range(i, 0, -2):
            print(a, end=" ")
        print("")


def main():
    num = int(input("Introduzca la altura del triángulo: "))
    triangulo(num)
 


if __name__ == "__main__":
    main()    