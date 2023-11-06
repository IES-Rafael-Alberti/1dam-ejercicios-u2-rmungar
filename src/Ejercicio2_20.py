def buscar(frase, letra):
    i = 0
    while i != len(frase):
        if letra != frase[i]:
            print(f"Sin coincidencias en la posición: {i}")
            i += 1
        else:
            print(f"Coincidencia en la posición: {i}")
            break




def main():
    frase = input("Dame una frase: ")
    letra = input("Dime que letra debo buscar: ")
    print(buscar(frase, letra))

if __name__ == "__main__":
    main() 