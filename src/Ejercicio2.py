contraseña_guardada ="rmungar1209" 
contraseña_introducida = str(input("Escriba la contraseña: "))
def contraseña(contraseña_introducida):
    if contraseña_introducida == contraseña_guardada:
        return "Contraseña correcta"
    else:
        return "Contraseña incorrecta" 
def main():
    contraseña_introducida = contraseña()
    
    if contraseña(contraseña_introducida) == contraseña_guardada :
        print("Contraseña correcta.")
    else:
        print("Contraseña incorrecta.")


if __name__ == "__main__":
    main()    
    

