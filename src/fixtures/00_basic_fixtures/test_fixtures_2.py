# A simple example of test fixtures
# By Nick from CoffeeBeforeArch

import pytest

# A simple fixture that generates an input
@pytest.fixture
def num1():
    return 5

# A simple fixture that generates an input
@pytest.fixture
def num2():
    return 10

# Simple function that squares a number
def square(num):
    return num * num

# A test using two fixtures
def test_square(num1, num2):
    result1 = square(num1)
    assert result1 == num ** 2

    result2 = square(num2)
    assert result2 == num ** 2
