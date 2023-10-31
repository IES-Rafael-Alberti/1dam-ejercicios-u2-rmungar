import pytest
from src.Ejercicio3 import division

@pytest.mark.parametrize(
"num1, num2, expected",
    [
      (1, 0, "ERROR"),
      (18, 2, 9),
      (100, 4, 25),
      (9, 3,3),
      (40, 0, "ERROR")
    ])
def test_division_params(num1, num2, expected):
    assert division(num1, num2) == expected
