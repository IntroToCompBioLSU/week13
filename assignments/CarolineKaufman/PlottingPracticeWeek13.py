#!/usr/bin/env python


import matplotlib.pyplot as plt
import numpy as np

def f(t):
    'A damped exponential'
    s1 = np.cos(2 * np.pi * t)
    e1 = np.exp(-t)
    return s1 * e1

t1 = np.arange(0.0, 5.0, .2) #set min and max 

l = plt.plot(t1, f(t1), 'ro')
plt.setp(l, markersize=10) #size of points
plt.setp(l, markerfacecolor='C0') #color of points

plt.show()