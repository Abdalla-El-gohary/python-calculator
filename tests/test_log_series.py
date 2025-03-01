#!/usr/env/bin python3

from base_series import LognSeries
import math
import numpy as np

actual_log_output = []
expected_log_output = []

actual_logn_output = []
expected_logn_output = []

# Create an instance of the LnSeries class
log_series = LognSeries()
logn_series = LognSeries()

def test_log_series():
    # calculate the log of numbers from 1 to 10
    for i in np.arange(0.1, 18.0, 0.2):
        actual_log_output.append(log_series.calculate(i, 10))
        expected_log_output.append(math.log(i, 10))
        print(f"log({i}) = {actual_log_output[-1]}")
        print(f"expected: {expected_log_output[-1]}")
    
    # calculate the log base 10 of numbers from 1 to 10
    for i in np.arange(0.1, 18.0, 0.2):
        actual_logn_output.append(logn_series.calculate(i, i))
        expected_logn_output.append(math.log(i, i))
        print(f"log10({i}) = {actual_logn_output[-1]}")
        print(f"expected: {expected_logn_output[-1]}")

    # compare the actual and expected outputs (precision = 1e-6)
    for actual, expected in zip(actual_log_output, expected_log_output):
        assert abs(actual - expected) < 1e-6

    for actual, expected in zip(actual_logn_output, expected_logn_output):
        assert abs(actual - expected) < 1e-6


if __name__ == "__main__":
    test_log_series()
    print("All tests passed!")