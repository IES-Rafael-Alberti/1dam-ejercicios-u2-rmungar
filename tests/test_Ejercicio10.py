import pytest
from src.Ejercicio10 import tipo_pizza

@pytest.mark.parametrize(
    "tipo, expected",
    [
        ("vegetariana", "Ingredientes vegetarianos: Pimiento y Tofu."),
        ("no vegetariana", "Ingredientes no vegetarianos: Peperoni, Jamón y Salmón."),
        ("vegetariana", "Ingredientes vegetarianos: Pimiento y Tofu."),
        ("no vegetariana", "Ingredientes no vegetarianos: Peperoni, Jamón y Salmón."),
        ("vegetariana", "Ingredientes vegetarianos: Pimiento y Tofu."),
        ("ATUN", "Tipo inválido")
])
def test_tipo_pizza_params(tipo, expected):
    assert tipo_pizza(tipo) == expected





from src.Ejercicio10 import pizza_final

@pytest.mark.parametrize(
    "ingrediente, tipo, expected",
    [
        ( "tofu", "vegetariana", "Su pizza es vegetariana y lleva: Tomate, Mozzarella y Tofu"),
        ( "pimiento", "no vegetariana", "Ingrediente no válido"),
        ( "Pimiento", "vegetariana", "Su pizza es vegetariana y lleva: Tomate, Mozzarella y Pimiento"),
        ( "Jamon", "no vegetariana", "Su pizza es no vegetariana y lleva: Tomate, Mozzarella y Jamon"),
        ( "pimiento", "vegetariana", "Su pizza es vegetariana y lleva: Tomate, Mozzarella y Pimiento"),
        ( "PIÑA", "ATUN", "Tipo inválido")
])
def test_pizza_final_params(tipo, ingrediente, expected):
    assert pizza_final(tipo, ingrediente) == expected