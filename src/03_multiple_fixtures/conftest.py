# conftest.py is a file that pytest will automatically import fixtures from

import pytest
import random

# A simple figure that generates a random number
@pytest.fixture
def random_number():
    return random.randint(0, 10)


# A simple fixture that generates some inputs
# This fixture uses another fixture which generates a random number
@pytest.fixture
def expensive_input(random_number):
    return [i for i in range(random_number)]
