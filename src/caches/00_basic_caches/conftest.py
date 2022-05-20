# conftest.py is a file that pytest will automatically import fixtures from

import pytest
import random

# A function that we'll pretend is expensive to run
def expensive_computation():
    return random.randint(0, 10)


# A simple fixture that generates some inputs
# This uses the special request fixture that we can use to access the cache
@pytest.fixture
def value(request):
    # Try and get the value from the cache
    value = request.config.cache.get("expensive_value", None)

    # If we didn't find the value generate it, and set it in the cache
    if not value:
        print('Generating expensive value!')
        value = expensive_computation()
        request.config.cache.set("expensive_value", value)

    # Return our value
    return value
