# A simple example of test fixtures
# By Nick from CoffeeBeforeArch

import pytest

# A simple fixture that generates some inputs
@pytest.fixture(scope="module")
def initial_value():
    print("Generating an initial value!")
    return 5


# Simple function that squares a number
def square(num):
    return num * num


# Simple function that squares a number
def cube(num):
    return square(num) * num


# One test that uses our fixture
def test_square(initial_value):
    result = square(initial_value)
    assert result == initial_value ** 2


# One test that uses our fixture
def test_cube(initial_value):
    result = cube(initial_value)
    assert result == initial_value ** 3
