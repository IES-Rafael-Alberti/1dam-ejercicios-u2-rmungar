import pytest
from src.P2_1.Ejercicio6 import Grupo

@pytest.mark.parametrize(
"nombre, sexo, expected",
    [
      ("Nicolás", "hombre", "Perteneces al grupo A"),
      ("Lara", "mujer", "Perteneces al grupo A"),
      ("Paco", "MUJER", "Perteneces al grupo B"),
      ("César", "hombre", "Perteneces al grupo B"),
      ("Raúl", "HOMBRE", "Perteneces al grupo A")
    ])
def test_grupo_params(nombre, sexo, expected):
    assert Grupo(nombre, sexo) == expected