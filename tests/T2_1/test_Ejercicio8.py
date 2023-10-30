import pytest
from src.P2_1.Ejercicio8 import rendimiento

@pytest.mark.parametrize(
"puntuacion, expected",
    [
      (0.0, "Su nivel de rendimiento es Inaceptable, no recibirás dinero."),
      (2.1, "Su nivel de rendimiento es Meritorio, recibirás: 5040.0€"),
      (0.4, "Su nivel de rendimiento es Aceptable, recibirás: 960.0€"),
      (0.3, "Ingrese una puntuación válida"),
      (0.6, "Su nivel de rendimiento es Meritorio, recibirás: 1440.0€")
    ])
def test_imposicion_params(puntuacion, expected):
    assert rendimiento(puntuacion) == expected