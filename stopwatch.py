# -*- coding: utf-8 -*-
"""Stopwatch.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TQsK-y8N6YR52VnYm7eaDYWyy_MPiQ4c

Simple Stopwatch
"""

import time

input("Press Enter to start the stopwatch.")
start_time = time.time()

input("Press Enter to stop the stopwatch.")
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds.")