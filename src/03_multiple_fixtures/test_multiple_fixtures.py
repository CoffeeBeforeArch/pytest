# A simple using nested fixtures
# By Nick from CoffeeBeforeArch

import logging

# Simple function that squares a number
def square(num):
    return num * num


# One test that uses our fixture
def test_square(expensive_input):
    for num in expensive_input:
        result = square(num)
        assert result == num ** 2
