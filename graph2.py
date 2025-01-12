# -*- coding: utf-8 -*-
"""graph2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mEc4S01dXG5TUOCQou4rB40J-IhnIEaD
"""

!pip install sympy
from sympy import plot_implicit, Eq, symbols

# Define symbols
x, y = symbols('x y')

# Plot the implicit equation
p4 = plot_implicit(
    Eq((y**2)*(3-x), x**3), (x, -2, 5), (y, -5, 5)  # a=3
)