# -*- coding: utf-8 -*-
"""randomgame.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1x0_wMJ_Tq7C3-TVirEoRk1DtsC5GZVJL

**random guess number**
"""

import random
number = random.randint(1, 100)
guess = 0

while guess != number:
    guess = int(input("Guess a number (1-100): "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You guessed it!")