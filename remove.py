# -*- coding: utf-8 -*-
"""Remove.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dp3BC-E_37hZtBaGhXH0CQ299gDOoIhc

remove character from a string
"""

s = input("Enter a string: ")
result = ""
for char in s:
    if char not in result:
        result += char
print(result)