# -*- coding: utf-8 -*-
"""decimaltobinary.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ypVAWLinZDNXL7b8dwRlok3Qpy_c62d2

**Decimal to Binary Conversion**
"""

decimal = int(input("Enter a decimal number: "))
binary = bin(decimal)[2:]
print("Binary value:", binary)