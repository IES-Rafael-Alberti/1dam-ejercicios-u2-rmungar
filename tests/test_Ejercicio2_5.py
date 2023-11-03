import pytest
from src.Ejercicio2_6 import piramide

@pytest.mark.parametrize(
    "num, expected",
    [
        (3, "*"
            "* *" 
            "* * *"),
        (1, "18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0"),
        (2, "9, 8, 7, 6, 5, 4, 3, 2, 1, 0")
    ])
def test_piramide_params(num, expected):
    assert piramide(num) == expected