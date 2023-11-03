def numeros(num):
  
  cantP = 0
  while num != 0:
    Primos = True
    for n in range (2,num):
        if num%n == 0:
            Primos = False
            break
    if Primos == True:
            cantP += 1
    num = int(input("Dame otro número: "))
  return f"Hay {cantP} números primos."



def main():
   num = int(input("Dame un número: "))
   print(numeros(num))


if __name__ == "__main__":
    main()