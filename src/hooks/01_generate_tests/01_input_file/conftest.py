# conftest.py is a file that pytest will automatically import fixtures from

import pytest

# A pytest hook for adding an option
def pytest_addoption(parser):
    parser.addoption(
        "--input_file", action="store", default="", help="Choose an input file!"
    )


# A pytest hook to dynamically parametrize tests
def pytest_generate_tests(metafunc):
    # Check if the num fixture is used
    if "num" in metafunc.fixturenames:
        # Get the command line option
        input_file = metafunc.config.getoption("--input_file")

        # Read the data from the input file (if specified)
        data = []
        if input_file:
            with open(input_file, "r") as f:
                lines = f.readlines()
            data = [int(line) for line in lines]

        # Parametrize the test
        metafunc.parametrize("num", data)
