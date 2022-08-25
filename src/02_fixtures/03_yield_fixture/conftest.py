# conftest.py is a file that pytest will automatically import fixtures from

import pytest

# A simple fixture that generates some inputs
@pytest.fixture
def initial_value():
    print("Providing a value to our test!")
    yield 5
    print("Finishing Up!")
