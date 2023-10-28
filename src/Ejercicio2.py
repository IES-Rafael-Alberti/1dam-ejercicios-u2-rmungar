contraseña_guardada = "rmungar1209" 
def contraseña(contraseña_introducida):
    
    if contraseña_introducida == contraseña:
        return "Contraseña correcta"
    else:
        return "Contraseña incorrecta" 
 
def main():
    contraseña_introducida = input("Escriba la contraseña: ")
    contraseña_introducida = contraseña_introducida.lower()
    if contraseña_guardada == contraseña_introducida :
        print("Contraseña correcta.")
    else:
        print("Contraseña incorrecta.")


if __name__ == "__main__":
    main()    
    

