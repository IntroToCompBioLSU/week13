#!/usr/bin/env python

import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt

fig = plt.figure()
fig.suptitle("Shoe sales before and after Thanksgiving", fontsize=8)
plt.xlabel("Last Weeks of November", fontsize=8)
plt.ylabel("Number of Shoes Sold", fontsize=8)
plt.plot([19,20,21,22,23,24,25,26,27,28,29,30], [0,0,3,4,50,60,65,55,45,60,65,40])
plt.axis([18, 30, 0, 100])
plt.show()

