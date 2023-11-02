def veces(palabra, letra):
    contador = 0
    for i in palabra:
        if i == letra.lower() or i == letra.upper():
            contador += 1
    print(f"La letra {letra} aparece {contador} veces en {palabra}")
    
def main():
    palabra = input("Dime una palabra: ")
    letra = input("Dime una letra: ")
    print(veces(palabra,letra))

if __name__ == "__main__":
    main()    