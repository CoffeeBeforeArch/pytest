# A simple example using the skip marker in pytest
# By Nick from CoffeeBeforeArch

import pytest

# Simple function that squares a number
def square(num):
    return num * num


# A single test marked with skip
def test_square():
    pytest.skip()
    num = 5
    result = square(num)
    assert result == num ** 2
