# A simple example of test fixtures
# By Nick from CoffeeBeforeArch

import pytest

# A simple fixture that generates some inputs
@pytest.fixture
def initial_value():
    return 5


# Simple function that squares a number
def square(num):
    return num * num


# One test that uses our fixture
def test_square(initial_value):
    result = square(initial_value)
    assert result == initial_value ** 2
