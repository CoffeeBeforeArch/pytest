# A simple example of test fixtures
# By Nick from CoffeeBeforeArch

# Simple function that squares a number
def square(num):
    return num * num


# One test that uses our fixture
def test_square(expensive_input):
    for num in expensive_input:
        result = square(num)
        assert result == num ** 2
    print("Printing from test body!")
