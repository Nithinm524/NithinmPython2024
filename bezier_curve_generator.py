# -*- coding: utf-8 -*-
"""Bezier Curve Generator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mhp3AEjaDH-3o5BQASGy0dWCnwan69g6
"""

import numpy as np
import matplotlib.pyplot as plt

def bezier_curve(points, n=100):
    points = np.array(points)
    t = np.linspace(0, 1, n)
    curve = np.zeros((n, 2))
    n_points = len(points)
    for i in range(n_points):
        curve += (
            np.outer((1 - t) ** (n_points - i - 1) * t ** i, points[i])
            * np.math.comb(n_points - 1, i)
        )
    return curve

# Example usage
control_points = [(0, 0), (1, 2), (3, 3), (4, 0)]
curve = bezier_curve(control_points)
points = np.array(control_points)

plt.plot(points[:, 0], points[:, 1], "ro--", label="Control Points")
plt.plot(curve[:, 0], curve[:, 1], "b-", label="Bezier Curve")
plt.legend()
plt.show()