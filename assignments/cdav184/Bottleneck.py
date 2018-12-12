#!/usr/bin/env python

import matplotlib.pyplot as plt

fig = plt.figure()
fig.suptitle("Number of offspring produced after bottleneck occurs", fontsize=18)
plt.xlabel("Days Post-Bottleneck", fontsize=14)
plt.ylabel("Offspring", fontsize=14)
plt.plot([0,1,2,3,4,5,6,7,8,9,10], [100,90,80,70,60,50,40,30,20,10,0])
plt.axis([0, 50, 0, 100])
plt.show()

# DB: Good!