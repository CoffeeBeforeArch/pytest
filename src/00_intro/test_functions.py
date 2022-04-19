# A simple exaple of tests using pytest
# By Nick from CoffeeBeforeArch

# Simple function that squares a number
def square(num):
    return num * num


# Simple function that cubes another
def cube(num):
    return square(num) * num


# Tests start with "test_"
def test_square():
    num = 5
    result = square(num)
    assert result == num ** 2


# Define another test in the same file
def test_cube():
    num = 5
    result = cube(num)
    assert result == num ** 3
