# -*- coding: utf-8 -*-
"""count.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bfYuNhtq6-JFOAbEnnnq-JDha7rmh4r8

count
"""

numbers=[1,2,2,3,3,3,4,4,4,4,4]
frequency={}
for num in numbers:
    frequency[num]=frequency.get(num,0)+1
print("frequency:",frequency)