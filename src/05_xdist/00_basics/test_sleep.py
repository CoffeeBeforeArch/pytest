# A simple test where each variant sleeps for 1s each
# By Nick from CoffeeBeforeArch

import pytest
import time


def expensive_function():
    time.sleep(1)


@pytest.mark.parametrize("variant", range(10))
def test_sleep(variant):
    expensive_function()
