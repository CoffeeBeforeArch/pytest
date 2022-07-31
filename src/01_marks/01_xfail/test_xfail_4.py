# A simple example xfail tests in pytest
# By Nick from CoffeeBeforeArch

import pytest

# Simple function that squares a number (with a bug!)
def square(num):
    return num + num


# A single test marked with xfail (we expect the test to fail)
@pytest.mark.xfail(strict=True)
def test_square():
    num = 5
    result = square(num)
    assert result == num ** 2
