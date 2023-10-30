import pytest
from src.P2_1.Ejercicio5 import apto

@pytest.mark.parametrize(
"edad, ingreso, expected",
    [
      (1, 1000, "No tiene que tributar"),
      (18, 2200, "Tiene que tributar"),
      (100, 5000, "Tiene que tributar"),
      (9, 0, "No tiene que tributar"),
      (40, 324234, "Tiene que tributar")
    ])
def test_apto_params(edad, ingreso, expected):
    assert apto(edad, ingreso) == expected