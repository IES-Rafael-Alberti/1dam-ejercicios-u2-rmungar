contraseña_guardada="rmumngar1209"

def contraseña(contraseña_introducida=(input("Escriba la contraseña: "))):
    contraseña_introducida=contraseña_introducida.lower()
    if contraseña_introducida==contraseña_guardada:
        return "Contraseña correcta"
    else:
        return "Contraseña incorrecta"
    
    