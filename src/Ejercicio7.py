def imposicion(renta):
    if renta <= 10000 :
        return "El impuesto es de un 5%"
    elif 10000< renta <= 20000:
        return "El impuesto es de un 15%"
    elif 20000< renta <= 35000:
        return "El impuesto es de un 20%"
    elif 35000< renta <= 60000:
        return "El impuesto es de un 30%"
    else:
        return "El impuesto es de un 45%"
    
def main():
    renta = float(input("Digame su renta anual: "))
    print (imposicion(renta))

if __name__ == "__main__":
    main()