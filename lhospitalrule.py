# -*- coding: utf-8 -*-
"""lhospitalrule.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rOoIcS5E06nuaAgLY8PgZL1oPeTWomm9

We can evaluate inderminate forms easily in python using Limit comman 1. lim
 x→0
 sin(x)
"""

from sympy import Limit, Symbol,exp,sin
x=Symbol('x')
l=Limit((sin(x))/x,x,0).doit()
print(l)

"""2. Evaluate lim
 x→1
 ((5x4−4x2−1)
 (10−x−9x3)
"""

from sympy import *
x=Symbol('x')
l=Limit((5*x**4-4*x**2-1)/(10-x-9*x**3),x,1).doit()
print(l)

""" 3. Prove that limx→∞ 1+ 1
 x
 x=e
"""

from sympy import *
from math import inf
x=Symbol('x')
l=Limit((1+1/x)**x,x,inf).doit()
display(l)