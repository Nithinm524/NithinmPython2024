# -*- coding: utf-8 -*-
"""Cycloid: x = a(θ −sinθ);y = a(1−sinθ.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1S9vEpp62pBXe4HbiNUjQ11McWcUl9_JY
"""

import numpy as np # import numpy library and alias as np
import matplotlib.pyplot as plt # import matplotlib.pyplot and alias as plt

def cycloid(r):
  x = [] #create the list of x coordinates
  y = [] #create the list of y coordinates
  for theta in np.linspace(-2*np.pi, 2*np.pi, 100):
 #loop over a list of theta, which ranges from-2 pi to 2 pi
     x.append(r*(theta- np.sin(theta)))
 #add the corresponding expression of x to the x list
     y.append(r*(1- np.cos(theta))) #same for y
  plt.plot(x,y) #plot using matplotlib.piplot
  plt.show() #show the plot
cycloid(2) #call the function