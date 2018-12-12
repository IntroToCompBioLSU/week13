#!/usr/bin/env python

# script to practice plotting

import numpy as np 
import matplotlib.pyplot as plt

range = np.arange(50)
growth = np.random.randint(0, 25, size =(range.size))
time = 0 + range

#print("this is the range: %s" % range)
#print("this is the growth: %s" % growth) 
plt.plot(time, growth, color="m")
plt.xlabel("time")
plt.ylabel("growth")
plt.title("Growth over time")

plt.show()

# DB: Good!