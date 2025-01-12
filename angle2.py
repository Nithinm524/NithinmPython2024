# -*- coding: utf-8 -*-
"""angle2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1X_9BW69NZOKybesdgBkf4u-CP8wYGxes

Find the angle between the curves r = 4cost and r = 5sint
"""

from sympy import *
 r,t =symbols('r,t')
 r1=4*(cos(t));
 r2=5*(sin(t));
 dr1=diff(r1,t)
 dr2=diff(r2,t)
 t1=r1/dr1
 t2=r2/dr2
 q=solve(r1-r2,t)
 w1=t1.subs({t:float(q[0])})
 w2=t2.subs({t:float(q[0])})
 y1=atan(w1)
 y2=atan(w2)
 w=abs(y1-y2)
 print('Angle between curves in radians is %0.4f'%float(w))