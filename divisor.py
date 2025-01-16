# -*- coding: utf-8 -*-
"""divisor.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xqU3KSSQyDM0ZzqJjC98hDsKB57mGNYa
"""

def find_divisors(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return divisors

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Divisors of {n}: {find_divisors(n)}")