# conftest.py is a file that pytest will automatically import fixtures from


# A pytest hook to for modifying collected items
def pytest_collection_modifyitems(items, config):
    selected = []
    deselected = []
    for item in items:
        # Get the value from the callspec
        num = item.callspec.params.get("initial_value")
        if num in [1, 5]:
            deselected.append(item)
        else:
            selected.append(item)

    # Update the deselected tests
    config.hook.pytest_deselected(items=deselected)

    # Update the selected tests
    items[:] = selected
