# A test where the collection of tests is modified
# By Nick from CoffeeBeforeArch

import pytest

# Simple function that squares a number
def square(num):
    return num * num


# One test that uses our fixture
@pytest.mark.parametrize("num", range(10))
def test_square(num):
    result = square(num)
    assert result == num ** 2
