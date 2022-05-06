# conftest.py is a file that pytest will automatically import fixtures from

import pytest

# A pytest hook to dynamically parametrize tests
def pytest_generate_tests(metafunc):
    if "num" in metafunc.fixturenames:
        entries = []
        for i in range(10):
            if i != 5:
                entries.append(i)
        metafunc.parametrize('num', entries)
