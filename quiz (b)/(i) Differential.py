import sympy as sp

# Define the variable and the function
x = sp.symbols('x')
f = x**3 + 2*x**2 + x + 1

# Differentiate the function
f_prime = sp.diff(f, x)

f_prime
