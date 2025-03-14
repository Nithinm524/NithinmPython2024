# -*- coding: utf-8 -*-
"""Random Quote Generator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dLWiugpdywjzXY_RFEuGJsyGt_vfaWUH
"""

import random

def random_quote():
    quotes = [
        "The best way to predict the future is to create it.",
        "Believe you can and you're halfway there.",
        "Your time is limited, so don’t waste it living someone else’s life.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Act as if what you do makes a difference. It does."
    ]
    print(random.choice(quotes))

if __name__ == "__main__":
    random_quote()