def piramide(num):
    cont = 1
    while cont <= num:
        print("* " * cont)
        cont += 1
        

def main():
    num = int(input("Dame un número: "))
    print(piramide(num))


if __name__ == "__main__":
    main()    