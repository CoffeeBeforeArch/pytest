# conftest.py is a file that pytest will automatically import fixtures from


# A pytest hook to for modifying collected items
def pytest_collection_modifyitems(items, config):
    # Even tests are selected, odds are deselected
    selected = []
    deselected = []
    for i, item in enumerate(items):
        if i % 2:
            deselected.append(item)
        else:
            selected.append(item)

    # Update the deselected tests
    config.hook.pytest_deselected(items=deselected)

    # Update the selected tests
    items[:] = selected
