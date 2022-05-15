# A simple tests with parametrized input
# By Nick from CoffeeBeforeArch

import pytest

# Simple function that squares a number
def square(num):
    return num * num


# Our test parametrized with the input 'num'
@pytest.mark.parametrize("num", range(3))
def test_parametrize(num):
    result = square(num)
    assert result == num ** 2


# Another test with multiple parametrizations
# This creates a cartesian product of the parameters
@pytest.mark.parametrize("num1", range(3))
@pytest.mark.parametrize("num2", range(3))
def test_two_parametrize(num1, num2):
    result1 = square(num1)
    result2 = square(num2)
    assert result1 == num1 ** 2
    assert result2 == num2 ** 2


# A test that combines parameters into one parametrize
@pytest.mark.parametrize("num,result", [(i, i ** 2) for i in range(3)])
def test_combined_parametrize(num, result):
    assert square(num) == result
