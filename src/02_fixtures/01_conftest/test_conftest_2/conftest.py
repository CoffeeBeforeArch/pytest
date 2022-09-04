# A simple conftest file for pytest
# By Nick from CoffeeBeforeArch

import pytest

# A simple fixture that generates an input
@pytest.fixture
def initial_value():
    print("Providing the value 10!")
    return 10
