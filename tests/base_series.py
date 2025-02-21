from abc import ABC, abstractmethod
import math

class BaseSeries(ABC):
    def __init__(self, precision=1e-6):
        self.precision = precision

    @abstractmethod   
    def calculate(self): # child classes should implement this method
        pass


class SinSeries(BaseSeries): 
    def calculate(self, x):  # x is in radians
        if x > 2 * math.pi:
            x = x % (2 * math.pi)
        output = 0
        n = 0
        while True:
            term = (-1)**n * x**(2*n+1) / math.factorial(2*n+1)
            if abs(term) < self.precision:
                break
            output += term
            n += 1
        return output
    

class CosSeries(BaseSeries):
    def calculate(self, x):  # x is in radians
        if x > 2 * math.pi:
            x = x % (2 * math.pi)
        output = 0
        n = 0
        while True:
            term = (-1)**n * x**(2*n) / math.factorial(2*n)
            if abs(term) < self.precision:
                break
            output += term
            n += 1
        return output
    

class ExpSeries(BaseSeries):
    def calculate(self, x): # x is a real number (power of e)
        output = 0
        n = 0
        while True:
            term = x**n / math.factorial(n)
            if abs(term) < self.precision:
                break
            output += term
            n += 1
        return output
    

class LnSeriesTaylor(BaseSeries):
    def calculate(self, x): # x is a real number (positive and less than 2)
        self.precision = 1e-7
        if x <= 0 or x >= 2:
            raise ValueError("x must be between 0 and 2 (exclusive).")
        

        output = 0
        n = 1
        while True:
            term = ((-1)**(n+1))*((x - 1)**n / n)
            if abs(term) < self.precision:
                break
            output += term
            n += 1        
        return output
    
class LnSeries(BaseSeries):  # Gregory–Leibniz series
    def calculate(self, x):  # valid for x > 0
        self.precision = 1e-7
        if x <= 0:
            raise ValueError("x must be positive.")
        
        y = (x - 1) / (x + 1)  # Transformation for better convergence
        output = 0
        n = 0
        
        while True:
            term = (2 * (y ** (2 * n + 1))) / (2 * n + 1)
            if abs(term) < self.precision:
                break
            output += term
            n += 1
        
        return output  


# class Log
    

