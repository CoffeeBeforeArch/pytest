# A simple example of test fixtures
# By Nick from CoffeeBeforeArch

import pytest


# Simple function that computes the sum of list elements
def sum_elements(elements):
    total = 0
    for e in elements:
        total += e
    return total

# One test that uses our fixture
# The 'num_elements' parameter is automatically forwarded to our fixture
@pytest.mark.parametrize("element_list", [1, 2, 3, 4, 5], indirect=True)
def test_square(element_list):
    result = sum_elements(element_list)
    assert result == sum(element_list)
