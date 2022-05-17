# A simple conftest file for pytest
# By Nick from CoffeeBeforeArch

import pytest

# A simple fixture that prints that tests are starting
@pytest.fixture(autouse=True)
def log_start():
    print('Test Starting!')
