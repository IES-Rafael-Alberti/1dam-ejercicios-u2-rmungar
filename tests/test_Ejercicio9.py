import pytest
from src.P2_1.Ejercicio9 import calcular_precio_entrada

@pytest.mark.parametrize(
    "edad, expected",
    [
        (1, "La entrada es gratis"),
        (18, "La entrada cuesta 5€"),
        (100, "La entrada cuesta 10€"),
        (5, "La entrada cuesta 5€"),
        (17, "La entrada cuesta 5€"),
        (125, "La entrada cuesta 10€")
])
def test_entrada_params(edad, expected):
    assert calcular_precio_entrada(edad) == expected