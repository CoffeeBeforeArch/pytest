# conftest.py is a file that pytest will automatically import fixtures from

import pytest

# A simple fixture that generates some inputs
@pytest.fixture
def expensive_input():
    print("Before Test!")
    yield [i for i in range(10)]
    print("After Test!")
