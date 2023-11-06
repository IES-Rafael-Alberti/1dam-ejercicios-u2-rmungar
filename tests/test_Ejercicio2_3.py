import pytest
from src.Ejercicio2_3 import impares

@pytest.mark.parametrize(
    "num, expected",
    [
        (1, "1"),
        (18, "1, 3, 5, 7, 9, 11, 13, 15, 17"),
        (6, "1, 3, 5")
    ])
def test_impares_params(num, expected):
    assert impares(num) == expected