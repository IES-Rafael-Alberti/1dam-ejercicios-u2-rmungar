import pytest
from src.Ejercicio7 import imposicion

@pytest.mark.parametrize(
"renta, expected",
    [
      (10001, "El impuesto es de un 15%"),
      (20001, "El impuesto es de un 20%"),
      (65001, "El impuesto es de un 45%"),
      (1239, "El impuesto es de un 5%"),
      (36516, "El impuesto es de un 30%")
    ])
def test_imposicion_params(renta, expected):
    assert imposicion(renta) == expected