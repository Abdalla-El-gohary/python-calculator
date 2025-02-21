#!/usr/env/bin python3

from base_series import SinhSeries , CoshSeries , TanhSeries
import math

actual_sinh_output = []
expected_sinh_output = []

actual_cosh_output = []
expected_cosh_output = []

actual_tanh_output = []
expected_tanh_output = []

# Create an instance of the SinhSeries class
sinh_series = SinhSeries()

# Create an instance of the CoshSeries class
cosh_series = CoshSeries()

# Create an instance of the TanhSeries class
tanh_series = TanhSeries()

def test_sinh_series():
    # calculate the sinh of numbers from -10 to 10
    for i in range(-89, 90):
        actual_sinh_output.append(sinh_series.calculate(math.radians(i)))
        expected_sinh_output.append(math.sinh(math.radians(i)))
        print(f"sinh({i}) = {actual_sinh_output[-1]}")
        print(f"expected: {expected_sinh_output[-1]}")

    # compare the actual and expected outputs (precision = 1e-6)
    for actual, expected in zip(actual_sinh_output, expected_sinh_output):
        assert abs(actual - expected) < 1e-6

def test_cosh_series():
    # calculate the cosh of numbers from -10 to 10
    for i in range(-89, 90):
        actual_cosh_output.append(cosh_series.calculate(math.radians(i)))
        expected_cosh_output.append(math.cosh(math.radians(i)))
        print(f"cosh({i}) = {actual_cosh_output[-1]}")
        print(f"expected: {expected_cosh_output[-1]}")

    # compare the actual and expected outputs (precision = 1e-6)
    for actual, expected in zip(actual_cosh_output, expected_cosh_output):
        assert abs(actual - expected) < 1e-6

def test_tanh_series():
    # calculate the tanh of numbers from -10 to 10
    for i in range(-89, 90):
        actual_tanh_output.append(tanh_series.calculate(math.radians(i)))
        expected_tanh_output.append(math.tanh(math.radians(i)))
        print(f"tanh({i}) = {actual_tanh_output[-1]}")
        print(f"expected: {expected_tanh_output[-1]}")

    # compare the actual and expected outputs (precision = 1e-6)
    for actual, expected in zip(actual_tanh_output, expected_tanh_output):
        assert abs(actual - expected) < 1e-6


if __name__ == "__main__":
    test_sinh_series()
    test_cosh_series()
    test_tanh_series()
    print("All tests passed!")