import pytest
from src.Ejercicio2_2 import años

@pytest.mark.parametrize(
    "edad, expected",
    [
        (1, "0 1 "),
        (18, "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 "),
        (9, "0 1 2 3 4 5 6 7 8 9 ")
    ])
def test_años_params(edad, expected):
    assert años(edad) == expected