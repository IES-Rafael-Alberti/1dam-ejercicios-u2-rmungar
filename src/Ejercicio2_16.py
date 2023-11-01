def num_mayor(entrada):
    mayor = 0
    while entrada != 0:
       entrada = int(input("Dime otro número: "))
       if entrada > mayor:
            mayor = entrada
            
    return f"{mayor} es el numero más grande"
    

def main():
    entrada = int(input("Dime un numero: "))
    print(num_mayor(entrada))


if __name__ == "__main__":
    main()    