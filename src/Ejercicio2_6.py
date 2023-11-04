def piramide(num):
    cont = 0
    while cont < num:
        cont += 1
        print ("* "*cont)
    
        
        

def main():
    num = int(input("Dame un número: "))
    print(piramide(num))


if __name__ == "__main__":
    main()    