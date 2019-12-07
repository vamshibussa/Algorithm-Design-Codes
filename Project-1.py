#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 20:22:20 2019

@author: vamshi
"""

import time 
import math

def Iterfib(n):
    a = [0]
    if n>0:
        a.append(1)
        for i in range(2,n+1):
            b = a[i-1]+a[i-2]
            a.append(b)
    return a[n]        

def Recurfib(n):
    if n<= 1:
        return n;
    else:
        return Recurfib(n-1)+Recurfib(n-2)
    return 0;

Calculate_Recurfib = time.time()
Recurfib_outcome = Recurfib(35)
Finish_Recurfib = time.time()
print(Finish_Recurfib-Calculate_Recurfib,'seconds')


Calculate_Iterfib = time.time()
Iterfib_outcome = Iterfib(35)
Finish_Iterfib = time.time()
print(Finish_Iterfib-Calculate_Iterfib,'seconds')





