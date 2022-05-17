# A simple example of test fixtures
# By Nick from CoffeeBeforeArch

import pytest

# A simple fixture that generates some inputs
@pytest.fixture
def num():
    return 5

# Simple function that squares a number
def square(num):
    return num * num

# One test that uses our fixture
def test_square(num):
    result = square(num)
    assert result == num ** 2
