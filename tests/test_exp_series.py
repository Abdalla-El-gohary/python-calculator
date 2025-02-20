#!/usr/bin/env python3

from base_series import ExpSeries
import math

actual_exp_output = []
expected_exp_output = []

# Create an instance of the ExpSeries class
exp_series = ExpSeries()

def test_exp_series():
    # calculate the exp of numbers from -5 to 5
    for i in range(-5, 6):
        actual_exp_output.append(exp_series.calculate(i))
        expected_exp_output.append(math.exp(i))
        print(f"exp({i}) = {actual_exp_output[-1]}")
        print(f"expected: {expected_exp_output[-1]}")

    # compare the actual and expected outputs (precision = 1e-6)
    for actual, expected in zip(actual_exp_output, expected_exp_output):
        assert abs(actual - expected) < 1e-6


if __name__ == "__main__":
    test_exp_series()
    print("All tests passed!")