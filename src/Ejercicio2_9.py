def contraseña(contraseña_introducida):
    contraseña_guardada = "rmungar1209"
    while contraseña_introducida.lower() != contraseña_guardada:
        contraseña_introducida = input("Vuelva a introducir la contraseña: ")
    return "Contraseña Correcta"
        

def main():
    contraseña_introducida = input("Ingrese la contraseña: ")
    print(contraseña(contraseña_introducida))


if __name__ == "__main__":
    main()    