# A simple example of test fixtures
# By Nick from CoffeeBeforeArch

import math
import pytest

# A simple fixture that generates an input
@pytest.fixture
def base():
    return 5


# A simple fixture that generates an input
@pytest.fixture
def exponent():
    return 10


# Simple function that squares a number
def pow(base, exponent):
    return num * num


# A test using two fixtures
def test_pow(base, exponent):
    result = pow(base, exponent)
    assert result1 == math.pow(base, exponent)
