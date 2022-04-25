# conftest.py is a file that pytest will automatically import fixtures from

import pytest
import random

# A simple figure that generates a random number
@pytest.fixture
def random_number():
    return random.randint(0, 10)

