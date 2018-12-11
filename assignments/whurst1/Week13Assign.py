#!/usr/bin/env python

#import accessories
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
fig.suptitle("Car MPG over Size")
plt.xlabel("MPG")
plt.ylabel("Weight (Lbs)")
plt.plot([0,5,10,20,30,40,50,60], [104,98,85,70,57,44,36,51])
plt.axis([0, 100, 0, 250])
plt.show()
