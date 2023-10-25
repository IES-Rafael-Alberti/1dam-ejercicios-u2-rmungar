import pytest
from src.Ejercicio1 import MayorEdad

@pytest.mark.parametrize(
"edad, expected",
    [
      (1, "Eres menor de edad"),
      (18, "Eres mayor de edad"),
      (100, "Eres mayor de edad"),
      (9, "Eres menor de edad"),
      (40, "Eres mayor de edad")
    ])
def test_MayorEdad_params(edad, expected):
    assert MayorEdad(edad) == expected
