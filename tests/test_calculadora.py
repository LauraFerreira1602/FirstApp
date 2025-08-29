import pytest
from utils.calculadora import soma,subtracao


def test_soma():
    # Arrange
    x = 2
    y = 3
    
    # Act
    resultado = soma(x,y)
    
    # Assert
    assert resultado == 5


def test_subtracao():
    # Arrange
    x = 2
    y = 3

    # Act
    resultado = subtracao(x, y)

    # Assert
    assert resultado == -1