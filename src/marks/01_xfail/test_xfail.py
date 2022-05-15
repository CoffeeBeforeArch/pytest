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


# A parametrized test with one variant marked with xfail
@pytest.mark.parametrize(
    "num",
    [
        pytest.param(1),
        pytest.param(
            5, marks=pytest.mark.xfail(reason="This values causes an assert!")
        ),
    ],
)
def test_multiple_square(num):
    assert num != 5
    result = square(num)
    assert result == num ** 3
