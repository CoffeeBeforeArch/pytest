# A simple using pytest cache
# By Nick from CoffeeBeforeArch

# Simple function that squares a number
def square(num):
    return num * num


# One test that uses our fixture
def test_square(inputs):
    for num in inputs:
        result = square(num)
        assert result == num ** 2
