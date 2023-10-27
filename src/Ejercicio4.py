num=int(input("Dime un número entero: "))
def tipo(num):
    resto = num%2
    if resto == 1:
        return "IMPAR"
    else:
        return "PAR"
    

def main(num):
    resto = num%2
    if resto ==1 :
        print ("IMPAR")
    else:
        print ("PAR")

if __name__ == "__main__":
    main(num)
