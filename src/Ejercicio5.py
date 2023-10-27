def apto(edad,ingreso):
    
    if edad>=16 and ingreso >= 1000:
        return True
    else:
        return False
    
def main():
    edad = int(input("Digame su edad: "))
    ingreso = float(input("Digame sus ingresos mensuales: "))
    if apto(edad, ingreso) == True:
        print("Usted tiene que tributar")
    else:
        print ("Usted no tiene que tributar")

if __name__ == "__main__":
    main()