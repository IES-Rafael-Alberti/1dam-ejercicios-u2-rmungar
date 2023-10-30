def apto(edad,ingreso):
    
    if edad>=16 and ingreso >= 1000:
        return "Tiene que tributar"
    else:
        return "No tiene que tributar"
    
def main():
    edad = int(input("Digame su edad: "))
    ingreso = float(input("Digame sus ingresos mensuales: "))
    print (apto(edad,ingreso))

if __name__ == "__main__":
    main()