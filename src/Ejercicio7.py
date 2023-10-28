def imposicion(renta):
    if renta <= 10000 :
        return "5%"
    elif 10000< renta <= 20000:
        return "15%"
    elif 20000< renta <= 35000:
        return "20%"
    elif 35000< renta <= 60000:
        return "30%"
    else:
        return "45%"
    
def main():
    renta = float(input("Digame su renta anual: "))
    impuesto = imposicion(renta)
    print (f"El impuesto será de un {impuesto}")

if __name__ == "__main__":
    main()