# -*- coding: utf-8 -*-
"""intersectionlist.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UPYUgvmJIHKBedAMgtLSmJfm6OZsvzDT

Find the Intersection of Two Lists
"""

# Input two lists of numbers
list1 = list(map(int, input("Enter the first list of numbers separated by space: ").split()))
list2 = list(map(int, input("Enter the second list of numbers separated by space: ").split()))

# Find the intersection
intersection = list(set(list1) & set(list2))

# Print the result
print(f"The intersection of the two lists is: {intersection}")