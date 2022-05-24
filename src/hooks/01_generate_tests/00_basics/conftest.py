# conftest.py is a file that pytest will automatically import fixtures from

import pytest

# A pytest hook to dynamically parametrize tests
def pytest_generate_tests(metafunc):
    if "num" in metafunc.fixturenames:
        metafunc.parametrize("num", [1, 2 ,3 ,4, 5])
