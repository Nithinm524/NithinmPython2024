# -*- coding: utf-8 -*-
"""raisingexceptions.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A32aZ_77hmUj7wpZFcUB9KapyP9zk1WE

raising exceptions
"""

def check_age(age):
    if age<18:
        raise ValueError("age must be greater than 18.")
    return True

try:
     check_age(16)
except ValueError as e:
     print(e)