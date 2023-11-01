def disminuye(num):
    cadena = ""
    while num >= 0:
        if num != 0:
            cadena += str(num) + ", "
        else:
            cadena += str(num)
        num -=1
    return cadena

def main():
    num = int(input("Dame un número: "))
    print(disminuye(num))


if __name__ == "__main__":
    main()    