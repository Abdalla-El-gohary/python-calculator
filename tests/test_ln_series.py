#!/usr/env/bin python3

from base_series import LnSeries
import math
import numpy as np


actual_ln_output = []
expected_ln_output = []

# Create an instance of the LnSeries class
ln_series = LnSeries()

def test_ln_series():
    # calculate the ln of numbers from 1 to 10
    for i in np.arange(0.1, 2.0, 0.2):
        actual_ln_output.append(ln_series.calculate(i))
        expected_ln_output.append(math.log(i))
        print(f"ln({i}) = {actual_ln_output[-1]}")
        print(f"expected: {expected_ln_output[-1]}")

    # compare the actual and expected outputs (precision = 1e-6)
    for actual, expected in zip(actual_ln_output, expected_ln_output):
        assert abs(actual - expected) < 1e-6


if __name__ == "__main__":
    test_ln_series()
    print("All tests passed!")