
def Grupo(nombre, sexo):
    nombre = nombre.upper()
    sexo = sexo.upper()
    if (sexo == "MUJER" and nombre < "M") or (sexo == "HOMBRE" and nombre > "N"):
        return "Perteneces al grupo A"
    else:
        return "Perteneces al grupo B"

def main():
    nombre = input("Ingrese su nombre: ")
    sexo = input("Ingrese su sexo: ")
    print(Grupo(nombre,sexo))

if __name__ == "__main__":
    main()
