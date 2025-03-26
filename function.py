#function file
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def modulus(a, b):
    return a % b

def reciprocal(a):
    if a == 0:
        raise ValueError("Cannot divide by zero")
    return 1 / a

def square(a):
    return a ** 2

def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(a)

def logarithm(a):
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers")
    return math.log10(a)

def natural_log(a):
    if a <= 0:
        raise ValueError("Natural logarithm undefined for non-positive numbers")
    return math.log(a)

def sine(a):
    return math.sin(math.radians(a))

def cosine(a):
    return math.cos(math.radians(a))

def tangent(a):
    if (a % 180) == 90:  
        raise ValueError("Tangent is undefined at this angle")
    return math.tan(math.radians(a))

