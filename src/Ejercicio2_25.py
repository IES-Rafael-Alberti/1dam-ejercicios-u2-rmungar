def longitud(frase):
    mayor = 0
    cantidad = 0
    while len(frase) != 0:
        cantidad += 1
        espacio = frase.find(" ")
        if espacio != -1:
            palabra = frase[0:espacio]
            while espacio < len(frase) and frase[espacio] == " ":
                espacio += 1
            frase = frase[espacio:]
        else:
            palabra = frase
            frase = ""
        if len(palabra) > mayor:
            mayor = len(palabra)
            palabra_mayor = palabra
    if cantidad > 0:
        print(f"La palabra más larga es: {palabra_mayor}")
    return f"Número de palabras: {cantidad}"






def main():
    frase=input("Ingrese una frase: ").strip(" ")
    print(longitud(frase))


if __name__ == "__main__":
    main()