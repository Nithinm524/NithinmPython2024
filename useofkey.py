# -*- coding: utf-8 -*-
"""useofkey.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1li0KxQdNmah5AwVPjdVmjATggCM8yQ4k
"""

arr={}
arr[1]=1
arr['1']=2
arr[1]+=1

sum=0
for k in arr:
    sum+=arr[k]
print(sum)