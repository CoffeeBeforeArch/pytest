# conftest.py is a file that pytest will automatically import fixtures from

import pytest

# A simple fixture that generates some inputs
# The cached result can be re-used by tests in the same module
@pytest.fixture(scope="module")
def expensive_input():
    return [i for i in range(10)]
