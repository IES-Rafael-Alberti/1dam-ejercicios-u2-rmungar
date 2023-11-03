import pytest
from src.Ejercicio2_1 import repeticion

@pytest.mark.parametrize(
"palabra, expected",
    [
      ("mario", "mario mario mario mario mario mario mario mario mario mario "),
      ("tortilla", "tortilla tortilla tortilla tortilla tortilla tortilla tortilla tortilla tortilla tortilla "),
      ("gato", "gato gato gato gato gato gato gato gato gato gato ")
    ])
def test_repeticion_params(palabra, expected):
    assert repeticion(palabra) == expected