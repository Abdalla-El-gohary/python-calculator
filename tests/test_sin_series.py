#!/usr/bin/env python3

from base_series import SinSeries
import math

actual_sin_output = []
expected_sin_output = []

# Create an instance of the SinSeries class
sin_series = SinSeries()

def test_sin_series():
    # calculate the sin of angles from 0 to 358 degrees
    for i in range(0, 360, 2):
        actual_sin_output.append(sin_series.calculate(math.radians(i)))
        expected_sin_output.append(math.sin(math.radians(i)))
        print(f"sin({i}) = {actual_sin_output[-1]}")
        print(f"expected: {expected_sin_output[-1]}")

    # compare the actual and expected outputs (precision = 1e-6)
    for actual, expected in zip(actual_sin_output, expected_sin_output):
        assert abs(actual - expected) < 1e-6



if __name__ == "__main__":
    test_sin_series()
    print("All tests passed!")

    



  


