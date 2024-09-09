import pytest
import allure
from main import suma, resta, multiplicacion, division

pepe = 90

@allure.parent_suite(pepe)
@allure.suite("numeros positivos")
@allure.sub_suite("numeros del 1 al 10")
def test_suma():
    assert suma(1, 2) == 3
    assert suma(2, 3) == 5
    assert suma(0, 0) == 0

@allure.parent_suite("resta suite")
@allure.suite("numeros positivos")
@allure.sub_suite("numeros del 1 al 10")
def test_resta():
    assert resta(3, 2) == 1
    assert resta(-1, 1) == -2
    assert resta(0, 0) == 0

@allure.parent_suite("multiplicacion suite ")
@allure.suite("numeros positivos")
@allure.sub_suite("numeros del 1 al 10")
def test_multiplicacion():
    assert multiplicacion(2, 3) == 6
    assert multiplicacion(-1, 1) == -1
    assert multiplicacion(0, 5) == 0

@allure.parent_suite("Division suite")
@allure.suite("numeros positivos")
@allure.sub_suite("numeros del 1 al 10")
def test_division():
    assert division(6, 3) == 2
    assert division(-6, 2) == -3
    assert division(0, 1) == 0
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        division(1, 0)
