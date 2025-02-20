#!/usr/bin/env python3

from base_series import CosSeries
import math

actual_cos_output = []
expected_cos_output = []

# Create an instance of the CosSeries class
cos_series = CosSeries()

def test_cos_series():
    # calculate the cos of angles from 0 to 358 degrees
    for i in range(0, 360, 2):
        actual_cos_output.append(cos_series.calculate(math.radians(i)))
        expected_cos_output.append(math.cos(math.radians(i)))
        print(f"cos({i}) = {actual_cos_output[-1]}")
        print(f"expected: {expected_cos_output[-1]}\n")

    # compare the actual and expected outputs (precision = 1e-6)
    for actual, expected in zip(actual_cos_output, expected_cos_output):
        assert abs(actual - expected) < 1e-6


if __name__ == "__main__":
    test_cos_series()
    print("All tests passed!")