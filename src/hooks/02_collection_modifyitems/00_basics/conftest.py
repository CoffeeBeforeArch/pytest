# conftest.py is a file that pytest will automatically import fixtures from

import pytest

# A pytest hook to for modifying collected items
def pytest_collection_modifyitems(items, config):
    # Even tests are selected, odds are deselected
    for i, item in enumerate(items):
        if i % 2:
            item.add_marker(pytest.mark.skip(reason="Skipping every other test!"))
