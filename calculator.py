"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# Second changes
def square_root(a):
    try:
        if(a < 0):
            raise ValueError

        return math.sqrt(a)

    except ValueError as e:
        print(str(e))
    except Exception as e:
        print(str(e))

def hypotenuse(a , b):
    return math.hypot(a , b)




# First example
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def mul(a,b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    if b <= 0 or b == 1:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b