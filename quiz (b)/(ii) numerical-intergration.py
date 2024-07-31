import scipy.integrate as spi
import numpy as np

# Define the function
def f(x):
    return x**3 + 2*x**2 + x + 1

# Perform numerical integration over the interval [0, 2]
result, error = spi.quad(f, 0, 2)

result
