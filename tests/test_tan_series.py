#!/usr/env/bin python3

from base_series import TanSeries
import math

actual_tan_output = []
expected_tan_output = []

# Create an instance of the TanSeries class
tan_series = TanSeries()

def test_tan_series():
    # calculate the tan of numbers from -10 to 10
    for i in range(-80, 80):
        actual_tan_output.append(tan_series.calculate(math.radians(i)))
        expected_tan_output.append(math.tan(math.radians(i)))
        print(f"tan({i}) = {actual_tan_output[-1]}")
        print(f"expected: {expected_tan_output[-1]}")

    # compare the actual and expected outputs (precision = 1e-6)
    for actual, expected in zip(actual_tan_output, expected_tan_output):
        print(f"actual: {actual}, expected: {expected}")
        assert abs(actual - expected) < 1e-6


if __name__ == "__main__":
    test_tan_series()
    print("All tests passed!")