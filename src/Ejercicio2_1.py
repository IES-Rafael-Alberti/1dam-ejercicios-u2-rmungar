def repeticion(palabra):
    return str(palabra + " ")  *10 

def main():
    palabra = input("Dime una palabra: ")
    print(repeticion(palabra))


if __name__ == "__main__":
    main()    
    