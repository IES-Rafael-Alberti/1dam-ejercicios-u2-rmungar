import pytest
from src.Ejercicio2 import contraseña

@pytest.mark.parametrize(
"contraseña_introducida, expected",
    [
      ("rmungar1209", "Contraseña correcta"),
      ("RMUNGAR1209", "Contraseña correcta"),
      ("contraseña", "Contraseña incorrecta"),
      ("aitortilla", "Contraseña incorrecta"),
      ("noaitortilla", "Contraseña incorrecta")
    ])
def test_contraseña_params(contraseña_introducida, expected):
    assert contraseña(contraseña_introducida)== expected
