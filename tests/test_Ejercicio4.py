import pytest
from src.Ejercicio4 import tipo

@pytest.mark.parametrize(
    "num, expected",
    [
        (1, "IMPAR"),
        (18, "PAR"),
        (100, "PAR"),
        (5, "IMPAR"),
        (17, "IMPAR"),
        (125, "IMPAR")
])
def test_tipo_params(num, expected):
    assert tipo(num) == expected