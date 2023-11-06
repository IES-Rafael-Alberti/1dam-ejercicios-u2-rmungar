def tablas():
    cont = 1
    while cont <=10:
        num = 0
        while num <=10:
            print (f"{num} * {cont} = {num*cont}")
            num +=1
        cont += 1

def main():
    tablas()



if __name__ == "__main__":
    main()    