# A simple example xfail tests in pytest
# By Nick from CoffeeBeforeArch

import pytest

# Simple function that squares a number
def square(num):
    return num * num


# A single test marked with xfail (we expect the test to fail)
@pytest.mark.xfail
def test_square(expensive_input):
    for num in expensive_input:
        result = square(num)
        assert result == num ** 3

