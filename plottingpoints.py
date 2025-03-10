# -*- coding: utf-8 -*-
"""plottingpoints.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VRfsOCqiV0leT6d6itzic9_aIAF3p8sM

Plotting points(Scattered plot
"""

# importing the required module
 import matplotlib.pyplot as plt
 x = [1,2,3,4,6,7,8] # x axis values
 y = [2,7,9,1,5,10,3] # corresponding y axis values
 plt.scatter(x, y) # plotting the points
 plt.xlabel('x- axis') # naming the x axis
 plt.ylabel('y- axis') # naming the y axis
 plt.title('Scatter points') # giving a title to my graph
 plt.show() # function to show the plot