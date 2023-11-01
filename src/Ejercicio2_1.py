def repeticion(palabra):
    cadena= str(palabra + " ")  *10
    return cadena

def main():
    palabra = input("Dime una palabra: ")
    print(repeticion(palabra))


if __name__ == "__main__":
    main()    
    