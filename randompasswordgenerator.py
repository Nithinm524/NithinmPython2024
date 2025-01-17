# -*- coding: utf-8 -*-
"""randompasswordgenerator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1k85S_CJaIUDljXKNVMqV3-eXNGXfzEOz

Generate Random Password
"""

import random
import string

# Password length
length = int(input("Enter the password length: "))

# Generate password
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))

# Print the result
print(f"Generated password: {password}")