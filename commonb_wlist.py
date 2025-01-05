# -*- coding: utf-8 -*-
"""commonb/wlist.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1t--8NHyDmB5DXN8i_zdVyG5yXjGeL_4N

common between list
"""

# Input two lists of numbers
list1 = list(map(int, input("Enter the first list of numbers separated by space: ").split()))
list2 = list(map(int, input("Enter the second list of numbers separated by space: ").split()))

# Find common elements
common_elements = list(set(list1) & set(list2))

# Print the result
print(f"The common elements between the two lists are: {common_elements}")