# A simple tests with parametrized input
# By Nick from CoffeeBeforeArch

import pytest

# Simple function that squares a number
def square(num):
    return num * num


# Our test parametrized test
@pytest.mark.parametrize("num1", [1, 2, 3])
@pytest.mark.parametrize("num2", [4, 5, 6])
def test_parametrize(num1, num2):
    # Test the first number
    result1 = square(num1)
    assert result1 == num1 ** 2

    # Test the second number
    result2 = square(num2)
    assert result2 == num2 ** 2
