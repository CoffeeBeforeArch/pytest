# A test where the collection of tests is modified
# By Nick from CoffeeBeforeArch

import pytest

# Simple function that squares a number
def square(num):
    return num * num


# One test that uses our fixture
@pytest.mark.parametrize("initial_value", range(10))
def test_square(initial_value):
    result = square(initial_value)
    assert result == initial_value ** 2
