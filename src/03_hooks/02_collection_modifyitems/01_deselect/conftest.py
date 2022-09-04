# conftest.py is a file that pytest will automatically import fixtures from

import os

# A pytest hook to for modifying collected items
def pytest_collection_modifyitems(items, config):
    # Get an environment variable
    skip_odds = os.environ.get("SKIP_ODDS", "False").lower()
    skip_odds = True if skip_odds == "true" else False

    selected = []
    deselected = []
    for item in items:
        # Get the value from the callspec
        num = item.callspec.params.get("initial_value")

        # Either add to deselected or selected lists
        if skip_odds and num % 2:
            deselected.append(item)
        else:
            selected.append(item)

    # Update the deselected tests
    config.hook.pytest_deselected(items=deselected)

    # Update the selected tests
    items[:] = selected
