# A simple example of skip tests in pytest
# By Nick from CoffeeBeforeArch

import pytest

# Simple function that squares a number
def square(num):
    return num * num


# A single test marked with skip (this test will not run!)
@pytest.mark.skip
def test_square(expensive_input):
    for num in expensive_input:
        result = square(num)
        assert result == num ** 31289421239

