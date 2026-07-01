# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 20:12:36 2026

@author: SMMH
"""

import numpy as np



print("قراره دو ماتریس n*nدرست کنیم")
print("بعد از درست کردن باهم ضرب کنیم")


print("فقط کافیه n رو مشخص کنی")
while True:
    try:
        
      sa = int(input())
      if isinstance(sa, int): 
            print("اولین ماتریس رو درست کن")
            break
    except ValueError:
            print("یک عدد طبیعی وارد کن")
    



a=[]
for i in range(sa):
    for j in range(sa):
        while True:
          try:
             print(f"وارد کنن درایه ی {i+1}{j+1}")
             b=float(input())
             a.append(b)
             break
          except ValueError:
            print("لطفا عدد وارد کنید")
c=np.array(a).reshape(sa, sa)
print("دومین ماتریس رو درست کن")
d=[]
for i in range(sa):
    for j in range(sa):
        while True:
          try:
             print(f"وارد کنن درایه ی {i+1}{j+1}")
             h=float(input())
             d.append(h)
             break
          except ValueError:
            print("لطفا عدد وارد کنید")
g=np.array(d).reshape(sa, sa)
print("صبر کنید")
print("...")
print("...")
print(c)
print("*")
print(g)
print("=")
print(c@g)
