# -*- coding: utf-8 -*-
"""factorial(recursion).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XDwWy1UBzOD2Anf0PuNHrjTzyR2mCbHj

factorial using recursion
"""

def factorial(n):
    if n==0:
       return 1
    else:
       return n*factorial(n-1)
number=int(input("enter a number:"))
print("factorial:",factorial(number))