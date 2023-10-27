num1 = float(input("Dame un número: "))
num2 = float(input("Dame otro número: "))

def division():
    if num2 == 0:
        return "ERROR"
    else:
        return num1/num2
    
def main():
    if num2 == 0 :
        print("ERROR")
    else:
        print(num1/num2)


if __name__ == "__main__":
    main()    