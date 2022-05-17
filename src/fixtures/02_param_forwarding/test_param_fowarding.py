# A simple example of test fixtures
# By Nick from CoffeeBeforeArch

import pytest

@pytest.fixture(autouse=True)
def log_num(num):
    print(f"The value of num is {num}")

# Simple function that squares a number
def square(num):
    return num * num

# One test that uses our fixture
# The 'num_elements' parameter is automatically forwarded to our fixture
@pytest.mark.parametrize("num1", [1, 2, 3, 4, 5])
def test_square(num1):
    result = square(num1)
    assert result == num1 ** 2
