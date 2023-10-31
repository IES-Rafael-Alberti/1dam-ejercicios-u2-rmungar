def rendimiento(puntuacion):
    if puntuacion == 0.0:
        return "Su nivel de rendimiento es Inaceptable, no recibirás dinero."
    elif puntuacion == 0.4:
        return "Su nivel de rendimiento es Aceptable, recibirás: 960.0€"
    elif puntuacion >= 0.6:
        return f"Su nivel de rendimiento es Meritorio, recibirás: {2400*puntuacion}€"
    else:
        return "Ingrese una puntuación válida"
def main():
    puntuacion = float(input("Digame la puntuación del trabajador: "))
    print(rendimiento(puntuacion))
    
if __name__ == "__main__":
    main()