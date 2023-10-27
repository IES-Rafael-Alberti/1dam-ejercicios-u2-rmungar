def calcular_precio_entrada(edad):
    if edad < 4:
        return 0  
    elif 4 <= edad <= 18:
        return 5  
    else:
        return 10  

def main():

    edad = int(input("Por favor, ingrese la edad: "))
    if edad < 0:
        print("La edad no puede ser un número negativo.")
    else:
        precio = calcular_precio_entrada(edad)
        print(f"El precio de entrada es de: {precio}€")

if __name__ == "__main__":
    main()