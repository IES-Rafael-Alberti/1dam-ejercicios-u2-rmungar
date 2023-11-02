def precio(monto):
    total = 0
    while monto != 0:
        if monto < 0:
            print("Monto inválido")
        else:
            total += monto
        monto = float(input("Monto de la venta: "))
    if total > 1000:
        total -= total*0.1
    return f"Monto total: {total}€"

def main():
    monto = float(input("Monto de la venta: "))
    print(precio(monto))

if __name__ == "__main__":
    main()
