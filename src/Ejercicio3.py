

def division(num1, num2):
    if num2 == 0:
        return "ERROR"
    else:
        return num1/num2
    
def main(num1, num2):
    num1 = float(input("Dame un número: "))
    num2 = float(input("Dame otro número: "))
    if num2 != 0:
        print (num1/num2)
    else:
        print ("ERROR")

if __name__ == "__main__":
    main()