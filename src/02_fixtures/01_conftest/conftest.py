# A simple conftest file for pytest
# By Nick from CoffeeBeforeArch

import pytest

# A simple fixture that generates an input
@pytest.fixture
def initial_value():
    return 5
