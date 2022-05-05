# conftest.py is a file that pytest will automatically import fixtures from

import pytest
import random

# A function that we'll pretend is expensive to run
def expensive_computation():
    print("Running expensive computation!")
    return random.randint(0, 10)


# A simple fixture that generates some inputs
# This uses the special request fixture that we can use to access the cache
@pytest.fixture
def inputs(request):
    # Try and get the value from the cache
    random_number = request.config.cache.get("example/value", None)

    # If we didn't find the value generate it, and set it in thecache
    if not random_number:
        random_number = expensive_computation()
        request.config.cache.set("example/value", random_number)

    # Return a list with random number of elements
    return [i for i in range(random_number)]
