# -*- coding: utf-8 -*-
"""boolean conversions.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xM-_KBR89aSSFG5-tze_QHmWtmusMEuF
"""

def binary_to_decimal(binary):
    return int(binary, 2)

def decimal_to_binary(decimal):
    return bin(decimal)[2:]

if __name__ == "__main__":
    choice = input("Convert (1) Binary to Decimal or (2) Decimal to Binary? ")
    if choice == "1":
        binary = input("Enter a binary number: ")
        print(f"Decimal: {binary_to_decimal(binary)}")
    elif choice == "2":
        decimal = int(input("Enter a decimal number: "))
        print(f"Binary: {decimal_to_binary(decimal)}")
    else:
        print("Invalid choice!")