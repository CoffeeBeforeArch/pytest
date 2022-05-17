# A simple tests with parametrized input
# By Nick from CoffeeBeforeArch

import pytest

# Simple function that squares a number
def square(num):
    return num * num

# Our test parametrized test
@pytest.mark.parametrize("num", [1, 2, 3, 4 ,5])
def test_parametrize(num):
    result = square(num)
    assert result == num ** 2
