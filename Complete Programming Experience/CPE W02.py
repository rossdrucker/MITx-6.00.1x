# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:58:37 2019

@author: rdrucker
"""

import math

def polysum(n, s):
    a = (.25 * n * (s**2))/math.tan(math.pi/n)
    p = n * s
    return round(a + (p**2), 4)