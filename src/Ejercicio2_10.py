def primo(num):
    for n in (2,num):
        if num%n == 0:
            return "No es primo"
        else:
            return "Es primo"

def main():
    num = int(input("Dime un número: "))
    print(primo(num))


if __name__ == "__main__":
    main()    