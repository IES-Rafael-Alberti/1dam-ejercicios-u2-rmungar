def vuelta(palabra):
    for i in range (len(palabra)-1, -1, -1):
        print (palabra[i])


def main():
    palabra = input("Dime un palabra: ")
    vuelta(palabra)



if __name__ == "__main__":
    main()    