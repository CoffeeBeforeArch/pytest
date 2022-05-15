# A simple example using the skip marker in pytest
# By Nick from CoffeeBeforeArch

import pytest
import sys

# Simple function that squares a number
def square(num):
    return num * num


# A single test marked with skip
@pytest.mark.skipif(sys.version_info > (3, 6), reason='Test requires Python version <= 3.6!')
def test_square():
    num = 5
    result = square(num)
    assert result == num ** 2
