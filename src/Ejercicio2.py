contraseña_guardada = "rmungar1209" 
def contraseña(contraseña_introducida):
    contraseña_introducida=contraseña_introducida.lower()
    if contraseña_introducida == contraseña_guardada:
        return "Contraseña correcta"
    else:
        return "Contraseña incorrecta" 
 
def main():
    contraseña_introducida = input("Escriba la contraseña: ")
    print(contraseña(contraseña_introducida))



if __name__ == "__main__":
    main()    
    

