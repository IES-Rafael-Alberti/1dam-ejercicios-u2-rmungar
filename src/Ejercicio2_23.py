def libros(cadena):
    numeros= "0123456789"
    lineas=0
    num_num = 0
    while cadena != "*":
        for caracter in cadena:
            if caracter in numeros:
                num_num += 1
        if cadena == "/":
            lineas += 1
            print(f"Hay {num_num} números en la línea.")
            num_num = 0
        cadena = input("Escriba una cadena: ")
    return f"Se ingresaron {lineas} líneas"




def main():
    cadena = input("Escriba una cadena: ")
    print(libros(cadena))



if __name__ == "__main__":
    main()