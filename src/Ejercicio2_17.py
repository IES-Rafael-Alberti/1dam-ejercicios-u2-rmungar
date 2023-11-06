def sumaDig(num):
    total = 0
    while num != 0:
        d1 = num%10
        total += d1
        num = num//10
    return f"La suma de los dígitos es: {total}"

def main():
    num = int(input("Dame un número: "))
    print(sumaDig(num))


if __name__ == "__main__":
    main()    