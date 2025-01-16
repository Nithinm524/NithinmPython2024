# -*- coding: utf-8 -*-
"""Draw a Pie Chart Using Matplotlib.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PtKzvCwR0q9Jr2aBj5geX0Ce0CD-w-UN
"""

import matplotlib.pyplot as plt

def draw_pie_chart():
    labels = ['Python', 'C', 'Java', 'JavaScript']
    sizes = [40, 30, 20, 10]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title("Programming Language Usage")
    plt.show()

if __name__ == "__main__":
    draw_pie_chart()