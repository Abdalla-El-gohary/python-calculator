import math
import re
from series_calculations.base_series import SinSeries, CosSeries, TanSeries, LnSeries, LognSeries, ExpSeries, SinhSeries, CoshSeries, TanhSeries


class Postfix:
    def __init__(self):
        self.mapping_dict = {
            'π': str(math.pi),
            'e': str(math.e)
        }

    def infix_to_postfix(self, expression):
        precedence = {
            'lon': 3, # log with base n
            'log': 3,
            'ln': 3,
            'sin': 3,
            'cos': 3,
            'tan': 3,
            'asin': 3,
            'acos': 3,
            'atan': 3,
            'sinh': 3,
            'cosh': 3,
            'tanh': 3,
            'asinh': 3,
            'acosh': 3,
            'atanh': 3,
            '^': 3,
            '*': 2,
            '/': 2,
            '+': 1,
            '-': 1,
            '(': 0,
            ')': 0
        }
        stack = []
        postfix = []
        

        tokens = re.findall(r"[\d.]+|[-\d.]+|[A-Za-z]+|\S", expression) # Tokenize the expression
        
        for token in tokens:
            if token.replace("-", "", 1).replace(".", "", 1).isnumeric():
                postfix.append(token)
            elif  token in ['π', 'e']:  # numerical constants
                postfix.append(self.mapping_dict[token])
                print(self.mapping_dict[token])
            elif token in precedence:
                if token == '(':
                    stack.append(token)
                elif token == ')':
                    while stack and stack[-1] != '(':
                        postfix.append(stack.pop())
                    stack.pop()
                else:
                    while stack and precedence[stack[-1]] >= precedence[token]:
                        postfix.append(stack.pop())
                    stack.append(token)
            else:
                postfix.append(token)
        while stack:
            postfix.append(stack.pop())
        return postfix
    
    def evaluate_postfix(self, postfix):
        stack = []
        for token in postfix:
            if token.replace("-", "", 1).replace(".", "", 1).isnumeric():
                stack.append(float(token))
            elif token == 'e':
                stack.append('e')
            elif token in ['sin', 'cos', 'tan', 'log', 'ln', 'lon', 'sinh', 'cosh', 'tanh', 'asin', 'acos', 'atan', 'asinh', 'acosh', 'atanh']:
                arg = stack.pop()
                if token == 'sin':
                    sin_series = SinSeries()
                    stack.append(sin_series.calculate(math.radians(arg)))
                elif token == 'cos':
                    cos_series = CosSeries()
                    stack.append(cos_series.calculate(math.radians(arg)))
                elif token == 'tan':
                    tan_series = TanSeries()
                    stack.append(tan_series.calculate(math.radians(arg)))
                
                elif token == 'sinh':
                    sinh_series = SinhSeries()
                    stack.append(sinh_series.calculate(arg))
                elif token == 'cosh':
                    cosh_series = CoshSeries()
                    stack.append(cosh_series.calculate(arg))
                elif token == 'tanh':
                    tanh_series = TanhSeries()
                    stack.append(tanh_series.calculate(arg))
                elif token == 'asin':
                    stack.append(math.degrees(math.asin(arg)))
                elif token == 'acos':
                    stack.append(math.degrees(math.acos(arg)))
                elif token == 'atan':
                    stack.append(math.degrees(math.atan(arg)))
                elif token == 'asinh':
                    stack.append(math.degrees(math.asinh(arg)))
                elif token == 'acosh':
                    stack.append(math.degrees(math.acosh(arg)))
                elif token == 'atanh':
                    stack.append(math.degrees(math.atanh(arg)))

                elif token == 'ln':
                    ln_series = LnSeries()
                    stack.append(ln_series.calculate(arg))
                
                elif token == 'log':
                    log_series = LognSeries()
                    stack.append(log_series.calculate(arg, 10))
                elif token == 'lon':
                    print(self.base_log)
                    logn_series = LognSeries()
                    stack.append(logn_series.calculate(arg, float(self.base_log)))

            
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(a / b)
                elif token == '^':
                    if a == math.e:
                        myex = ExpSeries()
                        stack.append(myex.calculate(x=b))
                    else:
                        stack.append(a ** b)
        return stack[0]

