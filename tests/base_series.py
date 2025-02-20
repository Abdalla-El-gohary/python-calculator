from abc import ABC, abstractmethod
import math

class BaseSeries(ABC):
    def __init__(self, precision=1e-6):
        self.precision = precision

    @abstractmethod   
    def calculate(self): # child classes should implement this method
        pass


class SinSeries(BaseSeries): 
    def calculate(self, input):  # input is in radians
        input = input
        if input > 2 * math.pi:
            input = input % (2 * math.pi)
        output = 0
        n = 0
        while True:
            term = (-1)**n * input**(2*n+1) / math.factorial(2*n+1)
            if abs(term) < self.precision:
                break
            output += term
            n += 1
        return output
    

class CosSeries(BaseSeries):
    def calculate(self, input):  # input is in radians
        input = input
        if input > 2 * math.pi:
            input = input % (2 * math.pi)
        output = 0
        n = 0
        while True:
            term = (-1)**n * input**(2*n) / math.factorial(2*n)
            if abs(term) < self.precision:
                break
            output += term
            n += 1
        return output