import pytest
from calc import add, subtract, multiply, divide

def test_add():
    assert add(1, 1 ) == 2
    assert add(-1, 5) == 4

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(10, 2) == 20

def test_divide():
    assert divide(10, 2) == 5

