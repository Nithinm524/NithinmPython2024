# -*- coding: utf-8 -*-
"""calendergenerator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1C6c0Ej8PfEug6prO4aaHqVYps74ovR6K

**Generate a Calendar for a Given Month**
"""

import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
print(calendar.month(year, month))