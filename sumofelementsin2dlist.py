# -*- coding: utf-8 -*-
"""sumofelementsin2dlist.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1r_4uFPQvMG490nAOy5NVgn8TFsMS28j7

Find the Sum of the Diagonal Elements in a 2D List
"""

# Input a 2D list (matrix)
matrix = [
    list(map(int, input("Enter a row of numbers separated by space: ").split()))
    for _ in range(3)
]

# Calculate the sum of diagonal elements
diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))

# Print the result
print(f"The sum of the diagonal elements is: {diagonal_sum}")