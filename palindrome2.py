# -*- coding: utf-8 -*-
"""palindrome2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fP8t4gnpnqhTdBCS67EEgzxGv0layPbi

palindrome2
"""

number=input("enter a number:")
if str(number)==number[::-1]:
    print( "palindrome")
else:
    print("is not a palindrome")