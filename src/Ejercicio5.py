def apto():
    edad = int(input("Digame su edad: "))
    ingreso = float(input("Digame sus ingresos mensuales: "))
    if edad>=16 and ingreso >= 1000:
        return True
    else:
        return False
    
def main():
    if apto() == True:
        print("Usted tiene que tributar")
    else:
        print ("Usted no tiene que tributar")

if __name__ == "__main__":
    main()