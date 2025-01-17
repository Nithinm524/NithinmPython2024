# -*- coding: utf-8 -*-
"""Collatz Conjecture.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gLyY1KbE8GPR17Kare9Dxti7mRlJx-YU
"""

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Example usage
number = int(input("Enter a number: "))
print(f"Collatz sequence: {collatz_sequence(number)}")