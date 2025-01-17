# -*- coding: utf-8 -*-
"""3D Plot Using Matplotlib.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14MKK8gtfzpCqyng2bh1wMMk1l04pcz4Z
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw_3d_plot():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = [1, 2, 3, 4]
    y = [4, 3, 2, 1]
    z = [1, 2, 3, 4]

    ax.scatter(x, y, z)
    ax.set_title("3D Plot Example")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    plt.show()

if __name__ == "__main__":
    draw_3d_plot()