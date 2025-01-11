# -*- coding: utf-8 -*-
"""generativeart.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19ZrIbWcS3X0-9YbsEOy4bGCABDBUeV_S

Creative Programming: Generative Art
"""

import matplotlib.pyplot as plt
import numpy as np

def generate_art():
    fig, ax = plt.subplots(figsize=(8, 8))
    for _ in range(30):  # Draw 30 random lines
        x = np.random.rand(2)  # Start and end x-coordinates
        y = np.random.rand(2)  # Start and end y-coordinates
        color = np.random.rand(3,)  # Random RGB color
        linewidth = np.random.rand() * 3 + 1  # Random line thickness
        ax.plot(x, y, color=color, linewidth=linewidth)

    ax.set_axis_off()
    plt.show()

generate_art()