# conftest.py is a file that pytest will automatically import fixtures from

import pytest

# A simple fixture that generates some inputs
@pytest.fixture
def expensive_input():
    return [i for i in range(10)]


@pytest.fixture(autouse=True)
def setup_teardown():
    print("Setup!")
    yield
    print("Teardown!")
