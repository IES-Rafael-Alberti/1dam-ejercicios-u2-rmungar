def tipos_num(num):
  totalPares = 0
  totalImpares = 0
  while num != 0:
    pares = 0
    impares = 0
    while num != 0:
        ultdig = num%10
        if ultdig%2 == 0:
            pares += 1
            totalPares += 1
        else:
           impares += 1
           totalImpares += 1
        num = num//10

    if pares == 1 and impares == 1:
       print(f"El número tiene {pares} número par y {impares} número impar")
    elif pares == 1 and impares != 1:
       print(f"El número tiene {pares} número par y {impares} números impares")
    elif pares != 1 and impares == 1:
       print(f"El número tiene {pares} números pares y {impares} número impar")
    else:
       print(f"El número tiene {pares} números pares y {impares} números impares")

    num = int(input("Dame otro número: "))
    return f"Total de números pares: {totalPares} y Total de números impares: {totalImpares}"




def main():
   num = int(input("Dame un número: "))
   print(tipos_num(num))

if __name__ == "__main__":
    main()