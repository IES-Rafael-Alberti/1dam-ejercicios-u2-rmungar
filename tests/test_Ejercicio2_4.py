import pytest
from src.Ejercicio2_4 import disminuye

@pytest.mark.parametrize(
    "num, expected",
    [
        (8, "8, 7, 6, 5, 4, 3, 2, 1, 0"),
        (18, "18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0"),
        (9, "9, 8, 7, 6, 5, 4, 3, 2, 1, 0")
    ])
def test_disminuye_params(num, expected):
    assert disminuye(num) == expected