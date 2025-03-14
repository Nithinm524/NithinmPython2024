# -*- coding: utf-8 -*-
"""Snake Case to Camel Case Converter.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WZJ7VZ3jgI1GGP2yX-BFWXm8fUS_B22s
"""

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)

if __name__ == "__main__":
    snake_str = input("Enter a snake_case string: ")
    print(f"CamelCase: {snake_to_camel(snake_str)}")