
def MayorEdad(edad):
    if edad >= 18:
        return "Eres mayor de edad"
    else:
        return "Eres menor de edad"

def main():
    edad = int(input("Dime tu edad: "))

    if MayorEdad(edad):
        print("Eres mayor de edad.")
    else:
        print("No eres mayor de edad.")


if __name__ == "__main__":
    main()