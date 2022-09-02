# A simple using pytest cache
# By Nick from CoffeeBeforeArch

# Simple function that squares a number
def square(num):
    return num * num


# One test that uses our fixture
def test_square(expensive_value):
    result = square(expensive_value)
    assert result == expensive_value ** 2
