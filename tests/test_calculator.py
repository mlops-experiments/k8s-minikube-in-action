# write unit tests for calculator functions
import pytest
from src.calculator import add, subtract, multiply, divide, power
from src.calculator import square, cube, fifth_power

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(2.5, 3.5) == 6.0
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(2.5, 1.5) == 1.0
    assert subtract(3, 5) == -2
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 5) == 0
    assert multiply(2.5, 4) == 10.0
def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(-6, 3) == -2
    with pytest.raises(ValueError):
        divide(1, 0)
def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(0, 5) == 0
    assert power(2, -1) == 0.5
    assert power(3, 2) == 9
    assert power(2, 10) == 1024
    assert power(1, 1000) == 1  


# Testing the square function
def test_square():
    assert square(2) == 4, "Test Failed: Square of 2 should be 4"
    assert square(3) == 9, "Test Failed: Square of 3 should be 9"

# Testing the cube function
def test_cube():
    assert cube(2) == 8, "Test Failed: Cube of 2 should be 8"
    assert cube(3) == 27, "Test Failed: Cube of 3 should be 27"

# Testing the fifth power function
def test_fifth_power():
    assert fifth_power(2) == 32, "Test Failed: Fifth power of 2 should be 32"
    assert fifth_power(3) == 243, "Test Failed: Fifth power of 3 should be 243"

# Test for invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")