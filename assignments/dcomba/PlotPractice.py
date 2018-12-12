#!/usr/bin/env python

#plotting a graph similar to the graphs I will be using for the final project

import numpy as np 
import matplotlib.pyplot as plt

time = np.arange(25)
population = np.random.randint(0, 25, size =(time.size))

plt.plot(time, population, color="m")
plt.xlabel("time")
plt.ylabel("population")
plt.title("Population over time")

plt.show()

# DB: Good!