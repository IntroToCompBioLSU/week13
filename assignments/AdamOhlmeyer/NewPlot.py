#!/usr/bin/env python

import matplotlib.pyplot as plt

#Statisitcs for Saquon Barkley's 2018 Fantasy Scoring 

fig = plt.figure()
fig.suptitle('2018 Fantasy Points per Game for Saquon Barkley', fontsize=18)
plt.xlabel('Game', fontsize=14)
plt.ylabel('Points', fontsize=14)
plt.plot([1,2,3,4,5,6,7,8,9,10,11], [20.8,24.8,22.7,22,28.9,37.9,26.4,20.1,0,14,35.2], 'bD')
plt.axis([0, 12, 0, 40])
plt.show()

# DB: Good!