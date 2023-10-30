def calcular_precio_entrada(edad):
    if edad < 4:
        return "La entrada es gratis"  
    elif 4 <= edad <= 18:
        return "La entrada cuesta 5€"  
    else:
        return "La entrada cuesta 10€" 


def main():
    edad = int(input("Por favor, ingrese la edad: "))
    print(calcular_precio_entrada(edad))
        

if __name__ == "__main__":
    main()