# A simple example using conftest with test fixtures
# By Nick from CoffeeBeforeArch

# Simple function that squares a number
def square(num):
    return num * num


# One test that uses our fixture
def test_square(num):
    result = square(num)
    assert result == num ** 2
