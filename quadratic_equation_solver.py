# -*- coding: utf-8 -*-
"""Quadratic Equation Solver.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RyREsuVLTTyw2UmlUD1PPpCQxRylmZEm
"""

import cmath

def solve_quadratic(a, b, c):
    discriminant = cmath.sqrt(b ** 2 - 4 * a * c)
    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)
    return root1, root2

# Example usage
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
root1, root2 = solve_quadratic(a, b, c)
print(f"Roots of the equation are {root1} and {root2}")