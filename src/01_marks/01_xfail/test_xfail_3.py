# A simple example xfail tests in pytest
# By Nick from CoffeeBeforeArch

import pytest
import sys

# Simple function that squares a number (with a bug!)
def square(num):
    return num + num


# A single test marked with xfail (we expect the test to fail)
@pytest.mark.xfail(
    sys.version_info > (3, 6), reason="Test requires Python version <= 3.6!"
)
def test_square():
    num = 5
    result = square(num)
    assert result == num ** 2
