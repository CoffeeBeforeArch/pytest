# A simple test of parallelizing tests with xdist
# By Nick from CoffeeBeforeArch

import pytest
import time

# A simple function that sleeps for 1 second
def sleep():
    time.sleep(1)


# A test for our sleep function
@pytest.mark.parametrize("variant", range(10))
def test_sleep(variant):
    sleep()
