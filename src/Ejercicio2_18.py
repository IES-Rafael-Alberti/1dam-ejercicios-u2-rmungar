def total_pares(num):
    pares = 0
    while num != -1:
        if num%2 == 0:
            pares += 1
        total = 0
        while num != 0:
            d1 = num%10
            total += d1
            num = num//10
        print (f"La suma de los dígitos es: {total}")
        num = int(input("Dame un número (-1 finaliza el programa): "))
    return f"Se ingresaron {pares} números pares"

def main():
    num = int(input("Dame un número (-1 finaliza el programa): "))
    print(total_pares(num))



if __name__ == "__main__":
    main()    