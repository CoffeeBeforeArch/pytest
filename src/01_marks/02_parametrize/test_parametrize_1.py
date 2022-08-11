# A simple tests with parametrized input
# By Nick from CoffeeBeforeArch

import pytest

# Simple function that squares a number
def square(num):
    return num * num


# Our test parametrized test
@pytest.mark.parametrize("num,ref", [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)])
def test_square(num, ref):
    result = square(num)
    assert result == ref
