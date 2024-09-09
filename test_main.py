import pytest
from main import suma, resta, multiplicacion, division

def test_suma():
    assert suma(1, 2) == 3
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0

def test_resta():
    assert resta(3, 2) == 8
    assert resta(-1, 1) == -2
    assert resta(0, 0) == 0

def test_multiplicacion():
    assert multiplicacion(2, 3) == 6
    assert multiplicacion(-1, 1) == -1
    assert multiplicacion(0, 5) == 0

def test_division():
    assert division(6, 3) == 2
    assert division(-6, 2) == -3
    assert division(0, 1) == 0
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        division(1, 0)
