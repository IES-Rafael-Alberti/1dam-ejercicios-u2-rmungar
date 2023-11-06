def programa(opcion):
    while opcion != 3:
        if opcion==1:
            print("INICIO")
            opcion=int(input("Ingrese una opción: "))
        elif opcion==2:
            print("Spiderman 2 GOTY")
            opcion=int(input("Ingrese una opción: "))
        else:
            return("Opción no válida.")
    return ("FIN")


def main():
    print(" 1 - Comenzar Programa")
    print(" 2 - imprimir texto")
    print(" 3 - finalizar programa")
    opcion=int(input("Ingrese una opción: "))

    print(programa(opcion))
    

if __name__ == "__main__":
    main()    