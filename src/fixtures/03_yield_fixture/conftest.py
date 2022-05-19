# conftest.py is a file that pytest will automatically import fixtures from

import pytest

# A simple fixture that generates some inputs
@pytest.fixture
def num():
    print("Before Test!")
    yield 5
    print("After Test!")
