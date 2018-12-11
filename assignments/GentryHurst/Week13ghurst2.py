#!/usr/bin/env python

#import libraries 
import numpy as np
import matplotlib.pyplot as plt

#define number of columns,mean values, width of bars
N = 4
Means = (15, 17, 30, 24)
ind = np.arange(N)
width = 0.5

p1 = plt.bar(ind, Means, width)
#labeling the graph
plt.ylabel('Number')
plt.title('Number of times each nucleotide occurs in short read overlap')
plt.xticks(ind, ('A', 'T', 'G', 'C'))
plt.yticks(np.arange(0,100,5))
#determine the color of columns
p1[0].set_color('fuchsia')
p1[1].set_color('cyan')
p1[2].set_color('chartreuse')
p1[3].set_color('salmon')
#prints plot to screen
plt.show()
