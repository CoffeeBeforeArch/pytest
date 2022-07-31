# A example of adding argparse-style options to pytest
# By Nick from CoffeeBeforeArch

import pytest

# Adds the argparse-like option
def pytest_addoption(parser):
    parser.addoption("--name", action="store", default="Nick", help="Choose a name!")


# A simple fixture that gets our name option
@pytest.fixture
def name(request):
    return request.config.getoption("--name")
