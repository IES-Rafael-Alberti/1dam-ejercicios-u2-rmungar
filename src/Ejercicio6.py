
def Grupo(nombre, sexo):
    nombre2 = nombre.upper()
    sexo2 = sexo.upper()
    if (sexo2 == "MUJER" and nombre2 < "M") or (sexo2 == "HOMBRE" and nombre2 > "N"):
        return "A"
    else:
        return "B"

def main():
    nombre = input("Ingrese su nombre: ")
    sexo = input("Ingrese su sexo: ")
    
    grupo = Grupo(nombre, sexo)
    
    print(f"Usted pertenece al grupo {grupo}")

if __name__ == "__main__":
    main()
