# A simple exaple of tests grouped into a class
# By Nick from CoffeeBeforeArch

# Simple function that squares a number
def square(num):
    return num * num


# Simple function that cubes another
def cube(num):
    return square(num) * num


# Our class containing our tests as methods
# Note: Must start with `Test`
class TestClass:
    # Share our common number between test instances
    num = 5

    # Test squaring of a number
    def test_square(self):
        result = square(self.num)
        assert result == self.num ** 2

    # Test cubing of a number
    def test_cube(self):
        result = cube(self.num)
        assert result == self.num ** 3
