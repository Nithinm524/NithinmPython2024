# -*- coding: utf-8 -*-
"""quantumvisualizer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14ta_ZrNoINjP51XTOTcY5Mw1AGZHQmMe

Quantum Number Visualizer
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_orbital(n, l, m):
    phi = np.linspace(0, 2 * np.pi, 100)
    theta = np.linspace(0, np.pi, 100)
    phi, theta = np.meshgrid(phi, theta)

    # Example spherical harmonics-like function
    r = (np.sin(theta)**l) * np.abs(np.cos(m * phi))**2

    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)

    # Plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(x, y, z, cmap="viridis", edgecolor="none")
    ax.set_title(f"Orbital Visualization: n={n}, l={l}, m={m}")
    plt.show()

# Input quantum numbers
n = int(input("Enter principal quantum number (n): "))
l = int(input("Enter azimuthal quantum number (l): "))
m = int(input("Enter magnetic quantum number (m): "))
visualize_orbital(n, l, m)