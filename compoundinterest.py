# -*- coding: utf-8 -*-
"""compoundinterest.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13aBX8oinn-Ic3DOvkv5SZrGkejKyWPb4

Calculate Compound Interest
"""

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time (in years): "))
compound_interest = principal * ((1 + rate / 100) ** time) - principal
print("Compound Interest:", compound_interest)