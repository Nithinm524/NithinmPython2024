# -*- coding: utf-8 -*-
"""gcd.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1u-rqi9Y_h68mSMAPc90I1lTWGGrSvviF

gcd
"""

def gcd(a,b):
    while b!=0:
       a,b=b,a%b
    return a
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
print("the gcd of",num1,"and",num2,"is",gcd(num1,num2))