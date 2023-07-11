# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 18:22:54 2023

@author: be
"""

import numpy as np 
import MCintegrate as mc

def f(x):
    return (x+x**2)
a=0 
b=1
n= 50000
integral = mc.MCint(f, a, b, n)

print(f"integral = {integral: 0.3f}")



#f(x)=x+x^2     a=0 b=1 max=2 