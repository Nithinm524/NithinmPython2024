# -*- coding: utf-8 -*-
"""mergelist.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WPgb5Nc58LoVXfnVj4lvjYjzrE5huVtB

merge two list
"""

# Input two lists of numbers
list1 = list(map(int, input("Enter the first list of numbers separated by space: ").split()))
list2 = list(map(int, input("Enter the second list of numbers separated by space: ").split()))

# Merge the lists
merged_list = list1 + list2

# Print the result
print(f"The merged list is: {merged_list}")