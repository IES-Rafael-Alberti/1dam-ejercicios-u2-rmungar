def positivos(entrada):
    total= 0
    while entrada != 0:
       entrada = int(input("Dime otro número: "))
       if entrada > 0:
            total +=1
            
    return total
    

def main():
    entrada = int(input("Dime un numero: "))
    print(positivos(entrada))


if __name__ == "__main__":
    main()    