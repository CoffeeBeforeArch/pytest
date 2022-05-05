# A simple example of test fixtures
# By Nick from CoffeeBeforeArch

import pytest

# Simple function that squares a number
def square(num):
    return num * num


# One test that uses our fixture
# The 'num_elements' parameter is automatically forwarded to our fixture
@pytest.mark.parametrize("num_elements", [1, 2, 7, 10])
def test_square(expensive_input, num_elements):
    for num in expensive_input:
        result = square(num)
        assert result == num ** 2
