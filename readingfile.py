# -*- coding: utf-8 -*-
"""readingfile.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dAIKgFtFOx1I2skW6ld9YNyk-Aw2knVF
"""

file=open("/content/example.txt","r")
content=file.read()
print(content)
file.close()

file=open("/content/drive/MyDrive/nithin.txt","r")
content=file.readline()
print(content)
file.close()

file=open("/content/drive/MyDrive/nithin.txt","r")
content=file.readlines()
print(content)
file.close()
