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
# We have an implicitly indirect parameter!
@pytest.mark.parametrize("num_elements", [1, 2, 3, 4, 5])
def test_sum(element_list):
    result = sum_elements(element_list)
    assert result == sum(element_list)
