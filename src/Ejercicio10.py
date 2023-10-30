def tipo_pizza(tipo):
    tipo = tipo.lower()
    if tipo == "vegetariana":
        return "Ingredientes vegetarianos: Pimiento y Tofu."
    elif tipo == "no vegetariana":
        return "Ingredientes no vegetarianos: Peperoni, Jamón y Salmón."
    else:
        return "Tipo inválido"
    

def pizza_final(ingrediente, tipo):
    listaveg = ["Pimiento", "Tofu"]
    listanoveg = ["Peperoni", "Salmon", "Jamon"]
    if tipo == "vegetariana":
        if ingrediente.capitalize() in listaveg:
            return f"Su pizza es {tipo} y lleva: Tomate, Mozzarella y {ingrediente.capitalize()}"
        else:
            return "Ingrediente no válido"
    else:
        if ingrediente.capitalize() in listanoveg:
            return f"Su pizza es {tipo} y lleva: Tomate, Mozzarella y {ingrediente.capitalize()}"
        else:
            return "Ingrediente no válido"

def main():
    tipo = input("¿Que tipo de pizza quieres? ")
    print(tipo_pizza(tipo))
    ingrediente = input("Eliga un ingrediente de los anteriores: ")
    print(pizza_final(ingrediente, tipo))

if __name__ == "__main__":
    main()